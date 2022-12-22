from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegistrationForm(FlaskForm):
    username = StringField(label = "username")
    email = StringField(label = "email")
    password1 = PasswordField(label = "password1")
    password2 = PasswordField(label = "password2")
    submit = SubmitField(label = 'Create Account')
