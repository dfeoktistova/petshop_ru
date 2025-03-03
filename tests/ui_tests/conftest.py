import pytest
from selene import browser
from selenium import webdriver
from model.const import URL
from selenium.webdriver.chrome.options import Options
from helpers.ui.application import Application
from utils import attach_ui


@pytest.fixture(autouse=True, scope="session")
def app():
    return Application()


@pytest.fixture(scope='session', autouse=True)
def browser_management():
    browser.config.base_url = 'https://www.petshop.ru'

    browser.config.timeout = 2.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    options = Options()

    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")

    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications-prompt")

    yield browser

    browser.quit()


@pytest.fixture(scope='function', autouse=True)
def open_home_page():
    browser.open(URL)


@pytest.fixture(scope='function', autouse=True)
def attach():
    yield

    # attach_ui.add_screenshot(browser)
    # attach_ui.add_logs(browser)
    # attach_ui.add_html(browser)
    # attach_ui.add_video(browser)
