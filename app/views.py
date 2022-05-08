from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html', title = "Home page")

@app.route('/login')
def login():

    
    return render_template('login.html', title = 'Login')


@app.route('/category')
def category():

    
    return render_template('category.html', title = 'Category')


@app.route('/sign_up')
def sign_up():

    
    return render_template('sign_up.html', title = 'Registration')




