import time
from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser
from utils.attach_mobile import attach


@allure.epic('Mobile')
def test_screen_lines(mobile_management):
    first_screen_line = browser.element(
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)'))
    second_screen_line = browser.element(
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(6)'))
    third_screen_line = browser.element(
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(7)'))
    fourth_screen_line = browser.element(
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(8)'))

    with step("Перейти ко второму экрану"):
        second_screen_line.click()
        time.sleep(1)

        attach()

    with step("Перейти к третьему экрану"):
        third_screen_line.click()

        attach()

    with step("Перейти к четвертому экрану"):
        fourth_screen_line.click()

        attach()

    with step("Перейти к первому экрану"):
        first_screen_line.click()

        attach()
