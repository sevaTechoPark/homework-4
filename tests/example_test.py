import os

import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.Auth.AuthPage import AuthPage
from tests.Auth.UsersName import UsersName
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
        # self.log_out()
        # self.driver.quit()

    def auth_user(self, who=True):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.authorized(who)

        main_page = MainPage(self.driver)
        center_menu = main_page.center_menu
        nickname = center_menu.get_nickname()
        UsersName.set_login(who, nickname)

    def log_out(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def create_notification(self):
        self.auth_user(False)
        main_page = MainPage(self.driver)
        top_menu = main_page.top_menu
        top_menu.select_friends()
        friends = main_page.friends
        friends.invite__friend_to_group()

        self.log_out()

    def create_like(self):
        self.auth_user(False)
        main_page = MainPage(self.driver)
        top_menu = main_page.top_menu
        top_menu.select_friends()
        friends = main_page.friends
        friends.select_friend()
        feed = main_page.feed
        like_id = feed.add_like()
        self.log_out()
        return like_id

    def open_user_wall(self):
        main_page = MainPage(self.driver)
        center_menu = main_page.center_menu
        center_menu.select_wall()

    def off_test_select_notification_tabs(self):
        self.auth_user()

        main_page = MainPage(self.driver)
        top_menu = main_page.top_menu
        top_menu.select_notification()

        for i in range(0, len(NOTIFICATION_TABS_TITLE)):
            top_menu.choose_tab_notification(i)
            title = top_menu.get_tab_content_title()
            self.assertEqual(NOTIFICATION_TABS_TITLE[i], title, "select notification tabs")

    def off_test_report_notification(self):
        self.create_notification()
        self.auth_user()

        main_page = MainPage(self.driver)
        top_menu = main_page.top_menu
        top_menu.select_notification()
        top_menu.report_notification()
        self.assertEqual(REPORT_SUCCESS, top_menu.place_first_notification(), "report notification fail")

    def off_test_close_notification(self):
        self.create_notification()
        self.auth_user()

        main_page = MainPage(self.driver)
        top_menu = main_page.top_menu
        top_menu.select_notification()
        top_menu.close_notification()
        self.assertEqual(True, top_menu.check_notification_close(), "close notification fail")

    def off_test_add_reaction(self):
        self.auth_user()

        main_page = MainPage(self.driver)
        feed = main_page.feed

        reaction_number = feed.add_emotion_to_like()
        self.assertEqual(reaction_number, feed.get_number_emotion(), "add reaction fail")

    def off_test_change_reaction(self):
        self.auth_user()

        main_page = MainPage(self.driver)
        feed = main_page.feed
        for i in range(0, 10):
            old_reaction = feed.get_number_emotion()
            reaction_number = feed.add_emotion_to_like(old_reaction)
            print reaction_number, old_reaction
            self.assertNotEquals(reaction_number, old_reaction, "change reaction fail")

    def off_test_remove_reaction(self):
        self.auth_user()

        main_page = MainPage(self.driver)
        feed = main_page.feed

        feed.remove_like()
        self.assertEquals(5, feed.get_number_emotion(), "remove reaction fail")

    def test_show_who_last_reaction(self):
        like_id = self.create_like()
        self.auth_user()
        self.open_user_wall()

        main_page = MainPage(self.driver)
        feed = main_page.feed
        names = feed.get_names_last_liked(like_id)
        is_second_user_liked = False
        if any(UsersName.get_login(False) in s for s in names):
            is_second_user_liked = True
        self.assertTrue(is_second_user_liked, "second user not found")
