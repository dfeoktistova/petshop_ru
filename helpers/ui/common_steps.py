from model.const import URL
import allure
from selene import browser


class CommonHelper:
    @allure.step('Открыть главную страницу"')
    def open_home_page(self):
        browser.open(URL)
