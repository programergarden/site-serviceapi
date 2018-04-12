from flask_restful import reqparse, abort, Api, Resource
from main import api
from models import db, User, userSchema

def abort_user(user_id):
    dbuser = User.query.filter_by(id=user_id).first()
    if(dbuser is None):
        abort(404, message="Users {} doesn't exist".format(user_id))

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('email', type=str)
parser.add_argument('password', type=str)
parser.add_argument('status', type=str)

class user(Resource):
    def get(self, user_id):
        abort_user(user_id)
        dbuser = User.query.filter_by(id=user_id).first()
        return userSchema.dump(dbuser)

    def put(self, user_id):
        args = parser.parse_args()
        abort_user(user_id)
        dbuser = User.query.filter_by(id=user_id).first()
        username = args['username']
        email = args['email']
        password = args['password']
        status = args['status']
        dbuser.username = username
        dbuser.email = email
        dbuser.password = password
        dbuser.status = int(status)
        db.session.add(dbuser)
        db.session.commit()
        return userSchema.dump(dbuser), 201

    def delete(self, user_id):
        abort_user(user_id)
        dbuser = User.query.filter_by(id=user_id).first()
        db.session.delete(dbuser)
        db.session.commit()
        return ' ', 204

class users(Resource):
    def get(self):
        dbusers = User.query.all()
        reqdata = []
        for item in dbusers:
            reqdata.append(userSchema.dump(item).data)

        return reqdata

    def post(self):
        args = parser.parse_args()
        username = args['username']
        email = args['email']
        password = args['password']
        dbuser = User(username, email, password)
        db.session.add(dbuser)
        db.session.commit()
        return dbuser.id,201


api.add_resource(users, '/users')
api.add_resource(user, '/users/<user_id>')