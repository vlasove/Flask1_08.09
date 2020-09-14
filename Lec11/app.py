from flask import Flask , request
from flask_restful import Resource, Api , reqparse
from flask_jwt import JWT, jwt_required, current_identity
from resources.user import UserResource
from resources.item import ItemResource , ItemCollectionResource
from resources.store import StoreResource, StoreCollectionResource
from secure.auth_conf import authenticate, identity



app = Flask(__name__)

app.secret_key = "MySuperDuperSecretKey"
api = Api(app)
jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)

# Подключение к БД + запрет на выброс информации про модификации таблиц при помощи ORM
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

# Данная функция будет запущена и выполнена перед самым первым запросом
@app.before_first_request
def creator():
    db.create_all() # Подцепит все схемы, ссылающиеся на db и сгенерирует все необходимые таблицы



api.add_resource(ItemResource, "/item/<string:name>")
api.add_resource(ItemCollectionResource, "/items") 
api.add_resource(UserResource, "/register")
api.add_resource(StoreResource, "/store/<string:title>")
api.add_resource(StoreCollectionResource, "/stores")



if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=8080, debug=True)



