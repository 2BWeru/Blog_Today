from . import db
# from flask_login import UserMixin


class User(db.Model):
  __tablename__= 'users'
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255))
  password = db.Column(db.String(80))
  pass_secure = db.Column(db.String(255))

#   def save_u(self):
#         db.session.add(self)
#         db.session.commit()

#   def delete(self):
#         db.session.delete(self)
#         db.session.commit()


def __repr__(self):
        return f'User {self.username}'


  



