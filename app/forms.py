from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired,Length,EqualTo
from flask_wtf import FlaskForm

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Password', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')