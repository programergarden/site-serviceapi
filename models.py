from main import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields, pprint

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Integer, default=0)

    def __init__(self, username, email, password, status):
        self.username = username
        self.email = email
        self.password = password
        self.status = status

    def __repr__(self):
        return "<Model User `{}`".format(self.id)


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    email = fields.String()
    password = fields.String()
    create_at = fields.DateTime()
    status = fields.Integer()

userSchema = UserSchema()
