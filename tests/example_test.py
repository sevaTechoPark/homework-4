import os

import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.Auth import UsersName
from tests.Auth.AuthPage import AuthPage
from tests.Main.Album import AlbumComponent
from tests.Main.Friend import FriendComponent
from tests.Main.Gender import GenderComponent
from tests.Main.Group import GroupComponent
from tests.Main.Language import LanguagePage, LanguageForm
from tests.Main.Like import LikeComponent, LikePage
from tests.Main.MainPage import MainPage
from tests.Main.Message import MessagePage, MessageComponent
from tests.Main.Note import NoteComponent
from tests.Main.Theme import ThemePage, ThemeComponent
from tests.constants.Constants import *


class Tests(unittest.TestCase):
    driver = None  # type: webdriver.Remote

    def setUp(self):
        pass

    def tearDown(self):
        self.log_out()

    @classmethod
    def setUpClass(cls):
        browser = os.environ.get('BROWSER', 'CHROME')

        cls.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        cls.save_nicknames()

    @classmethod
    def tearDownClass(cls):
        pass
        # cls.driver.quit()

    @classmethod
    def save_nicknames(cls):
        cls.auth_user()
        cls.log_out()
        cls.auth_user(False)
        cls.log_out()
        print "save nicknames complete"

    @classmethod
    def auth_user(cls, who=True):
        auth_page = AuthPage(cls.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.authorized(who)

        main_page = MainPage(cls.driver)
        center_menu = main_page.center_menu
        nickname = center_menu.get_nickname()
        if who:
            UsersName.first_account_name = nickname
        else:
            UsersName.second_account_name = nickname

    @classmethod
    def log_out(cls):
        cls.driver.delete_all_cookies()
        cls.driver.refresh()

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

    # def test_select_notification_tabs(self):
    #     print "\ntest_select_notification_tabs"
    #     self.auth_user()
    #
    #     main_page = MainPage(self.driver)
    #     top_menu = main_page.top_menu
    #     top_menu.select_notification()
    #
    #     for i in range(0, len(NOTIFICATION_TABS_TITLE)):
    #         top_menu.choose_tab_notification(i)
    #         title = top_menu.get_tab_content_title()
    #         self.assertEqual(NOTIFICATION_TABS_TITLE[i], title, "select notification tabs")
    #
    # def test_report_notification(self):
    #     print "\ntest_report_notification"
    #     self.create_notification()
    #     self.auth_user()
    #
    #     main_page = MainPage(self.driver)
    #     top_menu = main_page.top_menu
    #     top_menu.select_notification()
    #     top_menu.report_notification()
    #     self.assertEqual(REPORT_SUCCESS, top_menu.place_first_notification(), "report notification fail")
    #
    # def test_close_notification(self):
    #     print "\ntest_close_notification"
    #     self.create_notification()
    #     self.auth_user()
    #
    #     main_page = MainPage(self.driver)
    #     top_menu = main_page.top_menu
    #     top_menu.select_notification()
    #     top_menu.close_notification()
    #     self.assertEqual(True, top_menu.check_notification_close(), "close notification fail")
    #
    # def test_add_reaction(self):
    #     print "\ntest_add_reaction"
    #     self.auth_user()
    #
    #     main_page = MainPage(self.driver)
    #     feed = main_page.feed
    #     reaction_number = feed.add_emotion_to_like()
    #     self.assertEqual(reaction_number, feed.get_number_emotion(), "add reaction fail")
    #
    # def test_change_reaction(self):
    #     print "\ntest_change_reaction"
    #
    #     self.auth_user()
    #
    #     main_page = MainPage(self.driver)
    #     feed = main_page.feed
    #     old_reaction = feed.get_number_emotion()
    #     reaction_number = feed.add_emotion_to_like(old_reaction)
    #     self.assertNotEquals(reaction_number, old_reaction, "change reaction fail")
    #
    # def test_remove_reaction(self):
    #     print "\ntest_remove_reaction"
    #
    #     self.auth_user()
    #
    #     main_page = MainPage(self.driver)
    #     feed = main_page.feed
    #
    #     feed.remove_like()
    #     self.assertEquals(5, feed.get_number_emotion(), "remove reaction fail")
    #
    def atest_show_who_last_reaction(self):
        print "\ntest_show_who_last_reaction"

        like_id = self.create_like()
        self.auth_user()
        self.open_user_wall()

        main_page = MainPage(self.driver)
        feed = main_page.feed
        names = feed.get_names_last_liked(like_id)
        is_second_user_liked = False
        if any(UsersName.second_account_name in s for s in names):
            is_second_user_liked = True
        self.assertTrue(is_second_user_liked, "second user not found")
    #
    # def test_go_to_page_who_last_reaction(self):
    #     print "\ntest_go_to_page_who_last_reaction"
    #
    #     like_id = self.create_like()
    #     self.auth_user()
    #     self.open_user_wall()
    #
    #     main_page = MainPage(self.driver)
    #     feed = main_page.feed
    #     names = feed.get_names_last_liked(like_id)
    #     links = feed.get_links_last_liked(like_id)
    #     for i in range(0, len(links)):
    #         if names[i] == UsersName.first_account_name:
    #             continue
    #         main_page.BASE_URL = links[i]
    #         main_page.open()
    #         center_menu = main_page.center_menu
    #         nickname = center_menu.get_another_nickname()
    #         if nickname == UsersName.second_account_name:
    #             self.assertTrue(True)
    #
    # def test_show_all_who_reaction(self):
    #     print "\ntest_show_all_who_reaction"
    #
    #     like_id = self.create_like()
    #     self.auth_user()
    #     self.open_user_wall()
    #
    #     main_page = MainPage(self.driver)
    #     feed = main_page.feed
    #     feed.open_all_likes(like_id)
    #     names = feed.get_all_names()
    #     is_second_user_liked = False
    #     if any(UsersName.second_account_name in s for s in names):
    #         is_second_user_liked = True
    #     self.assertTrue(is_second_user_liked, "second user not found")
    #
    # def test_go_to_page_from_all_reaction(self):
    #     print "\ntest_go_to_page_from_all_reaction"
    #
    #     like_id = self.create_like()
    #     self.auth_user()
    #     self.open_user_wall()
    #
    #     main_page = MainPage(self.driver)
    #     feed = main_page.feed
    #     feed.open_all_likes(like_id)
    #     names = feed.get_all_names()
    #     links = feed.get_all_links()
    #     for i in range(0, len(links)):
    #         if names[i] == UsersName.first_account_name:
    #             continue
    #         main_page.PATH = links[i]
    #         main_page.open()
    #         center_menu = main_page.center_menu
    #         nickname = center_menu.get_another_nickname()
    #         if nickname == UsersName.second_account_name:
    #             self.assertTrue(True)

    def test_album(self):
        print "album test"
        self.auth_user()


        album_component = AlbumComponent(self.driver)
        album_component.open_photos_page()
        album_component.create_album()

        album_component.open_photos_page()

        self.assertTrue(album_component.random_album_name in album_component.get_albums(), "Album not created")

    def test_auth(self):
        print "auth test"
        self.auth_user()
        self.assertGreater(self.driver.find_elements_by_css_selector('.toolbar_dropdown').__len__(),
                           0, "Wrong login or password")

    def test_friend(self):

        self.auth_user()

        friend_component = FriendComponent(self.driver)
        friend_component.open_friend_page()
        friend_component.add_to_friends()
        self.assertTrue(friend_component.get_pending_friends())
        friend_component.cancel_request()

    def test_gender(self):
        print 'gender test'
        self.auth_user()

        profile_component = GenderComponent(self.driver)
        profile_component.open_profile()
        profile_component.click_edit()
        profile_component.set_start_gender()
        profile_component.change_gender()
        profile_component.save()

        self.assertTrue(profile_component.get_current_gender(),"Gender didn't changed!")

    def test_group(self):
        print 'test group'
        self.auth_user()

        group_component = GroupComponent(self.driver)
        group_component.fill_search()
        group_component.search()
        group_component.follow()

        self.assertFalse(group_component.getFollowBtn(), "Follow group error")
        group_component.unfollow()

    def test_language(self):
        print "language test"
        self.auth_user()


        language_settings_page = LanguagePage(self.driver)
        language_settings_page.PATH = 'settings'
        language_settings_page.open()

        languageForm = LanguageForm(self.driver)
        languageForm.open()
        inactive_language = languageForm.get_inactive_language()
        languageForm.change()
        active_language = self.driver.find_element_by_css_selector(
            '.user-settings .user-settings_i:nth-of-type(6) .user-settings_i_tx').text
        self.assertTrue(inactive_language.lower() == active_language.lower(), "Language haven't changed")

    def test_like(self):
        print "like test"
        self.auth_user()


        like_page = LikePage(self.driver)
        like_page.PATH = 'feed'
        like_component = LikeComponent(self.driver)
        like_page.open()
        like_component.like_first_found_post()

        like_page.open()
        self.assertTrue(int(like_component.get_likes_from_btn_by_owner(like_component.data_id)) - 1 == int(
            like_component.likes_count), "like error!")
        like_component.remove_like(like_component.data_id)

    def test_message(self):
        print 'message test'
        self.auth_user()

        messagePage = MessagePage(self.driver)
        messagePage.PATH = 'messages'
        messageComponent = MessageComponent(self.driver)
        messagePage.open()
        messageComponent.selectFirstDialog()
        messageComponent.writeMessage()
        messageComponent.send_message()

        messageComponent.open_dialog()
        self.assertEqual(messageComponent.default_message, messageComponent.get_last_message())

    def test_note(self):
        print "note test"
        self.auth_user()


        note_page = NoteComponent(self.driver)
        note_page.open_notes()
        note_page.focus_note()
        note_page.set_note_text()
        note_page.upload_note()
        self.driver.refresh()
        last_post = self.driver.find_element_by_css_selector(
            "div[class='media-text_cnt']").text
        self.assertEqual(last_post,
                         note_page.default_note_text, "Note post error")

    def test_theme(self):
        print "theme test"
        self.auth_user()

        themePage = ThemePage(self.driver)
        themePage.PATH = "themes"
        themePage.open()
        themeForm = ThemeComponent(self.driver)
        themeForm.select()
        themeForm.apply()

        self.assertNotEqual(themeForm.start_theme_name,
                            themeForm.get_selected_theme(), "Theme apply error")