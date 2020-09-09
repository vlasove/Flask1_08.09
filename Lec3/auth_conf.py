from user import User 
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'Alex', 'abcdefg'),
    User(2, 'Bob', 'qwerty')
]



user_names = {u.login : u for u in users}
user_id = {u.id : u for u in users }

# По login пытается найти пользователя в БД
# Если такой имеется, то сравнивается пароль из БД с паролем password
# В случае если все ОК - Возвращает этого пользователя
def authenticate(username, password):
    # Находим в БД пользователя с login
    user = user_names.get(username, None)
    # Проверяем что он не None и что его пароль (который в БД) совпадает с тем паролем, с которым он к нам пришел
    if user  and safe_str_cmp(user.password , password):
        return user 

# Возвращаем пользователя по id - отвечает за выдачу пропуска
def identity(payload):
    uid = payload['identity']
    return user_id.get(uid, None)