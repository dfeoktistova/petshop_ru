import os
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helpers.ui.application import Application
from utils import attach_ui, attach_mobile
import config
from appium import webdriver as appium_driver

DEFAULT_BROWSER_NAME = "chrome"
DEFAULT_BROWSER_VERSION = "126.0"
DEFAULT_UI_ENV = 'local'
DEFAULT_MOBILE_ENV = 'local_emulator'


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
        '--context',
        choices=['bstack', 'local_emulator'],
        default=DEFAULT_MOBILE_ENV
    )
    parser.addoption(
        '--ui_env',
        choices=['local', 'selenoid'],
        default=DEFAULT_UI_ENV
    )


@pytest.fixture(scope="function", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(autouse=True, scope="session")
def app():
    return Application()


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"
    load_dotenv(dotenv_path=env_file_path)

    return env_file_path


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function')
def mobile_management(context):
    options = config.to_driver_options(context=context)

    browser.config.driver = appium_driver.Remote(options.get_capability('remote_url'), options=options)

    session_id = browser.driver.session_id

    yield

    if context == 'bstack':
        attach_mobile.add_video(session_id, os.getenv('USER_NAME'), os.getenv('ACCESS_KEY'))

    browser.quit()


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_name = request.config.getoption('--browser_name')
    ui_env = request.config.getoption('--ui_env')

    driver_options = webdriver.ChromeOptions()

    if ui_env == 'local':
        driver_options.add_argument('--disable-gpu')
        driver_options.add_argument('--no-sandbox')

    if ui_env == 'selenoid':
        options = Options()
        selenoid_capabilities = {
            "browserName": browser_name,
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        options.capabilities.update(selenoid_capabilities)

        driver = webdriver.Remote(
            command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
            options=options)

        browser.config.driver = driver

    browser.config.window_width = 1920
    browser.config.window_height = 1080

    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.timeout = 15.0

    yield

    attach_ui.add_screenshot(browser)
    attach_ui.add_logs(browser)
    attach_ui.add_html(browser)
    attach_ui.add_video(browser)

    browser.quit()
