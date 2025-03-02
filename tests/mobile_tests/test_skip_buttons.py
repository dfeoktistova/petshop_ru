from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser
from utils.attach_mobile import attach


def test_skip_buttons(mobile_management):
    continue_button = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Далее'))
    great_button = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Отлично!'))

    with step("Нажать кнопку 'Далее': Переход ко второму экрану"):
        continue_button.click()

        attach()

    with step("Нажать кнопку 'Далее': Переход к третьему экрану"):
        continue_button.click()

        attach()

    with step("Нажать кнопку 'Далее': Переход к четвертому экрану"):
        continue_button.click()

        attach()

    with step("Нажать кнопку 'Отлично!': Переход к авторизационному экрану"):
        great_button.click()

        attach()
