from crypt import methods
from flask import render_template,abort ,request,redirect, session, url_for
from flask_login import login_required,current_user, user_accessed
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db
from . import main
import markdown2  
from .. import db
from ..models import Pitch, User,Comment,Upvote,Downvote


@main.route('/')
def index():
    pitches = Pitch.query.all()
    job = Pitch.query.filter_by(category = 'Job').all() 
    music = Pitch.query.filter_by(category = 'Music').all()
   
    
    return render_template('index.html', title = "Home page", pitches=pitches, job=job,music=music)


@main.route('/all_pitches', methods = ['GET'])
def all_pitches():
    pitches = Pitch.query.all()
    job = Pitch.query.filter_by(category = 'Job').all() 
    music = Pitch.query.filter_by(category = 'Music').all()
    
    return render_template('all_pitches.html', title = 'All_pitches',pitches=pitches, job=job,music=music)


@main.route('/user/<uname>', methods=["GET", "POST"])
@login_required
def account(uname):
    user = User.query.filter_by(username = uname).first()
    user_id = current_user._get_current_object().id
    posts = Pitch.query.filter_by(user_id = user_id).all()
    

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


@main.route('/new_pitch' , methods = ["GET","POST"])
@login_required
def new_pitch():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        post = pitch_form.post.data
        category = pitch_form.category.data
        new_pitch_object = Pitch(post = post, user_id= current_user.id,category = category,title = title)
        new_pitch_object.save_pitch()
        return redirect(url_for('main.all_pitches'))

    return render_template("new_pitch.html", title = "New_pitch", form = pitch_form)


@main.route('/comment/<int:pitch_id>' , methods = ['GET', 'POST'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_c()
        return redirect(url_for('main.comment', pitch_id = pitch_id))
    return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)

@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def like(id):
    get_pitches = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.all_pitches',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, pitch_id=id)
    new_vote.save()
    return redirect(url_for('main.all_pitches',id=id))

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def dislike(id):
    pitch = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for p in pitch:
        to_str = f'{p}'
        print(valid_string + " " + to_str)
        if valid_string == to_str:
            return redirect(url_for('main.all_pitches',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, pitch_id=id)
    new_downvote.save()
    return redirect(url_for('main.all_pitches',id = id))
