from db import db 

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    # Поле для установки соотношения между таблицами
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, title):
        self.title = title 

    def json(self):
        return {'title' : self.title, 'items' : [item.json() for item in self.items.all()]}
        #list(map(lambda x: x.json(), self.items.all()))

    @classmethod 
    def store_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod 
    def all_stores(cls):
        return cls.query.all()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.add(self)
        db.session.commit()