import configuration
import requests
import data

#создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)

#получение заказа по его треку
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK,
                         params={"t": track},
                         headers=data.headers)

