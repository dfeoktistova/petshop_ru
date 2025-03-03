import allure


@allure.epic('UI')
@allure.story('info')
def test_info_delivery(app):
    app.info.open_delivery_info()


@allure.epic('UI')
@allure.story('info')
def test_info_quick_delivery(app):
    app.info.open_quick_delivery_info()
