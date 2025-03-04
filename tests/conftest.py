import os
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from model.const import URL
from helpers.ui.application import Application
from utils import attach_ui

DEFAULT_BROWSER_NAME = "chrome"
DEFAULT_BROWSER_VERSION = "126.0"
DEFAULT_MOBILE_ENV = 'browserstack'
DEFAULT_UI_ENV = 'local'


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        choices=['chrome', 'firefox'],
        default='chrome'
    )
    parser.addoption(
        '--browser_version',
        choices=['99.0', '100.0', '113.0', '114.0', '120.0', '121.0', '122.0', '123.0', '124.0', '125.0', '126.0'],
        default='126.0'
    )
    parser.addoption(
        '--mobile_env',
        default=DEFAULT_MOBILE_ENV
    )
    parser.addoption(
        '--ui_env',
        choices=['local', 'selenoid'],
        default=DEFAULT_UI_ENV
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(autouse=True, scope="session")
def app():
    return Application()


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_name = request.config.getoption('--browser_name')
    ui_env = request.config.getoption('--ui_env')

    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    browser_name = browser_name if browser_name != "" else DEFAULT_BROWSER_NAME
    ui_env = ui_env if ui_env != "" else DEFAULT_UI_ENV

    options = Options()

    if ui_env == 'local':
        options.page_load_strategy = 'eager'
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')

    if ui_env == 'selenoid':
        selenoid_capabilities = {
            "browserName": browser_name,
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        options.capabilities.update(selenoid_capabilities)

        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')
        driver = webdriver.Remote(command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
                                  options=options)

        browser.config.driver = driver
        browser.config.window_width = 1920
        browser.config.window_height = 1080

    browser.config.base_url = URL
    browser.config.driver_options = options
    browser.config.timeout = 20.0

    browser.open(URL)

    yield browser

    attach_ui.add_screenshot(browser)
    attach_ui.add_logs(browser)
    attach_ui.add_html(browser)
    attach_ui.add_video(browser)

    browser.quit()
