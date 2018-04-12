from flask_restful import reqparse, abort, Api, Resource
from main import api
from models import db, User, userSchema, Article, articleSchema
import json

def abort_article(article_id):
    dbarticle = Article.query.filter_by(article_id=article_id).first()
    if(dbarticle is None):
        abort(404, message="articles {} doesn't exist".format(article_id))

parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('subtitle', type=str)
parser.add_argument('description', type=str)
parser.add_argument('article_type', type=str)
parser.add_argument('content', type=str)
parser.add_argument('author', type=str)
parser.add_argument('status', type=str)

class article(Resource):
    def get(self, article_id):
        abort_article(article_id)
        dbarticle = Article.query.filter_by(article_id=article_id).first()
        return articleSchema.dump(dbarticle)

    def put(self, article_id):
        args = parser.parse_args()
        abort_article(article_id)
        dbarticle = Article.query.filter_by(article_id=article_id).first()
        title = args['title']
        subtitle = args['subtitle']
        description = args['description']
        article_type = args['article_type']
        content = args['content']
        author = args['author']
        status = args['status']
        dbarticle.title = title
        dbarticle.subtitle = subtitle
        dbarticle.description = description
        dbarticle.article_type = article_type
        dbarticle.article_text = content
        dbarticle.author = int(author)
        dbarticle.status = int(status)
        db.session.add(dbarticle)
        db.session.commit()
        return articleSchema.dump(dbarticle), 201

    def delete(self, article_id):
        abort_article(article_id)
        dbarticle = Article.query.filter_by(article_id=article_id).first()
        db.session.delete(dbarticle)
        db.session.commit()
        return ' ', 204

class articles(Resource):
    def get(self):
        dbarticles = Article.query.all()
        print(dbarticles)
        reqdata = []
        for item in dbarticles:
            reqdata.append(articleSchema.dump(item).data)

        return reqdata

    def post(self):
        args = parser.parse_args()
        title = args['title']
        subtitle = args['subtitle']
        description = args['description']
        article_type = args['article_type']
        content = args['content']
        author = args['author']

        dbarticle = Article(title, subtitle, description, article_type, content, int(author), 0)
        db.session.add(dbarticle)
        db.session.commit()
        return dbarticle.article_id,201


api.add_resource(articles, '/articles')
api.add_resource(article, '/articles/<article_id>')