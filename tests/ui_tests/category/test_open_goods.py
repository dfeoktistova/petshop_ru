import allure


@allure.epic('UI')
@allure.story('category')
def test_open_dogscatalog(setup_browser, app):
    app.category.open_dogs_catalog()


@allure.epic('UI')
@allure.story('category')
def test_open_cats_catalog(setup_browser, app):
    app.category.open_cats_catalog()
