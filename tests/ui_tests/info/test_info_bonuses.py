import allure


@allure.epic('UI')
@allure.story('info')
def test_info_bonuses(app, setup_browser):
    app.info.open_bonuses_info_button()
