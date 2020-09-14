from db import db 

class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(50))
    price =  db.Column(db.Float(precision=2))

    # Сообщаем модели ItemModel что она теперь состоит в соотношениях с моделью StoreModel
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
    #############################################################

    def __init__(self, name, price, store_id):
        self.name = name 
        self.price = price 
        self.store_id = store_id

    def json(self):
        return {"name" : self.name, "price" : self.price}

    @classmethod
    def search_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name price=price LIMIT 1" ->


    @classmethod
    def get_all(cls):
        return cls.query.all() # SELECT * FROM items

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
