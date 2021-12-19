from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    note_field = StringField('Enter Note', validators=[DataRequired()])
    add = SubmitField('Add')

class DeleteForm(FlaskForm):
    id_field = StringField('Enter Id', validators=[DataRequired()])
    delete = SubmitField('Delete')

class AdminForm(FlaskForm):
    username_field = StringField('Username', validators=[DataRequired()])
    password_field = StringField('Password', validators=[DataRequired()])
    login = SubmitField('Login')