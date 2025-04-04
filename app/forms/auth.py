from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, Length, EqualTo

from app.models import User


class LoginForm(FlaskForm):
    user_identifier = StringField('Username or Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=25)])
    password_confirmation = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password',
                                                                                                  message='Passwords must match.')])
    submit = SubmitField('Register')

class ProfileForm(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last name")
    username = StringField("Username", [DataRequired(), Length(4, 255)])
    email = StringField("Email Address", [DataRequired(), Email()])
    submit = SubmitField("Save")
