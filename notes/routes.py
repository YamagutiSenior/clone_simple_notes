import os
import socket

from notes import db, note, auth, users
from notes.forms import AddForm, AdminForm, ResetForm, DeleteForm
from flask import render_template, request, flash, redirect, jsonify
from werkzeug.security import check_password_hash


@note.route('/', methods=['GET', 'POST'])
@note.route('/index', methods=['GET', 'POST'])
def index():
    logo = os.path.join(note.config['IMAGE_FOLDER'], 'gitlab-logo-100.png')

    items = []

    conn = db.create_connection()
    ing_path = "/" + os.environ.get("NOTES_ING_PATH")

    try:
        items = db.select_note_by_id(conn, None, False)
    except Exception as e:
        flash('Error generating notes: Check Logs')
        note.logger.error("Error Generating Notes: %s" % e)

    arr = []
    if len(items) > 0:
        for item in items:
            try:
                _id = item[0]
                _note = item[1]
                note_str = '%s | %s' % (_id, _note)
                arr.append(note_str)
            except Exception as e:
                note.logger.error(e)

    add_form = AddForm()
    delete_form = DeleteForm()
    admin_form = AdminForm()

    if add_form.validate_on_submit():
        try:
            result = add_note(add_form.note_field.data)

            if result[1] == 200:
                flash('Note "{}" has been added!'.format(
                    add_form.note_field.data))
            else:
                flash('Failed to add Note "{}": {}'.format(
                    add_form.note_field.data, "Check Logs"))
        except Exception as e:
            flash('Failed to add Note "{}": {}'.format(
                add_form.note_field.data, e))

        return redirect(ing_path)

    if delete_form.validate_on_submit():
        try:
            result = delete_note(delete_form.id_field.data)
            if result[1] == 204:
                flash('Note "#{}" has been Deleted!'.format(
                    delete_form.id_field.data))
            else:
                flash('Failed to delete Note "#{}": {}'.format(
                    delete_form.id_field.data, "Check Logs"))
        except Exception as e:
            flash('Failed to delete Note "#{}": {}'.format(
                delete_form.id_field.data, e))

        return redirect(ing_path)

    if admin_form.validate_on_submit():
        return redirect(ing_path + '/admin')
    
    return render_template('index.html',
                            notes=arr,
                            add_form=add_form,
                            delete_form=delete_form,
                            admin_form=admin_form,
                            gitlab_logo=logo)

@note.route('/admin', methods=['GET', 'POST'])
@auth.login_required
def admin(): 
    conn = db.create_connection() 
    ing_path = "/" + os.environ.get("NOTES_ING_PATH")

    items = []
    try:
        items = db.select_note_by_id(conn, None, True)
    except Exception as e:
        flash('Error generating notes: Check Logs')
        note.logger.error("Error generating notes: %s" % e)

    arr = []
    if len(items) > 0:
        for item in items:
            try:
                _id = item[0]
                _note = item[1]
                _ip_address = item[2]
                _hostname = item[3]

                note_str = '%s | %s | %s | %s' % (_id, _note, _ip_address, _hostname)
                arr.append(note_str)
            except Exception as e:
                note.logger.error(e)

    reset_form = ResetForm()
    if reset_form.validate_on_submit():
        try:
            result = reset()
            if result:
                flash('Database Table "{}" has been reset!'.format("notes"))
            else:
                flash('Database Table "{}" Failed to reset: Check Logs'.format("notes"))
        except Exception as e:
            flash('Database Table "{}" Failed to reset: {}}'.format("notes", e))
        
        return redirect(ing_path + '/admin')
    
    return render_template('admin.html',
                            notes=arr,
                            reset_form=reset_form)

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@note.route('/add', methods=['GET', 'POST'])
def add_note(msg=""):
    if not msg:
        data = request.get_json(force=True)
        msg = data.get('message')

    if not msg:
         return jsonify({"Error": "No message in Request"}), 400

    if len(msg) > 100:
         return jsonify({"Error": "Message too long, keep at chars or less"}), 400

    if (msg == "\""):
        response = jsonify({"Success": "Maybe a Security Issue!"}), 200
        response.headers.set('Content-Type', 'text/html')
        return response

    ip_address = "unknown"
    hostname = "unknown"

    try:
        if request.environ.get('HTTP_X_FORWARDED_FOR') is not None:
            ip_address = str(request.environ['HTTP_X_FORWARDED_FOR'])
            hostname = str(socket.gethostbyaddr(ip_address)[0])
        
    except Exception as e:
        note.logger.error("Error Getting Requester IP and Hostname: %s" % e)
        ip_address = "unknown"
        hostname = "unknown"

    conn = db.create_connection()
    try:
        note.logger.info("Attempting to add note with msg: {}, ipaddress: {}, hostname: {}".format(msg, ip_address, hostname))
        db.create_note(conn, msg, ip_address, hostname)
        return jsonify({"Success": "Note added!"}), 200
    except Exception as e:
        err = "%s" % e
        return jsonify({"Error": err}), 500

@note.route('/get', methods=['GET'])
def get_note():
    id = request.args.get('id')
    conn = db.create_connection()

    try:
        result = str(db.select_note_by_id(conn, id))
        return jsonify({"Note": result}), 200
    except Exception as e:
        note.logger.error("Error Getting Notes: %s" % e)
        return jsonify({"Error": e}), 500

@note.route('/delete', methods=['GET', 'DELETE'])
def delete_note(id=None):
    if not id:
        id = request.args.get('id')

    if not id:
        return jsonify({"Error": "No id sent in request!"}), 400

    conn = db.create_connection()
    try:
        db.delete_note(conn, id)
    except Exception as e:
        return jsonify({"Error": e}), 500

    return jsonify({"Success": "Note Deleted!"}), 204

def reset():
    conn = db.create_connection()
    sql_drop_notes_table = """DROP TABLE notes;"""
    
    try:
        db.drop_table(conn, sql_drop_notes_table)
    except Exception as e:
        note.logger.error("Failed to reset database table 'notes': %s" % e)
        return False

    conn = db.create_connection()
    try:
        sql_create_notes_table = note.config['CREATE_TABLE_QUERY']
        db.create_table(conn, sql_create_notes_table)
    except Exception as e:
        note.logger.error("Failed to re-create database table 'notes': %s" % e)
        return False

    return True