from server.instance import server 

# Для удобного использования тестов импортирую все ресурсы в вакуум
from resources.item import *

if __name__ == "__main__":
    server.run()