from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
# from wtforms.validators import Required


class Your_pitchForm(FlaskForm):

    category = StringField("Category")
    Your_pitch = TextAreaField('Your Pitch')
    post = SubmitField('Submit')