import allure


@allure.epic('UI')
@allure.story('info')
def test_info_action(app, setup_browser):
    app.info.open_action_info()
