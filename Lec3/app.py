from flask import Flask , request
from flask_restful import Resource, Api , reqparse
# Из расширения flask-jwt достанем необходимый функционал
from flask_jwt import JWT, jwt_required, current_identity

from auth_conf import authenticate, identity


app = Flask(__name__)
app.secret_key = "MySuperDuperSecretKey"

api = Api(app)


jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)


items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be blank")

    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item:
            return {'item' : item}, 200
        return {'Error': "Item with that name not found"}, 404

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'Error' : 'Item with name {} exists'.format(name)}, 400
        
        request_body = Item.parser.parse_args()
        item = {'name' : name, 'price' : request_body['price']}
        items.append(item)
        return item, 201

    @jwt_required()
    def put(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item:      
            data = Item.parser.parse_args()
            item.update(data)
            return item, 202 
        return {"Error" : "Item with name {} not found".format(name)}, 404

    @jwt_required()
    def delete(self, name):
        global items 
        start_len = len(items)
        items =  list(filter(lambda x: x['name'] != name, items))
        if abs(len(items) - start_len) > 0:
            return {'Message' : 'Item deleted'}, 202
        return {'Error' : 'Item with that name not found'}, 404




class ItemCollection(Resource):
    def get(self):
        return {'items' : items }, 200
 


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemCollection, "/items") 



if __name__ == "__main__":
    app.run(port=8080, debug=True)
