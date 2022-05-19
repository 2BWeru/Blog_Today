from crypt import methods
from email.quoprimime import quote
from flask import render_template,abort ,request,redirect, session, url_for
from flask_login import login_required,current_user, user_accessed
<<<<<<< HEAD
from app.requests import get_quote
from .forms import UpdateProfile,PitchForm,CommentForm
=======

from app.requests import get_quote
from .forms import UpdateProfile,BlogForm,CommentForm
>>>>>>> 4bf4cab... create blog pdate function
from .. import db
from . import main
import markdown2  
from .. import db
from ..models import Blog, User,Comment


@main.route('/')
def entry():
<<<<<<< HEAD
    
=======
>>>>>>> 4bf4cab... create blog pdate function
    quote=get_quote()
    
    return render_template('entry.html', title = "Home page",quote=quote)


@main.route('/all_blogs', methods = ['GET'])
def all_blogs():
    blogs = Blog.query.all()
    self_love=Blog.query.filter_by(category = 'self_love').all() 
    hope=Blog.query.filter_by(category = 'hope').all() 
    mental_health=Blog.query.filter_by(category = 'mental_health').all() 
    work = Blog.query.filter_by(category = 'work').all() 
    music =Blog.query.filter_by(category = 'Music').all()
    
    return render_template('all_blogs.html', title = 'All_blogs',blogs=blogs, work=work,music=music,hope=hope,mental_health=mental_health,self_love=self_love)


@main.route('/user/<uname>', methods=["GET", "POST"])
@login_required
def account(uname):
    user = User.query.filter_by(username = uname).first()
    user_id = current_user._get_current_object().id
    posts = Blog.query.filter_by(user_id = user_id).all()
    

    if user is None:
            abort(404)
    
    return render_template('profile/account.html', title = 'My account', user=user,posts=posts)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.account',uname = current_user.username))

    return render_template('profile/update_profile.html',form =form)


@main.route('/new_blog' , methods = ["GET","POST"])
@login_required
def new_blog():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        title = blog_form.title.data
        post = blog_form.post.data
        category = blog_form.category.data
        new_blog_object = Blog(post = post, user_id= current_user.id,category = category,title = title)
        new_blog_object.save_b()
        return redirect(url_for('main.all_blogs'))

    return render_template("new_blog.html", title = "New_Blog", form = blog_form)


@main.route('/comment/<int:blog_id>' , methods = ['GET', 'POST'])
@login_required
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,blog_id = blog_id)
        new_comment.save_c()
        return redirect(url_for('main.comment', blog_id = blog_id))
    return render_template('comment.html', form =form, blog = blog,all_comments=all_comments)

@main.route("/blog/<int:id>/delete", methods=["POST"])
@login_required
def delete_comment(id):
    comment=Comment.get_comment(id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("main.comment", id=comment.id))

@main.route('/blog/<id>/update', methods=['GET', 'POST'])
@login_required
def update_blog(id):
    blog=Blog.get_blogs(id)
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        title = blog_form.title.data
        post = blog_form.post.data
        category = blog_form.category.data
        new_blog_object = Blog(post = post, user_id= current_user.id,category = category,title = title)
        new_blog_object.save_b()
        return redirect(url_for('main.all_blogs'))

    return render_template("new_blog.html", title = "New_Blog", form = blog_form,blog=blog)


@main.route("/blog/<int:id>/delete")
@login_required
def delete_blog():
    blog=Blog.get_blogs()
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for("main.index", blog_id=blog))
