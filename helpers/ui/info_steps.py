import time

import allure
from selene import browser, by, have


class InfoHelper:
    def __init__(self):
        self.delivery_info_button = browser.element('[class="delivery"]')
        self.action_info_button = browser.element('[class="action"]')
        self.shop_info_button = browser.element('[class="shop"]')
        self.bonuses_info_button = browser.element('[class="bonuses"]')

        self.delivery_title = browser.element('[class="DeliverySelect_wrapper__3xUUq DeliverySelect_mobile__AbSiK '
                                              'DeliverySelect_tablet__DUtNY DeliverySelect_desktop__hx2OW"]')
        self.action_title = browser.element('[class="text text_text__8Us2K PageTitle_title__AxCoi"]')
        self.bonuses_title = browser.element('[class="HeaderBlock_left__Tg60m HeaderBlock_h1__VTWcb"]')
        self.pesthopru_icon = browser.element('[class="Link_link__-8H7G FirstLine_item__A3tLl action-header-top__logo '
                                              'PetshopLogo_link__Bzop1"]')

        self.shop_list_button = browser.element('[class="Link_link__-8H7G Button_item__R0pkO FirstLine_item_30__2WIgo '
                                                'action-header-top__color Button_item_black__p1j2K '
                                                'Button_item_click__syE0M"]')

    @allure.step('Открыть страницу "Доставка" через кнопку "Условия доставки"')
    def open_delivery_info(self):
        self.delivery_info_button.click()

    @allure.step('Открыть страницу "Акции и скидки"')
    def open_action_info(self):
        self.action_info_button.click()
        time.sleep(10)
        self.action_title.should(have.text('Акции и распродажи в Petshop'))

    @allure.step('Открыть страницу "Магазины и пункты выдачи" через кнопку "Магазины и пункты выдачи"')
    def open_shop_info(self):
        self.shop_info_button.click()

    @allure.step('Открыть страницу "Магазины и пункты выдачи" через кнопку "Магазины"')
    def open_shop_list(self):
        self.shop_list_button.click()

    @allure.step('Открыть страницу "Программы лояльности"')
    def open_bonuses_info_button(self):
        self.bonuses_info_button.click()
        self.bonuses_title.should(have.text('Бонусные программы'))
