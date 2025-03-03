from helpers.api.api_steps import get_GET_response
import allure
from jsonschema import validate
from data.schemas import schema_get_suggestions


@allure.epic('API')
def test_get_suggestions():
    url = 'api/v4/site/catalog/suggestions/?phrase='

    with allure.step("Запросить акционные предложения"):
        cookies, response = get_GET_response(url)
        validate(response, schema_get_suggestions)