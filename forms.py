from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    remember = BooleanField("Remember me")
    submit = SubmitField("Submit")