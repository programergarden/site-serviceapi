from main import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from marshmallow import Schema, fields

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Integer, default=0)
    authors = db.relationship('Article', backref='user')
    def __init__(self, username, email, password, status):
        self.username = username
        self.email = email
        self.password = password
        self.status = status

    def __repr__(self):
        return "Model User `{}`".format(self.id)


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    email = fields.String()
    password = fields.String()
    create_at = fields.DateTime()
    status = fields.Integer()

userSchema = UserSchema()

class Article(db.Model):
    __tablename__ = 'articles'
    article_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    subtitle = db.Column(db.String(200))
    description = db.Column(db.String(500))
    article_type = db.Column(db.String(50), nullable=True)
    content = db.Column(db.Text(), nullable=True)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    create_at = db.Column(db.DateTime(), default=datetime.utcnow)
    status = db.Column(db.Integer, default=0)

    def __init__(self, title, subtitle, description, article_type, content, author, status):
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.article_type = article_type
        self.article_text = content
        self.author = author
        self.status = status

    def __repr__(self):
        return "Model article `{}`".format(self.article_id)


class ArticleSchema(Schema):
    article_id = fields.Integer()
    title = fields.String()
    subtitle = fields.String()
    description = fields.String()
    article_type = fields.String()
    content = fields.String()
    author = fields.Method('get_author')
    create_at = fields.DateTime()
    status = fields.Integer()

    def get_author(self, obj):
        dataUser = User.query.filter_by(id=obj.author).first()
        if(dataUser is None):
            return '{}'
        else:
            return userSchema.dump(dataUser).data


articleSchema = ArticleSchema()