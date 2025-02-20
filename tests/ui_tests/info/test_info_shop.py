import allure


@allure.epic('UI')
@allure.story('info')
def test_info_shop(app):
    app.info.open_shop_info_button()
