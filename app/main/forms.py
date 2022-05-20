from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField,SelectField,BooleanField
from wtforms.validators import InputRequired,Email,EqualTo
from wtforms import ValidationError
from ..models import User

class UpdateProfile(FlaskForm):
    bio = TextAreaField(render_kw={'placeholder':'Tell us about you.'},validators = [InputRequired()])
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):
    title = StringField(validators=[InputRequired()],render_kw={"placeholder":"Title"})
    category = SelectField(choices=[('Music','Music'),('self_love','self_love'),('mental_health','mental_health'),('work','work')],validators=[InputRequired()])
    post = TextAreaField(validators=[InputRequired()],render_kw={"placeholder":"Your pitch"})
    submit = SubmitField('Pitch')
   

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[InputRequired()],render_kw={"placeholder":"Comment"})
    submit = SubmitField('Comment')

#.....
class ReviewForm(FlaskForm):
    title = StringField('Review title',validators=[InputRequired()], render_kw={"placeholder":"title"})
    review = TextAreaField('Movie review')
    submit = SubmitField('Submit')