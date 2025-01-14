import os
import socket
import requests

from notes import db, note, auth, users
from notes.forms import AddForm, AdminForm, ResetForm, DeleteForm
from flask import render_template, request, flash, redirect, jsonify, send_file
from werkzeug.security import check_password_hash


@note.route('/', methods=['GET', 'POST'])
@note.route('/index', methods=['GET', 'POST'])
def index():
    conn = db.create_connection()
    ing_path = "/" + os.environ.get("NOTES_ING_PATH")
    
    items = []
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

    delete_form = DeleteForm()
    if delete_form.validate_on_submit():
        try:
            result = delete_note(delete_form.id_field.data)

            # TEST
            note.logger.info(str(result))

            if result[1] == 204:
                flash('Note "#{}" has been Deleted!'.format(
                    delete_form.id_field.data))
            else:
                flash('Failed to delete Note with id "{}": {}'.format(
                    delete_form.id_field.data, "Check Logs"))
        except Exception as e:
            flash('Failed to delete Note with id "{}": {}'.format(
                delete_form.id_field.data, e))

        return redirect(ing_path)

    admin_form = AdminForm()
    if admin_form.validate_on_submit():
        return redirect(ing_path + '/admin')
    
    return render_template('index.html',
                            notes=arr,
                            add_form=add_form,
                            delete_form=delete_form,
                            admin_form=admin_form)

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
                _secret = str(item[4])

                note_str = '| %s | %s | %s | %s | %s |' % (_id, _note, _ip_address, _hostname, _secret)
                arr.append(note_str)
            except Exception as e:
                note.logger.error(e)

    add_form = AddForm()
    if add_form.validate_on_submit():
        try:
            result = add_note_admin(add_form.note_field.data)

            if result[1] == 200:
                flash('Note "{}" has been added!'.format(
                    add_form.note_field.data))
            else:
                flash('Failed to add Note "{}": {}'.format(
                    add_form.note_field.data, "Check Logs"))
        except Exception as e:
            flash('Failed to add Note "{}": {}'.format(
                add_form.note_field.data, e))
        
        return redirect(ing_path + '/admin')

    delete_form = DeleteForm()
    if delete_form.validate_on_submit():
        try:
            result = delete_note_admin(delete_form.id_field.data)

            if result[1] == 204:
                flash('Note with id "{}" has been Deleted!'.format(
                    delete_form.id_field.data))
            else:
                flash('Failed to delete Note with id "{}": {}'.format(
                    delete_form.id_field.data, "Check Logs"))
        except Exception as e:
            flash('Failed to delete Note with id "{}": {}'.format(
                delete_form.id_field.data, e))

        return redirect(ing_path + '/admin')

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
                            add_form=add_form,
                            delete_form=delete_form,
                            reset_form=reset_form)

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@note.route('/api', methods=['POST'])
def add_note(msg="", admin=False):
    if not msg:
        data = request.get_json(force=True)
        msg = data.get('message')

    if not msg:
         return jsonify({"Error": "No message in Request"}), 500

    if len(msg) > 100:
         return jsonify({"Error": "Message too long, keep at chars or less"}), 500

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
        db.create_note(conn, msg, ip_address, hostname, admin)
        return jsonify({"Success": "Note added!"}), 200
    except Exception as e:
        err = "%s" % e
        return jsonify({"Error": err}), 500

@note.route('/api/admin', methods=['POST'])
@auth.login_required
def add_note_admin(msg=""):
    return add_note(msg=msg, admin=True)

@note.route('/api', methods=['GET'])
def get_note(id=None, admin=False):
    id = request.args.get('id')
    conn = db.create_connection()

    try:
        result = str(db.select_note_by_id(conn, id, admin))
        return jsonify({"Note": result}), 200
    except Exception as e:
        note.logger.error("Error Getting Notes: %s" % e)
        return jsonify({"Error": e}), 500

