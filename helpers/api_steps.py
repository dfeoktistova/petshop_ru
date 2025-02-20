import requests
from model.const import URL
import logging
from utils.attach import attach, logging
import allure


@allure.step("Отправить GET запрос")
def get_GET_response(url, **kwargs):
    response = requests.get(URL + url, **kwargs)
    cookies = response.cookies.get_dict()

    assert response.status_code == 200

    attach(response)
    logging(response)

    return cookies, response.json()


@allure.step("Отправить POST запрос")
def get_POST_response(url, **kwargs):
    response = requests.post(URL + url, **kwargs)
    cookies = response.cookies.get_dict()

    assert response.status_code == 200

    attach(response)
    logging(response)

    return cookies, response.json()


@allure.step("Отправить POST запрос")
def get_DELETE_response(url, **kwargs):
    response = requests.delete(URL + url, **kwargs)
    cookies = response.cookies.get_dict()

    assert response.status_code == 200

    attach(response)
    logging(response)

    return cookies, response.json()


@allure.step("Сравнить полученные результаты")
def assert_results(assert_type, expected_result, actual_result):
    if assert_type == 0:
        assert expected_result == actual_result, 'Ошибка: Фактический результат не соответствует ожидаемому!'
    elif assert_type == 1:
        assert expected_result in actual_result, 'Ошибка: Последовательность не сожержится в списке!'
    elif assert_type == 2:
        assert expected_result not in actual_result, 'Ошибка: Последовательность сожержится в списке!'
    elif assert_type == 3:
        assert expected_result != actual_result, 'Ошибка: Фактический результат не соответствует ожидаемому!'
