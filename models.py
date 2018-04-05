from manage import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True)
    email = db.Column(db.String(120),unique=True)
    password = db.Column(db.String(120))

    #def __init__(self,username,email):
    #    self.username = username
    #    self.email = email

    def __repr__(self):
        return "<Model User `{}`".format(self.username)