from db import db 

class ItemModel(db.Model):
    __tablename__ = 'items'
    # Имена колонок должны совпадать с именами полей определяемыми в конструкторе
    id = db.Column(db.Integer, primary_key=True) # Вводим новое поле
    name = db.Column(db.String(50))
    price =  db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name 
        self.price = price 

    def json(self):
        return {"name" : self.name, "price" : self.price}

    @classmethod
    def search_name(cls, name):
        # name (слева) - имя колонки, name (справа) - аргумент метода search_name
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name price=price LIMIT 1" ->
        # conn = sqlite3.connect('data.db')
        # cur = conn.cursor()

        # select_query = 'SELECT * FROM {} WHERE name=?'.format(cls.__tablename__)
        # row = cur.execute(select_query, (name,)).fetchone()

        # conn.close()
        # if row:
        #     return  {'name' : row[0], 'price' : row[1]}

    @classmethod
    def get_all(cls):
        return cls.query.all() # SELECT * FROM items
        # conn = sqlite3.connect('data.db')
        # cur = conn.cursor()

        # select_query = "SELECT * FROM {}".format(cls.__tablename__)
        # items = []
        # for line in cur.execute(select_query):
        #     items.append({"name" : line[0], "price" : line[1]})
        
        # conn.close()
        # return items 


    def insert(self):
        db.session.add(self)
        db.session.commit()
        # conn = sqlite3.connect('data.db')
        # cur = conn.cursor()

        # insert_query = "INSERT INTO {} VALUES(?, ?)".format(self.__tablename__)
        # cur.execute(insert_query, (self.name, self.price))

        # conn.commit()
        # conn.close()

    def update(self):
        db.session.add(self)
        db.session.commit()
        # conn = sqlite3.connect('data.db')
        # cur = conn.cursor()

        # update_query = "UPDATE {} SET price=? WHERE name=?".format(self.__tablename__)
        # cur.execute(update_query, (self.price, self.name))

        # conn.commit()
        # conn.close()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        # conn = sqlite3.connect('data.db')
        # cur = conn.cursor()

        # delete_query = "DELETE FROM {} WHERE name=?".format(self.__tablename__)
        # cur.execute(delete_query, (self.name,))

        # conn.commit()
        # conn.close()
