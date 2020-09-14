from flask import Flask , request
from flask_restful import Resource, Api , reqparse
from flask_jwt import JWT, jwt_required, current_identity
from resources.user import UserResource
from resources.item import ItemResource , ItemCollectionResource
from secure.auth_conf import authenticate, identity
# from db import db # если отсавить это здесь - проблема циклического импорта


app = Flask(__name__)

app.secret_key = "MySuperDuperSecretKey"
api = Api(app)
jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)

# Подключение к БД + запрет на выброс информации про модификации таблиц при помощи ORM
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 



api.add_resource(ItemResource, "/item/<string:name>")
api.add_resource(ItemCollectionResource, "/items") 
api.add_resource(UserResource, "/register")



if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=8080, debug=True)



