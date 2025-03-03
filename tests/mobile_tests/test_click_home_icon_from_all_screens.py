import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser
from utils.attach_mobile import attach


@allure.epic('Mobile')
def test_click_home_icon_from_all_screens():
    first_screen_line = browser.element(
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)'))
    second_screen_line = browser.element(
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(6)'))
    third_screen_line = browser.element(
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(7)'))
    fourth_screen_line = browser.element(
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(8)'))
    home_icon = browser.element(
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'))

    with allure.step("Перейти ко второму экрану и нажать на домашнюю иконку"):
        second_screen_line.click()
        home_icon.click()
        time.sleep(5)

        attach()

    with allure.step("Перейти к третьему экрану и нажать на домашнюю иконку"):
        third_screen_line.click()
        home_icon.click()

        attach()

    with allure.step("Перейти к четвертому экрану и нажать на домашнюю иконку"):
        fourth_screen_line.click()
        home_icon.click()

        attach()

    with allure.step("Перейти к первому экрану и нажать на домашнюю иконку"):
        first_screen_line.click()
        home_icon.click()

        attach()