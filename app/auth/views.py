from flask import redirect,render_template,url_for
from . import auth
from app.Authentication_form import LoginForm,RegisterForm
from ..models import User
from app import db



# Register
@auth.route('/sign_up ', methods=["GET","POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
    #    hashed_password = bcrypt.generate_passsword_hash(form.password.data)
       new_user = User(username = form.username.data,password = form.password.data)
       db.session.add(new_user)
       db.session.commit( )
       return redirect(url_for('main.profile'))
        
    return render_template('auth/sign_up.html', title = 'Register', form = form)


# login
@auth.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
      users = User.query.filter_by(username = form.username.data).first()
      return redirect(url_for('main.profile'))

    return render_template('auth/login.html', title = 'Log in', form=form)


# log out
@auth.route('/log_out', methods=["GET","POST"])
# @login_required
def log_out():
    # logout_user
    return redirect (url_for('auth.login'))

