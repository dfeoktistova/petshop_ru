import logging as log
import allure
from allure_commons.types import AttachmentType
import json


def attach(response):
    allure.attach(body=response.request.method + " " + response.request.url, name="Request",
                  attachment_type=AttachmentType.TEXT, extension="txt")
    allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                  attachment_type=AttachmentType.JSON, extension="json")


def logging(response):
    log.info(response.request.url)
    log.info(response.status_code)
    log.info(response.text)
