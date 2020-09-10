from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3




class Item(Resource):
    __tablename__ = 'items'

    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be blank")

    @classmethod
    def search_name(cls, name):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        select_query = 'SELECT * FROM {} WHERE name=?'.format(cls.__tablename__)
        row = cur.execute(select_query, (name,)).fetchone()

        conn.close()
        if row:
            return  {'name' : row[0], 'price' : row[1]}




    def get(self, name):
        item = Item.search_name(name)
        if item:
            return {'item' : item}, 200
        return {'Error': "Item with that name not found"}, 404


    @jwt_required()
    def post(self, name):
        if Item.search_name(name):
            return {'Error' : 'Item with name {} exists'.format(name)}, 400
        
        request_body = Item.parser.parse_args()
        item = {'name' : name, 'price' : request_body['price']}
       

        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        insert_query = "INSERT INTO {} VALUES(?, ?)".format(self.__tablename__)
        cur.execute(insert_query, (item["name"], item["price"]))

        conn.commit()
        conn.close()


        return item, 201

    @jwt_required()
    def put(self, name):
        item = Item.search_name(name)
        if item:      
            data = Item.parser.parse_args()

            conn = sqlite3.connect('data.db')
            cur = conn.cursor()

            update_query = "UPDATE {} SET price=? WHERE name=?".format(self.__tablename__)
            cur.execute(update_query, (data['price'], name))

            conn.commit()
            conn.close()

            return {'name' : name, 'price' : data['price']}, 202 
        return {"Error" : "Item with name {} not found".format(name)}, 404

    @jwt_required()
    def delete(self, name):
        if Item.search_name(name):
            # Тогда его можно удалить
            conn = sqlite3.connect('data.db')
            cur = conn.cursor()

            delete_query = "DELETE FROM {} WHERE name=?".format(self.__tablename__)
            cur.execute(delete_query, (name,))

            conn.commit()
            conn.close()

            return {"Message" : "Item deleted"}, 202

        return {"Error" : "Item with name {} not found".format(name)}, 404




class ItemCollection(Resource):
    __tablename__ = 'items'
    def get(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        select_query = "SELECT * FROM {}".format(self.__tablename__)
        items = []
        for line in cur.execute(select_query):
            items.append({"name" : line[0], "price" : line[1]})
        
        conn.close()


        return {'items' : items }, 200
 