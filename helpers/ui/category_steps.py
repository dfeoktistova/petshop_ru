import allure
from selene import browser, by, have


class CategoryHelper:
    def __init__(self):
        self.category_dogs = browser.element('[href="/catalog/dogs/"]')
        self.category_cats = browser.element('[href="/catalog/cats/"]')
        self.category_title = browser.element('[class="text text_text__8Us2K PageTitle_title__AxCoi"]')

    @allure.step('Открыть товары для собак')
    def open_dogs_goods(self):
        self.category_dogs.click()

    @allure.step('Открыть товары для кошек')
    def open_cats_goods(self):
        self.category_cats.click()

    @allure.step('Открыть категорию товаров {category}')
    def open_category(self, category):
        browser.element(f'[title="{category}"]').click()

    @allure.step('Проверить, что название раздела = {title}')
    def assert_title(self, title):
        self.category_title.should(have.text(title))