import allure
from selene import browser, by, have


class InfoHelper:
    def __init__(self):
        self.delivery_info_button = browser.element('[class="delivery"]')
        self.action = browser.element('[class="action"]')
        self.shop = browser.element('[class="shop"]')
        self.bonuses = browser.element('[class="bonuses"]')

        self.delivery_title = browser.element('[class="DeliverySelect_wrapper__3xUUq DeliverySelect_mobile__AbSiK '
                                              'DeliverySelect_tablet__DUtNY DeliverySelect_desktop__hx2OW"]')
        self.action_title = browser.element('[class="text text_text__8Us2K PageTitle_title__AxCoi"]')
        self.bonuses_title = browser.element('[class="HeaderBlock_left__Tg60m HeaderBlock_h1__VTWcb"]')

    @allure.step('Открыть страницу "Доставка"')
    def open_delivery_info_button(self):
        self.delivery_info_button.click()
        self.delivery_title.should(have.text('Способы доставки в'))

    @allure.step('Открыть страницу "Акции и скидки"')
    def open_action_info_button(self):
        self.action.click()
        self.action_title.should(have.text('Акции и распродажи в Petshop'))

    @allure.step('Открыть страницу "Магазины и пункты выдачи"')
    def open_shop_info_button(self):
        self.shop.click()

    @allure.step('Открыть страницу "Программы лояльности"')
    def open_bonuses_info_button(self):
        self.bonuses.click()
        self.bonuses_title.should(have.text('Бонусные программы'))
