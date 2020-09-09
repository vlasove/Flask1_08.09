
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

from flask import Flask 
from flask_restful import Resource, Api 

# Общая конфигурация приложения Flask
app = Flask(__name__)
# Подключение функционала RESTful API
api = Api(app)



# Локальная БД
items = []

# Ресурс Item /item/<string:name>
class Item(Resource):
    pass 

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
