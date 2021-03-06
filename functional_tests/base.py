from datetime import datetime
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import override_settings
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options


class FunctionalTest(StaticLiveServerTestCase):
    host = 'web'

    def setUp(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Remote(
            'http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
        self.browser.get(self.live_server_url)
        self.actions = ActionChains(self.browser)

    def tearDown(self):
        if self._test_has_failed():
            for i, handle in enumerate(self.browser.window_handles):
                self.browser.switch_to.window(handle)
                filepath = self._create_error_capture_filepath(i)
                timestamp = datetime.now()
                self.browser.save_screenshot(
                    f'{filepath}/screenshot-{timestamp}.png')
                self.capture_html(filepath, timestamp)
        self.browser.quit()

    def _test_has_failed(self):
        # returns True if any errors were raised during test run
        return any(error for (method, error) in self._outcome.errors)

    def _create_error_capture_filepath(self, handle_index):
        timestamp = datetime.now()
        classname = self.__class__.__name__
        method = self._testMethodName
        dir_path = f'functional_tests/error_capture/{timestamp}-{classname}.{method}/{handle_index}'
        os.makedirs(dir_path)
        return dir_path

    def capture_html(self, filepath, timestamp):
        filename = f'{filepath}/source-{timestamp}.html'
        with open(filename, 'w') as f:
            f.write(self.browser.page_source)
