from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,BooleanField
from wtforms.validators import InputRequired,Email,EqualTo
from wtforms import ValidationError
from ..models import User

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')