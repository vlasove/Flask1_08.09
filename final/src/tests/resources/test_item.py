from resources.item import *

# Функции, которые будут запускаться тестовым фреймворком pytest
# Должны начинаться с префикса test_
# @pytest.fixture -> client


# {"id" : 0, "title" : "First Item"},
#     {"id" : 1, "title" : "Flask Course Item"},
def test_get_item_id(client):
    request =  '/item/0'
    response = client.get(request)

    # Начинаем сценарий для тестов
    assert response.status_code == 200
    assert response.json == {
        "id" : 0,
        "title" : "First Item",
    }


def test_get_item_with_wrong_id(client):
    request = '/item/10'
    response = client.get(request)

    assert response.status_code == 404