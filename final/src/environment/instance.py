# Модуль для конфигов переменных окружения
import os 

# Ссоздаем объект окружения, по умолчанию - development
env = os.environ.get("PYTHON_ENV", "development")

# Все возможные окружения
all_envs = {
    "development" : {"port" : 8080, "debug" : True, "swagger-url" : "/api/swagger"},
    "production" : {"port" : 5000, "debug" : False, "swagger-url" : None},
}

enviroment_config = all_envs[env]


