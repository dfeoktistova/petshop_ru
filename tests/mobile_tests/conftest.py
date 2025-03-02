import pytest
from appium import webdriver
from dotenv import load_dotenv
from selene import browser

import config
from utils import attach_mobile
import os
import allure
from allure_commons.types import AttachmentType
from selene import browser


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack",
        help="Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"
    load_dotenv(dotenv_path=env_file_path)

    return env_file_path


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    options = config.to_driver_options(context=context)

    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)

    allure.attach(browser.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
    allure.attach(browser.driver.page_source, name='xml_dump', attachment_type=AttachmentType.XML)
    session_id = browser.driver.session_id

    yield

    if context == 'bstack':
        attach_mobile.add_video(session_id, os.getenv('USER_NAME'), os.getenv('ACCESS_KEY'))

    browser.quit()
