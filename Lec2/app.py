
# РЕСУРС /ITEMS
# GET /items - возвращает информацию про все товары в магазине


# РЕСУРС /ITEM/<STRING:NAME> 
# GET /item/<string:name> - возвращает информацию про товар с именем name
# POST /item/<string:name> - добавляет информацию про товар с именем name (поле price берем из json)
# PUT /item/<string:name> - обновляем информацию про товар с именем name 
# DELETE /item/<string:name> - удаляем информацию про товар с именем name 


# СТРУКТУРА ТОВАРА
# {
#     "name" : "Item Name",
#     "price" : 14.99
# }

from flask import Flask , request
from flask_restful import Resource, Api , reqparse

# Общая конфигурация приложения Flask
app = Flask(__name__)
# Подключение функционала RESTful API
api = Api(app)



# Локальная БД
items = []

# Ресурс Item /item/<string:name>
class Item(Resource):
    # Инициализируем парсер тел запросов
    parser = reqparse.RequestParser()
    # Добавляем первый аргумент для проверки
    parser.add_argument('price', type=float, required=True, help="This field cannot be blank")

    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item:
            return {'item' : item}, 200
        return {'Error': "Item with that name not found"}, 404

    def post(self, name):
        # Проверим, что товара с именем name еще нет в БД
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'Error' : 'Item with name {} exists'.format(name)}, 400
        # Получаем тело запроса
        request_body = Item.parser.parse_args()
        item = {'name' : name, 'price' : request_body['price']}
        items.append(item)
        return item, 201

    def put(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item:
            # Обновляем его 
            data = Item.parser.parse_args()
            item.update(data)
            return item, 202 
        return {"Error" : "Item with name {} not found".format(name)}, 404


    def delete(self, name):
        global items 
        start_len = len(items)
        items =  list(filter(lambda x: x['name'] != name, items))
        if abs(len(items) - start_len) > 0:
            return {'Message' : 'Item deleted'}, 202
        return {'Error' : 'Item with that name not found'}, 404



# Ресурс Items /items
class ItemCollection(Resource):
    # теперь не нужно использовать @app.route(......)
    # нужно лишь определять методы с названиями HTTP запросов
    # важная вещь - имя метода С МАЛЕНЬКОЙ БУКВЫ
    def get(self):
        # jsonify() больше не нужен, он применяется автоматически flask_restful
        return {'items' : items }, 200
 

# Добавим ресурс в api
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemCollection, "/items")



if __name__ == "__main__":
    app.run(port=8080, debug=True)
