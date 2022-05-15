from flask import flash, render_template,redirect,url_for,request
from . import auth
from flask_login import login_user,login_user,logout_user,login_required
from .forms import LoginForm,RegisterForm
from .. import db
from ..email import mail_message
from ..models import User

@auth.route('/login' , methods = ["GET","POST"])
def login():
     login_form = LoginForm()
     if login_form.validate_on_submit():
        user = User.query.filter_by(username = login_form.username.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.all_pitches'))

        flash('Invalid username or Password')


     return render_template('auth/login.html', form = login_form)
    
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/register', methods = ["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        user.save_user()
    
        mail_message("Welcome to Pitch_whorl","email/welcome_user",user.email,user=user)
        
        return redirect(url_for('main.account',uname=user))

    return render_template('auth/sign_up.html', title = "Create an  Account", form = form)


