import sqlite3 

# Подключение к БД
conn = sqlite3.connect('data.db')
# Интуерфейс СУБД
cur = conn.cursor()

# Первая SQL команда
create_table = 'CREATE TABLE IF NOT EXISTS users (id INTEGER, login TEXT, password TEXT)'
# Выполним первый запрос
cur.execute(create_table)



# Второй запрос - создание нового юзера
insert_query = 'INSERT INTO users VALUES(?, ?, ?)'
user = [1, "Alex", "qwerty"]
cur.execute(insert_query, (user[0], user[1], user[2]))
conn.commit()


# Третий запрос - получить все строки из таблицы
select_query = "SELECT * FROM users"
for row in cur.execute(select_query):
    print(row)


"UPDATE users SET password=200 WHERE login=Alex"
