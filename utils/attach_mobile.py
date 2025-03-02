import allure
import requests
from selene import browser
from allure_commons.types import AttachmentType


def add_video(session_id, login, access_key):
    browserstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json', auth=(login, access_key)).json()
    video_url = browserstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src={video_url} type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML)


def attach():
    allure.attach(browser.driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
    allure.attach(browser.driver.page_source, name='xml_dump', attachment_type=AttachmentType.XML)
