from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import InputRequired,length,ValidationError,Email,EqualTo
from .models import User


class RegisterForm(FlaskForm):
      username = StringField(validators={InputRequired(),length(min=4,
         max=20)},render_kw={"placeholder":"username"})

      # email = StringField(validators=[InputRequired(),Email()],render_kw={"placeholder":"email"})

      password = PasswordField('Password',validators = [InputRequired(),
        EqualTo('password_confirm',message = 'Passwords must match')],render_kw={"placeholder":"Password"})
    
      submit = SubmitField("Register")

# shows whether the username already exist
      def validate_username(self,user):
            existing_user_username = User.query.filter_by(
                  username = user).first()

            if existing_user_username:
                  raise ValidationError(
                   "This username already exists.Please choose a different one."
                        )

# log in form
class LoginForm(FlaskForm):
      username = StringField(validators={InputRequired(),length(min=4,
         max=20)},render_kw={"placeholder":"username"})

      # email = StringField(validators={InputRequired(),length(min=4,
      #    max=20)},render_kw={"placeholder":"email"})
      
      password = PasswordField(validators={InputRequired(),length(min=4,
         max=20)},render_kw={"placeholder":"Password"})

      
      
      submit = SubmitField("Login")

# shows whether the username already exist
      def validate_email(seld,email):
            existing_user_email = User.query.filter_by(
                  email = email.date).first()
                  
            if existing_user_email:
                  raise ValidationError(
                   "This email already exists.Please choose a different one."
                        )

