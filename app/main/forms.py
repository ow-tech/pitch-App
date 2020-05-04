from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Length, Email, EqualTo, ValidationError
from app.models import User, Pitch


class Your_pitchForm(FlaskForm):

    category = StringField("Category")
    Your_pitch = TextAreaField('Your Pitch')
    post = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [Required(),Length(min=2, max=50)])
    email = StringField('Email', validators=[Required(),Email()])
    password = PasswordField('Password', validators=[Required()]) 
    confirm_password = PasswordField('Confirm Password', validators=[Required(), EqualTo('password')])

    submit = SubmitField('sign Up')  

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        # email = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Username already TAKEN. PLease Choose another')   

        def validate_email(self, email):
            email = User.query.filter_by(email = email.data).first()
            if email:
                raise ValidationError('Email already used. Use a different One')   

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required(),Length(min=2, max=50)])
    password = PasswordField('Password', validators=[Required()]) 
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')  

class PitchForm(FlaskForm):
    your_pitch = TextAreaField("Pitch", validators=[DataRequired()])
    submit = SubmitField('Post')
