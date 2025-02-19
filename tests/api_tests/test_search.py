import pytest
from helpers.api import get_GET_response
import urllib.parse
import allure


@pytest.mark.parametrize("cityId, page, query",
                         [(22, 1, 'корм для собак'),
                          (21, 2, 'Игрушка для щенка')])
def test_search(cityId, page, query):
    with allure.step("Выполнить поиск по сайту"):
        encode_query = urllib.parse.quote(query)

        url = f'api/v4/site/catalog/products/?cityId={cityId}&page={page}&query={encode_query}'

        get_GET_response(url)
