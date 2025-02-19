import allure
from helpers.api import get_GET_response, get_POST_response, assert_results
from data.api_data import product_65292, product_66863
import pytest


@pytest.mark.parametrize("product_id, quantity, brand_id, brand, price",
                         [(
                          product_65292.product_id, product_65292.quantity, product_65292.brand_id, product_65292.brand,
                          product_65292.price),
                          (
                          product_66863.product_id, product_66863.quantity, product_66863.brand_id, product_66863.brand,
                          product_66863.price)])
def test_add_to_cart(product_id, quantity, brand_id, brand, price):
    url = 'api/v4/site/cart/'

    with allure.step("Добавить товар в корзину"):
        cookies_response_add_to_cart, response_add_to_cart = get_POST_response(url, json={'productId': product_id,
                                                                                          'quantity': quantity})

    with allure.step("Запросить содержимое корзины"):
        cookies_get_cart, response_get_cart = get_GET_response(url, cookies=cookies_response_add_to_cart)

        actual_result_item_id = []
        actual_result_brand_id = []
        actual_result_brand = []
        actual_result_price = []
        actual_result_cartItems = response_get_cart['cartItems']
        actual_result_quantity = None
        for cartItem in actual_result_cartItems:
            actual_result_brand_id.append(cartItem['product']['brandId'])
            actual_result_brand.append(cartItem['product']['brand'])
            actual_result_price.append(cartItem['offer']['price'])
            actual_result_item_id.append(cartItem['offer']['id'])
            actual_result_quantity = cartItem['quantity']
        actual_result_products_final_sum = response_get_cart['total']['productsFinalSum']

    with allure.step("Проверить ответ на наличие товара"):
        assert_results(1, product_id, actual_result_item_id)
        assert_results(1, brand_id, actual_result_brand_id)
        assert_results(1, brand, actual_result_brand)
        assert_results(1, price, actual_result_price)
        assert_results(0, quantity, actual_result_quantity)
        assert_results(0, price * quantity, actual_result_products_final_sum)
