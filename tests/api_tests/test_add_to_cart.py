from helpers.api.api_steps import get_GET_response, get_POST_response, assert_results
from data.api_data import product_120571_toys, product_127000_toys
import pytest
import allure
from jsonschema import validate
from data.schemas import schema_add_to_cart


@allure.epic('API')
@pytest.mark.parametrize("product_id, quantity, brand_id, brand, price",
                         [(product_120571_toys.product_id, product_120571_toys.quantity,
                           product_120571_toys.brand_id, product_120571_toys.brand,
                           product_120571_toys.price),
                          (product_127000_toys.product_id, product_127000_toys.quantity,
                           product_127000_toys.brand_id, product_127000_toys.brand,
                           product_127000_toys.price)])
def test_add_to_cart(product_id, quantity, brand_id, brand, price):
    url = 'api/v4/site/cart/'

    with allure.step("Добавить товар в корзину"):
        response = {'productId': product_id, 'quantity': quantity}
        validate(response, schema_add_to_cart)

        cookies_response_add_to_cart, response_add_to_cart = get_POST_response(url, json=response)

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
