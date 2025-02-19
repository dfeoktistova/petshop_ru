import pytest
from selene import browser, have
from selenium import webdriver
from model.const import URL


@pytest.fixture(scope='session', autouse=True)
def browser_management():
    browser.config.timeout = 2.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    browser.open(URL)

    yield

    browser.quit()