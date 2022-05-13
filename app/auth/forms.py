from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import InputRequired,Email,EqualTo,length
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    username = StringField(validators={InputRequired(),length(min=4,
         max=20)},render_kw={"placeholder":"username"})
    
    password = PasswordField('Password',validators = [InputRequired()]
        ,render_kw={"placeholder":"Password"})

    remember = BooleanField(render_kw={'pacehlder','Remember me'})

    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField(validators={InputRequired(),length(min=4,
         max=20)},render_kw={"placeholder":"username"})

    email = StringField(validators=[InputRequired(),Email()],render_kw={"placeholder":"email"})

    password = PasswordField(validators = {InputRequired()
       },render_kw={"placeholder":"Password"})


    submit = SubmitField("Register")

    
def validate_email(data_field):
    if User.query.filter_by(email =data_field.data).first():
        raise ValidationError('There is an account with that email')

def validate_username(data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

