import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser
from utils.attach_mobile import attach


@allure.epic('Mobile')
def test_skip_buttons():
    continue_button = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Далее'))
    great_button = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Отлично!'))

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
