import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel



# Пользовательский ресурс
class UserResource(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="Username field required!")
    parser.add_argument("password", type=str, required=True, help="Password field required!")

    def post(self):
        request_body = UserResource.parser.parse_args()

        if UserModel.search_username(request_body["username"]):
            return {"Error" : "User with that username already exists!"}, 400

        user = UserModel(None, request_body["username"], request_body["password"])
        user.insert()

        return {"Message" : "User created"}, 201