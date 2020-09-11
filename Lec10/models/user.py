import sqlite3

# Модель пользователя
class UserModel:
    #Внушний атрибут класса , указывающий на имя таблицы
    __tablename__ = 'users'

    def __init__(self, _id, username, password):
        self.id = _id 
        self.username = username
        self.password = password


    def insert(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        insert_query = "INSERT INTO {} VALUES(NULL, ? ,?)".format(self.__tablename__) 
        cur.execute(insert_query, (self.username, self.password))

        conn.commit()
        conn.close()
    
    @classmethod
    def search_username(cls, username):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        select_query = "SELECT * FROM {} WHERE username=?".format(cls.__tablename__)
        sql_row = cur.execute(select_query, (username, )).fetchone() # (1, "Bob", "asp[daspd")

        if sql_row:
            user = cls(sql_row[0], sql_row[1], sql_row[2])
        else:
            user = None 

        conn.close()
        return user




    @classmethod
    def search_id(cls, _id) :
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        select_query = "SELECT * FROM {} WHERE id=?".format(cls.__tablename__)
        sql_row = cur.execute(select_query, (_id, )).fetchone() # [(1, "Bob", "asp[daspd")]

        if sql_row:
            user = cls(sql_row[0], sql_row[1], sql_row[2])
        else:
            user = None 

        conn.close()
        return user

