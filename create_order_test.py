#Вера Абдулина, 10 поток, финальный проект, инженер по тестированию
import sender_stand_request
import data


#тест на создание заказа
def test_create_order():
    order_response = sender_stand_request.post_new_order(data.order_body)
    track = order_response.json()["track"]
#получение заказа по его номеру
    order_get_response = sender_stand_request.get_order(track)
    assert order_get_response.status_code == 200

