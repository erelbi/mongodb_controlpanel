# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SelectField
from wtforms.validators import InputRequired, Email, DataRequired


## login and registration

class LoginForm(FlaskForm):
    username = TextField('Username', id='username_login', validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login', validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = TextField('Username', id='username_create', validators=[DataRequired()])
    email = TextField('Email', id='email_create', validators=[DataRequired(), Email()])
    password = PasswordField('Password', id='pwd_create', validators=[DataRequired()])


class MongoDBCreateUSer(FlaskForm):
    username = TextField('Username', id='username', validators=[DataRequired()])
    password = PasswordField('Password', id='pwd', validators=[DataRequired()])
    roles = SelectField('Roles', id='roles', choices=[('dbAdmin','DBadmin'),('dbOwner','DBowner'),('readWrite','readWrite')], validators=[DataRequired()])
