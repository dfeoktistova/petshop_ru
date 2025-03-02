import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser
from utils.attach_mobile import attach


@allure.epic('Mobile')
def test_open_help(mobile_management):
    continue_button = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Далее'))
    great_button = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Отлично!'))
    help_button = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Помощь 24/7'))

    with allure.step("Нажать кнопку 'Далее': Переход ко второму экрану"):
        continue_button.click()

        attach()

    with allure.step("Нажать кнопку 'Далее': Переход к третьему экрану"):
        continue_button.click()

        attach()

    with allure.step("Нажать кнопку 'Далее': Переход к четвертому экрану"):
        continue_button.click()

        attach()

    with allure.step("Нажать кнопку 'Отлично!': Переход к авторизационному экрану"):
        great_button.click()

        attach()

    with allure.step("Нажать кнопку связи с поддержкой"):
        help_button.click()

        attach()
