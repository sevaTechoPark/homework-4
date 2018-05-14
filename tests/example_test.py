import os

import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.Auth.AuthPage import AuthPage
from tests.Main.MainPage import MainPage
from tests.constants.Constants import *


class Tests(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        # pass
        self.driver.quit()

    def auth_user(self, who=True):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.authorized(who)

    def log_out(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def create_notification(self):
        self.auth_user(False)
        main_page = MainPage(self.driver)
        top_menu = main_page.top_menu
        top_menu.select_friends()
        top_menu.invite_to_group()

        self.log_out()

    def test_select_notification_tabs(self):
        self.auth_user()

        main_page = MainPage(self.driver)
        top_menu = main_page.top_menu
        top_menu.select_notification()

        for i in range(0, len(NOTIFICATION_TABS_TITLE)):
            top_menu.choose_tab_notification(i)
            title = top_menu.get_tab_content_title()
            self.assertEqual(NOTIFICATION_TABS_TITLE[i], title, "select notification tabs")

        self.log_out()

    def test_report_notification(self):
        self.create_notification()
        self.auth_user()

        main_page = MainPage(self.driver)
        top_menu = main_page.top_menu
        top_menu.select_notification()
        top_menu.report_notification()
        self.assertEqual(REPORT_SUCCESS, top_menu.place_first_notification(), "report notification fail")
        self.log_out()

    def test_close_notification(self):
        self.create_notification()
        self.auth_user()

        main_page = MainPage(self.driver)
        top_menu = main_page.top_menu
        top_menu.select_notification()
        top_menu.close_notification()
        self.assertEqual(True, top_menu.check_notification_close(), "close notification fail")
        self.log_out()

