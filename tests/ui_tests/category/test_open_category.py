import pytest
import allure


@allure.epic('UI')
@allure.story('category')
@pytest.mark.parametrize("category, title",
                         [('Еда', 'Корм для собак'),
                          ('Аптека', 'Лекарства для собак'),
                          ('Гигиена и уход', 'Средства гигиены для собак'),
                          ('Предметы обихода', 'Предметы обихода для собак'),
                          ('Игрушки', 'Игрушки для собак'),
                          ('Аксессуары', 'Аксессуары для собак'),
                          ('Умные товары', 'Умные товары для собак'),
                          ('Для дрессировки', 'Товары для дрессировки собак'),
                          ('Подарочные сертификаты', 'Подарочные сертификаты на товары для собак')])
def test_open_dogs_category(app, category, title):
    app.category.open_dogs_goods()
    app.category.open_category(category)
    app.category.assert_title(title)


@allure.epic('UI')
@allure.story('category')
@pytest.mark.parametrize("category, title",
                         [('Еда', 'Корм для кошек'),
                          ('Аптека', 'Лекарства для кошек'),
                          ('Гигиена и уход', 'Средства гигиены для кошек'),
                          ('Предметы обихода', 'Предметы обихода для кошек'),
                          ('Игрушки', 'Игрушки для кошек'),
                          ('Аксессуары', 'Аксессуары для кошек'),
                          ('Умные товары', 'Умные товары для кошек'),
                          ('Подарочные сертификаты', 'Подарочные сертификаты')])
def test_open_cats_category(app, category, title):
    app.category.open_cats_goods()
    app.category.open_category(category)
    app.category.assert_title(title)
