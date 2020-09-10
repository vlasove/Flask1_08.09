import sqlite3
from flask_restful import Resource, reqparse

# Модель пользователя
class User:
    #Внушний атрибут класса , указывающий на имя таблицы
    __tablename__ = 'users'

    def __init__(self, _id, username, password):
        self.id = _id 
        self.username = username
        self.password = password
    
    @classmethod
    def search_username(cls, username):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        select_query = "SELECT * FROM {} WHERE username=?".format(cls.__tablename__)
        sql_row = cur.execute(select_query, (username, )).fetchone() # (1, "Bob", "asp[daspd")

        if sql_row:
            user = cls(sql_row[0], sql_row[1], sql_row[2])
        else:
            user = None 

        conn.close()
        return user




    @classmethod
    def search_id(cls, _id) :
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        select_query = "SELECT * FROM {} WHERE id=?".format(cls.__tablename__)
        sql_row = cur.execute(select_query, (_id, )).fetchone() # [(1, "Bob", "asp[daspd")]

        if sql_row:
            user = cls(sql_row[0], sql_row[1], sql_row[2])
        else:
            user = None 

        conn.close()
        return user



# Пользовательский ресурс
class UserResource(Resource):
    __tablename__ = 'users'
    
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="Username field required!")
    parser.add_argument("password", type=str, required=True, help="Password field required!")

    def post(self):
        request_body = UserResource.parser.parse_args()

        if User.search_username(request_body["username"]):
            return {"Error" : "User with that username already exists!"}, 400

        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        insert_query = "INSERT INTO {} VALUES(NULL, ? ,?)".format(self.__tablename__) 
        cur.execute(insert_query, (request_body["username"], request_body["password"]))

        conn.commit()
        conn.close()

        return {"Message" : "User created"}, 201