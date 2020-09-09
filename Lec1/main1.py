from flask import Flask , jsonify, request

# Сущность приложения
app = Flask(__name__)

# Локальная БД
stores_info = [
    {
        'name' : 'First_Store',
        'items' : [
            {
                'name' : 'First Item',
                'price' : 10.99
            }
        ] 
    }
]

# GET /stores - отдаем информацию про все магазины какие у нас только есть
@app.route('/stores', methods=['GET'])
def get_stores():
    return jsonify({'stores' : stores_info}), 200


# POST /store + data.json{name:} - создаем новый магазин (с именем name) с пустым списком товаров
@app.route('/store', methods=['POST'])
def create_store():
    # Получаем все что лежит в теле запроса и перекладываем в dict()
    request_data = request.get_json()
    # создаем нвоый магазин
    new_store = {
        'name' : request_data['name'],
        'items' : []
    }
    # Добавляем новый магазин в БД
    stores_info.append(new_store)
    # Возвращаем в ответ только что созданный новый магазин
    return jsonify(new_store), 201



# GET /store/<name> - отдаем информацию про магазин с именем name
#/store/ThridStore -> name = "ThirdStore"
@app.route('/store/<string:name>', methods=['GET'])
def get_store_by_name(name):

    # Переберем все магазины
    for store in stores_info:
        # Если имя какого-то магазина совпадает с искомым
        if store['name'] == name :
            # Возвращаем этот магазин
            return jsonify(store), 200
    # В случае, если такого магазина у нас нет
    return jsonify({'Error': "Store with that name not found"}), 404


# PUT /store/<name> - обновить информацию про магазин с имененем name
@app.route('/store/<string:name>', methods=['PUT'])
def update_store(name):
    for store in stores_info:
        if store['name'] == name:
            # Магазин с данным именем есть в БД
                request_data = request.get_json()
                # Переопределяем значение поля "items" для магазина store в БД
                store["items"] = request_data["items"]
                return jsonify(store), 202
    # В случае если не найду магазин с именем name - обновлять нечего!
    return jsonify({"Error" : "Store with that name not found"}), 404 






# DELETE /store/<name> - удалить информацию про магазин с именем name
@app.route('/store/<string:name>', methods=['DELETE'])
def delete_by_name(name):
    for store in stores_info:
        if store["name"] == name:
            ids = stores_info.index(store)
            stores_info.pop(ids)
            return jsonify({"Message" : "Store deleted"}), 202
    return jsonify({"Error" : "Store with that name not found"}), 404


#CRUD API - API с поддержкой операций(Create Read Update Delete)


if __name__ == "__main__":
    app.run(port=8000, debug=True)