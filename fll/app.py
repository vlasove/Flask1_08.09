from flask import Flask
from flask_restplus import Api, fields, Resource
import os

app = Flask(__name__)
api = Api(app, version='1.0', title="Item MVC REST API", description="Simple Item managment API", prefix=os.environ.get("PREFIX"))

## namespace
ns = api.namespace('items', description='Item operations')

## model description and req parse
item = api.model('Item', {
    'id' : fields.Integer(readonly=True, description="Item unique identifier"),
    'name' : fields.String(required=True, description='The item name'),
    'price' : fields.Float(required=True, description='The item price in USD'),
    'amount' : fields.Integer(required=True, description='The item amount'),
})

## model class
class ItemModel(object):
    def __init__(self):
        self.counter = 0
        self.items = []

    def get(self, _id):
        for item in self.items:
            if item["id"] == _id:
                return item
        api.abort(404, f"Item {id} does not exists")

    def create(self, data):
        item = data 
        item["id"] = self.counter = self.counter + 1
        self.items.append(item)
        return item

    def update(self, _id, data):
        item = self.get(_id)
        item.update(data)
        return item

    def delete(self, _id):
        item = self.get(_id)
        self.items.remove(item)

## DataBase
DB = ItemModel()
DB.create({"name" : "chair" , "price" : 12.55, "amount" : 13})
DB.create({"name" : "table", "price" : 124.12, "amount" : 10})





## resourse for Items
@ns.route('/')
class ItemList(Resource):
    """
    Shows a list of all items and lets you POST to add new items
    """
    @ns.doc("list_items")
    @ns.marshal_list_with(item)
    def get(self):
        """
        List all items
        """
        return DB.items
    @ns.doc("create_item")
    @ns.expect(item)
    @ns.marshal_with(item, code=201)
    def post(self):
        """
        Create new item
        """
        return DB.create(api.payload), 201

## resource for Item
@ns.route('/<int:id>')
@ns.response(404, 'Item not found')
@ns.param('id' , 'The item identifier')
class Item(Resource):
    """
    Show a single item and lets you delete or update it
    """
    @ns.doc('get_item')
    @ns.marshal_with(item)
    def get(self, _id):
        """
        Fetch a given item
        """
        return DB.get(_id)

    @ns.doc("delete_item")
    @ns.response(204, 'Item deleted')
    def delete(self, _id):
        """
        Delete item with id
        """
        DB.delete(_id)
        return {"Message" : "Successfully deleted"}, 204

    @ns.doc('update_item')
    @ns.response(202, "Item updated")
    @ns.expect(item)
    @ns.marshal_with(item)
    def put(self, _id):
        """
        Update a given item by id
        """
        return DB.update(_id, api.payload), 202

if __name__ == '__main__':
    app.run(port=os.environ.get("PORT"), debug=os.environ.get("DEBUG"))