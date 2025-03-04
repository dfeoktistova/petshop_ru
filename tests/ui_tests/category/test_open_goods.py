import allure


@allure.epic('UI')
@allure.story('category')
def test_open_dogs_goods(app, setup_browser):
    app.category.open_dogs_goods()


@allure.epic('UI')
@allure.story('category')
def test_open_cats_goods(app, setup_browser):
    app.category.open_cats_goods()
