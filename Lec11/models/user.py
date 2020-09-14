from db import db 

# Модель пользователя
class UserModel(db.Model):
    #Внутренний атрибут класса , указывающий на имя таблицы
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True) # Вводим новое поле
    username = db.Column(db.String(50))
    password =  db.Column(db.String(50))

    def __init__(self, _id, username, password):
        self.id = _id 
        self.username = username
        self.password = password


    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def search_username(cls, username):
        return cls.query.filter_by(username=username).first()


    @classmethod
    def search_id(cls, _id) :
        return cls.query.filter_by(id= _id)

