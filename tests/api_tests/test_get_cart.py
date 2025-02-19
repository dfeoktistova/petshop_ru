import allure
from helpers.api import get_GET_response


def test_get_cart():
    url = 'api/v4/site/cart/'

    with allure.step("Запросить содержимое корзины"):
        get_GET_response(url)
