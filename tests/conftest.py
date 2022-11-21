import os
import pytest
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from appium import webdriver

from selene.support.shared import browser

from qa_guru_mobile_1.utils import attachments


@pytest.fixture(scope='session', autouse=True)
def driver_management():
    load_dotenv()

    options = UiAutomator2Options().load_capabilities({
        "app": os.getenv("app"),
        "deviceName": "Google Pixel 3",
        "platformVersion": "9.0",
        "project": "Python project",
        "build": "wikipedia-build-qa_guru",
        'bstack:options': {
            "projectName": "Wikipedia project",
            "buildName": "wikipedia-build-01",
            "sessionName": "BStack first_test",
            "userName": os.getenv('user_name'),
            "accessKey": os.getenv('access_key'),
        }
    })
    browser.config.driver = webdriver.Remote(
        command_executor="http://hub.browserstack.com/wd/hub",
        options=options
    )
    browser.config.timeout = 6
    yield driver_management
    attachments.add_video(browser)
    browser.quit()


@pytest.fixture(scope='session', autouse=True)
def patch_selene():
    import qa_guru_mobile_1.extensions.selene.patch_selector  # noqa