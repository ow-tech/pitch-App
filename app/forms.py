from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class Your_pitchForm(FlaskForm):

    title = StringField("Cartegory", validators=[Required])
    Your_pitch = TextAreaField('Your Pitch', validators=[Required])
    post = SubmitField('Submit')