from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel





class ItemResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be blank")

    def get(self, name):
        item = ItemModel.search_name(name)
        if item:
            return item.json(), 200
        return {'Error': "Item with that name not found"}, 404


    @jwt_required()
    def post(self, name):
        if ItemModel.search_name(name):
            return {'Error' : 'Item with name {} exists'.format(name)}, 400
        
        request_body = ItemResource.parser.parse_args()
        item = ItemModel(name, request_body['price'])
        item.insert()
        return item.json(), 201


    @jwt_required()
    def put(self, name):
        item = ItemModel.search_name(name)
        if item:      
            data = ItemResource.parser.parse_args()
            updated_item = ItemModel(name, data["price"])
            updated_item.update()

            return updated_item.json(), 202 
        return {"Error" : "Item with name {} not found".format(name)}, 404

    @jwt_required()
    def delete(self, name):
        item = ItemModel.search_name(name)
        if item:
            item.delete()
            return {"Message" : "Item deleted"}, 202

        return {"Error" : "Item with name {} not found".format(name)}, 404




class ItemCollectionResource(Resource):
    def get(self):
        return {'items' : list(map(lambda x: x.json(), ItemModel.get_all())) }, 200
 