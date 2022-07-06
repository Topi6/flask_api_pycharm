import sqlite3
from flask_restful import Resource, reqparse

from models.user import UserModel

class Userregister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Do give a username pls")
    parser.add_argument('password', type=str, required=True, help="Gonna need a password")
    def post(self):
        data = Userregister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "User with that name already exists."},400
        else:
            user = UserModel(data['username'],data['password'])
            user.save_to_db()
            return {"message":"User created"}, 201