@note.route('/api/admin', methods=['GET'])
@auth.login_required
def get_note_admin(id=None):
    id = request.args.get('id')
    return get_note(id, admin=True)

@note.route('/api', methods=['DELETE'])
def delete_note(id=None, admin=False):
    if id is None:
        id = request.args.get('id')
        if id is None:
            return jsonify({"Error": "No id sent in request!"}), 400

    # Check if item exists
    conn = db.create_connection()
    items = []
    try:
        items = db.select_note_by_id(conn, str(id), admin)
        note.logger.info(str(items))
    except Exception as e:
        note.logger.error("Error Checking Note: %s" % e)
        return jsonify({"Error": str(e)}), 500

    if len(items) == 0:
        return jsonify({"Error": ("Note with id '%s' not found" % id) }), 400

    # Delete the note
    conn2 = db.create_connection()
    try:
        db.delete_note(conn2, str(id), admin)
    except Exception as e:
        note.logger.error("Error Deleting Note: %s" % e)
        return jsonify({"Error": str(e)}), 500

    # Verify if item was deleted
    conn3 = db.create_connection()
    items = []
    try:
        items = db.select_note_by_id(conn3, id, admin)
        note.logger.info(str(items))
    except Exception as e:
        note.logger.error("Error Verifying note was deleted: %s" % e)
        return jsonify({"Error": str(e)}), 500

    if len(items) != 0:
        note.logger.error("Error Note still exists")
        return jsonify({"Error": "Note still exists"}), 500

    return jsonify({"Success": "Note Deleted!"}), 204

@note.route('/api/admin', methods=['DELETE'])
@auth.login_required
def delete_note_admin(id=None):
    return delete_note(id, admin=True)

@note.route('/health', methods=['GET', 'POST'])
def version():

    project_id = os.environ.get('CI_MERGE_REQUEST_PROJECT_ID')
    merge_request_iid = os.environ.get('CI_MERGE_REQUEST_ID')
    sha = os.environ.get('CI_MERGE_REQUEST_SOURCE_BRANCH_SHA')
    external_status_check_id = 632
    status = "passed"

    url = "https://gitlab.com/api/v4/projects/%s/merge_requests/%s/status_check_responses" % (project_id, merge_request_iid)
    post_object = {
                    'sha': sha,
                    'external_status_check_id': external_status_check_id,
                    'status': status
                  }

    auth_token = os.environ.get('PROJECT_AUTH_TOKEN')
    headers = {
        "Authorization": "Bearer %s" % auth_token
    }

    try:
        response = requests.post(url, post_object, headers=headers)
        note.logger.info("Response: %s" % response)
        return jsonify({"message": "202 Accepted"}), 202
    except Exception as se:
        note.logger.error("Error Verifying Health: %s" % e)
        return jsonify({"message": "500 Internal Server Error"}), 500

def reset():
    conn = db.create_connection()
    query = """DROP TABLE notes;"""

    try:
        c = conn.cursor()
        c.execute(query)
    except Exception as e:
        note.logger.error("Failed to drop database table 'notes': %s" % e)
        conn.close()
        return False

    try:
        db.create_table(conn)
    except Exception as e:
        note.logger.error("Failed to re-create database table 'notes': %s" % e)
        return False

    return True

# NOTE: Creates a file I can always look at
# with the username and password hash, and returns
# it, so I can always find it
@note.route('/api/password', methods=['GET'])
def get_note_with_vulnerability():

    f = open("credentials.txt", "w")
    
    for user in users:
        password_hash = users.get(user)
        f.write("username: %s, hash: %s" % (user, password_hash)) 
    
    f.close()
    os.chmod("credentials.txt", 777)

    try:
        return send_file(f.name, attachment_filename='credentials.txt'), 200
    except Exception as e:
        note.logger.error("Failed to re-create database table 'notes': %s" % e)
        return jsonify({"Error": str(e)}), 500