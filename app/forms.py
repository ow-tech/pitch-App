from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import Required, Length, Email, EqualTo


class Your_pitchForm(FlaskForm):

    category = StringField("Category")
    Your_pitch = TextAreaField('Your Pitch')
    post = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    username = StringField('Username' validators=[Required(),Length(min=2, max=50)])
    email = StringField('Email', validators=[Required(),Email()])
    password = PasswordField('Password', validators=[Required()]) 
    confirm_password = PasswordField('Confirm Password', validators=[Required(), EqualTo('password')])

    submit = SubmitField('sign Up')     
