from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
       return User.query.get(int(user_id))


class User(db.Model,UserMixin):
  __tablename__= 'users'
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255),unique = True)
  email = db.Column(db.String(255),unique = True,index = True)
  password_hash = db.Column(db.String(255))
  pass_secure = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String(255))
  address= db.Column(db.String(255))
  Age = db.Column(db.String(255))
  Dateofbirth=db.Column(db.String(255))
  blog = db.relationship('Blog', backref='user', lazy='dynamic')
  comment = db.relationship('Comment', backref='user', lazy='dynamic')

  def save_user(self):
        db.session.add(self)
        db.session.commit()
  def delete(self):
        db.session.delete(self)
        db.session.commit()


  @property
  def password(self):
      raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
      self.pass_secure = generate_password_hash(password)


  def verify_password(self,password):
      return check_password_hash(self.pass_secure,password)



def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    post = db.Column(db.Text(), nullable = False)
    comment = db.relationship('Comment',backref='blog',lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    time = db.Column(db.DateTime, default = datetime.utcnow)
    category = db.Column(db.String(255), index = True,nullable = False)
    
    def save_b(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls,id):
        blogs = Blog.query.filter_by(id).all()
        return blogs

        
    def __repr__(self):
        return f'Blog {self.post}'

# comments
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'),nullable = False)

    def save_c(self):
        db.session.add(self)
        db.session.commit()

    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,blog_id):
        comments = Comment.query.filter_by(blog_id=blog_id).all()

        return comments



class Quotes:
    def __init__(self, author, quote):
        self.author=author
        self.quote=quote


 