import email
from . import db

# profile class
# class Profile:
#       def __init__(self,id,name,email,image):
#        self.id = id
#        self.name = name 
#        self.email = email
#        self.image = image


class User(db.Model):
  __tablename__= 'users'
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255))

  def __repr__(self):
        return f'User {self.username}'