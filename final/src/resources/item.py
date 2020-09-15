from flask import Flask 
from flask_restplus import Api, Resource 

from server.instance import server 
from models.item import item, items_db 


app, api = server.app, server.api

@api.route('/items')
class ItemCollectionResource(Resource):
    # Проверка всех полей и marshal в json всех
    # Элементов списка
    @api.marshal_list_with(item)
    def get(self):
        """
        This method should return all items in DB 
        """
        return items_db , 200


@api.route('/item/<int:id>')
class ItemResource(Resource):
    # Из-за того, что нет класса ItemModel, функция для проверки вхождения реализуется здесь
    def find_by_id(self, id):
        return next((item for item in items_db if item["id"] == id), None)

    @api.marshal_with(item)
    def get(self, id):
        """
        This method should return concrete item with that id
        """
        current_item = self.find_by_id(id)
        if current_item:
            return current_item, 200
        return "Not found item with that name", 404 

    @api.marshal_with(item)
    def delete(self, id):
        """
        This method should delete item from db
        """
        global items_db 
        current_item = self.find_by_id(id)
        if current_item:
            items_db = list(filter(lambda x: x["id"] != id, items_db))
        return current_item, 202

    @api.expect(item , validate=True)
    @api.marshal_with(item)
    def post(self, id):
        # В случаае если хочется править id у новых объектов через автоинкремент
        if len(items_db) > 0:
            # Это значит что в БД уже что-то есть
            api.payload["id"] = items_db[-1]["id"] + 1
        else:
                # Это значит что БД == []
            api.payload["id"] =  0 
        #api.payload["id"] = items_db[-1]["id"] + 1 if len(items_db) > 0 else 0 

        items_db.append(api.payload)
        return api.payload, 201

    @api.expect(item , validate=True)
    @api.marshal_with(item)
    def put(self, id):
        current_item = self.find_by_id(id)
        if current_item:
            current_item.update(api.payload) 
            current_item["id"] = id
            return current_item, 202
        return "Not found item with that id", 404