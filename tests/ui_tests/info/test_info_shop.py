import time

import allure


@allure.epic('UI')
@allure.story('info')
def test_info_shop(app, setup_browser):
    app.common.open_home_page()
    app.info.open_shop_info()


@allure.epic('UI')
@allure.story('info')
def test_shop_list(app, setup_browser):
    app.common.open_home_page()
    app.info.open_shop_list()
    time.sleep(5)
