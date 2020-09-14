from flask_restful import Resource
from models.store import StoreModel
from flask_jwt import jwt_required

# /store/<string:title>
class StoreResource(Resource):
    @jwt_required()
    def get(self, title):
        store = StoreModel.store_by_title(title)
        if store:
            return store.json()
        return {"Error" : "Store with that title not found"}, 404 

    @jwt_required()
    def post(self, title):
        if StoreModel.store_by_title(title):
            return {"Error" : "Store with that title already exists"}, 400 

        store = StoreModel(title)
        store.insert()

        return store.json(), 201

    @jwt_required()
    def delete(self, title):
        store = StoreModel.store_by_title(title)
        if store:
            store.delete()
            return {"Message" : "Store deleted"}, 202

        return {"Error" : "Store with title {} not found".format(title)}, 404



# /stores
class StoreCollectionResource(Resource):
    @jwt_required()
    def get(self):
        return {"stores" : list(map(lambda x: x.json(), StoreModel.all_stores()))}, 200

