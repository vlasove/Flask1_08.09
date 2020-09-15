from flask_restplus import fields 
from server.instance import server

# Аналогично парсеру из from flask_restful import reqparse
item = server.api.model(
    'Item', {
        'id' : fields.Integer(description='Unique id'),
        'title': fields.String(required=True, min_length=1, max_length=200, description="Item title") ,
    }
)

items_db = [
    {"id" : 0, "title" : "First Item"},
    {"id" : 1, "title" : "Flask Course Item"},
]


# Непосредственно работа с моделью данных на уровне хранилища
# class ItemModel(....):
#     __tablename__ ='items' 
#     ......