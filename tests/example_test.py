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
        pass
        # self.driver.quit()

    def auth_user(self, who=True):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.authorized(who)

    def log_out(self):
        main_page = MainPage(self.driver)
        exit_menu = main_page.exit_menu
        exit_menu.log_out()

    def test_select_notification_tabs(self):
        self.auth_user()

        main_page = MainPage(self.driver)
        top_menu = main_page.top_menu
        top_menu.select_notification()

        title = top_menu.get_tab_title()
        self.assertEqual(notificationsAll, title)

        top_menu.choose_tab_friends()
        title = top_menu.get_tab_title()
        self.assertEqual(notificationsFriends, title)

        top_menu.choose_tab_gifts()
        title = top_menu.get_tab_title()
        self.assertEqual(notificationsGifts, title)

        top_menu.choose_tab_groups()
        title = top_menu.get_tab_title()
        self.assertEqual(notificationsGroups, title)

        top_menu.choose_tab_games()
        title = top_menu.get_tab_title()
        self.assertEqual(notificationsGames, title)

        top_menu.choose_tab_payments()
        title = top_menu.get_tab_title()
        self.assertEqual(notificationsPayments, title)

        top_menu.choose_tab_videos()
        title = top_menu.get_tab_title()
        self.assertEqual(notificationsVideos, title)

        top_menu.choose_tab_others()
        title = top_menu.get_tab_title()
        self.assertEqual(notificationsOthers, title)

        self.log_out()

    def test_report_notification(self):
        self.auth_user(False)
