from flask import redirect,render_template,url_for
from flask_bcrypt import bcrypt
from app.Authentication_form import LoginForm,RegisterForm
from . import main
from ..models import User
from app import db
# from flask_login import login_user,login_required,logout_user,current_user
# Views
# homepage
@main.route('/')
def index():

    
    return render_template('index.html', title = "Home page")



# login
@main.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
      users = User.query.filter_by(username = form.username.data).first()
      return redirect(url_for('main.profile'))

    return render_template('login.html', title = 'Log in', form=form)

# log out
@main.route('/log_out', methods=["GET","POST"])
# @login_required
def log_out():
    # logout_user
    return redirect (url_for('main.login'))


# Category
@main.route('/category')
def category():

    
    return render_template('category.html', title = 'Category')




# Register
@main.route('/sign_up ', methods=["GET","POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
       hashed_password = bcrypt.generate_passsword_hash(form.password.data)
       new_user = User(username = form.username.data,password = hashed_password)
       db.session.add(new_user)
       db.session.commit( )
       return redirect(url_for('main.login'))
        
    return render_template('sign_up.html', title = 'Register', form = form)


# Profile
@main.route('/profile', methods=["GET","POST"] )
# @login_required
def profile():
    
    
    return render_template('profile.html', title = 'Profile')



