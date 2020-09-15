from db import db 
from flask_sqlalchemy import backref

class User(db.Model):
    __tablename___ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    items = db.relationship("Item", secondary="stores")

class Item(db.Model):
    __tablename___="items"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))

    users = db.relationship("User", secondary="stores")


# Связующая модель
class Store(db.Model):
    __tablename___="stores"
    id= db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))


    user =  relationship(User, backref=backref("stores", cascade="all, delete-orphan"))
    item = relationship(Item, backref=backref("stores", cascade="all, delete-orphan"))