#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from tests.Auth import UsersName
from tests.Auth.AuthPage import AuthPage
from tests.Main.AddMusic import AddMusic
from tests.Main.Album import AlbumComponent
from tests.Main.AudioAdd import AudioAdd
from tests.Main.Auth import AuthForm
from tests.Main.BlackList import BlackList
from tests.Main.CommentClass import CommentClass
from tests.Main.CreateChanel import CreateChanel
from tests.Main.Events import Events
from tests.Main.Friend import FriendComponent
from tests.Main.Gender import GenderComponent
from tests.Main.Group import GroupComponent
from tests.Main.Interview import Interview
from tests.Main.Language import LanguagePage, LanguageForm
from tests.Main.Like import LikeComponent, LikePage
from tests.Main.MainPage import MainPage
from tests.Main.Message import MessagePage, MessageComponent
from tests.Main.Mood import Mood
from tests.Main.Note import NoteComponent
from tests.Main.Relations import Relations
from tests.Main.Share import Share
from tests.Main.Theme import ThemePage, ThemeComponent
from tests.Main.VideoAdd import VideoAdd
from tests.constants.Constants import *


class Tests(unittest.TestCase):
    driver = None  # type: webdriver.Remote

    def setUp(self):
        pass

    def tearDown(self):
        like_component = LikeComponent(self.driver)
        album_component = AlbumComponent(self.driver)
        friend_component = FriendComponent(self.driver)
        group_component = GroupComponent(self.driver)
        gender_component = GenderComponent(self.driver)
        like_component.remove_like()
        album_component.delete_album()
        friend_component.cancel_request()
        group_component.unfollow()
        gender_component.back_to_start_gender()
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

    @classmethod
    def save_nicknames(cls):
        cls.auth_user()
        cls.log_out()
        cls.auth_user(False)
        cls.log_out()

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

    def test_select_notification_tabs(self):
        self.auth_user()

        main_page = MainPage(self.driver)
        top_menu = main_page.top_menu
        top_menu.select_notification()

        titles = []
        for i in range(0, len(NOTIFICATION_TABS_TITLE)):
            top_menu.choose_tab_notification(i)
            title = top_menu.get_tab_content_title()
            titles.append(title)
        self.assertTrue(set(NOTIFICATION_TABS_TITLE).issubset(titles))

    def test_report_notification(self):
        self.create_notification()
        self.auth_user()

        main_page = MainPage(self.driver)
        top_menu = main_page.top_menu
        top_menu.select_notification()
        top_menu.report_notification()
        first_notification = top_menu.place_first_notification()
        self.assertEqual(
            REPORT_SUCCESS, first_notification, "report notification fail")

    def test_close_notification(self):
        self.create_notification()
        self.auth_user()

        main_page = MainPage(self.driver)
        top_menu = main_page.top_menu
        top_menu.select_notification()
        top_menu.close_notification()
        is_notification_close = top_menu.check_notification_close()
        self.assertTrue(is_notification_close, "close notification fail")

    def test_add_reaction(self):
        self.auth_user()

        main_page = MainPage(self.driver)
        feed = main_page.feed
        reaction_number = feed.add_emotion_to_like()
        self.assertEqual(
            reaction_number, feed.get_number_emotion(), "add reaction fail")

    def test_change_reaction(self):

        self.auth_user()

        main_page = MainPage(self.driver)
        feed = main_page.feed
        old_reaction = feed.get_number_emotion()
        reaction_number = feed.add_emotion_to_like(old_reaction)
        self.assertNotEquals(reaction_number, old_reaction,
                             "change reaction fail")

    def test_remove_reaction(self):

        self.auth_user()

        main_page = MainPage(self.driver)
        feed = main_page.feed
        self.create_like()
        feed.remove_like()
        self.assertEquals(
            REACTIONS_CLASS, feed.get_number_emotion(), "remove reaction fail")

    def test_show_who_last_reaction(self):

        like_id = self.create_like()
        self.auth_user()
        self.open_user_wall()

        main_page = MainPage(self.driver)
        feed = main_page.feed
        names = feed.get_names_last_liked(like_id)
        self.assertIn(UsersName.second_account_name,
                      names, "second user not found")

    def test_go_to_page_who_last_reaction(self):

        like_id = self.create_like()
        self.auth_user()
        self.open_user_wall()

        main_page = MainPage(self.driver)
        feed = main_page.feed
        names = feed.get_names_last_liked(like_id)
        links = feed.get_links_last_liked(like_id)
        for i in range(0, len(links)):
            if names[i] == UsersName.first_account_name:
                continue
            main_page.BASE_URL = links[i]
            main_page.open()
            center_menu = main_page.center_menu
            nickname = center_menu.get_another_nickname()
            self.assertEqual(nickname, UsersName.second_account_name)

    def test_show_all_who_reaction(self):

        like_id = self.create_like()
        self.auth_user()
        self.open_user_wall()

        main_page = MainPage(self.driver)
        feed = main_page.feed
        feed.open_all_likes(like_id)
        names = feed.get_all_names()
        self.assertIn(UsersName.second_account_name,
                      names, "second user not found")

    def test_go_to_page_from_all_reaction(self):

        like_id = self.create_like()
        self.auth_user()
        self.open_user_wall()

        main_page = MainPage(self.driver)
        feed = main_page.feed
        feed.open_all_likes(like_id)
        names = feed.get_all_names()
        links = feed.get_all_links()
        for i in range(0, len(links)):
            if names[i] == UsersName.first_account_name:
                continue
            main_page.PATH = links[i]
            main_page.open()
            center_menu = main_page.center_menu
            nickname = center_menu.get_another_nickname()
            self.assertEqual(nickname, UsersName.second_account_name)

    def test_auth(self):
        auth_form = AuthForm(self.driver)
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form.set_login()
        auth_form.set_password()
        auth_form.submit()
        self.assertTrue(auth_form.isAuth(), "Wrong login or password")

    def test_album(self):
        self.auth_user()

        album_name = "new_album"
        album_component = AlbumComponent(self.driver)
        album_component.open_photos_page()
        album_component.create_album()
        albums = album_component.get_albums()
        albums.fill_name(album_name)
        self.assertIn(album_name,
                      albums, "Album not created")

    def test_auth(self):
        self.auth_user()
        self.assertGreater(self.driver.find_elements_by_css_selector('.toolbar_dropdown').__len__(),
                           0, "Wrong login or password")

    def test_friend(self):

        self.auth_user()

        friend_component = FriendComponent(self.driver)
        friend_component.open_friend_page()
        friend_component.add_to_friends()
        self.assertTrue(friend_component.get_pending_friends())

    def test_gender(self):
        self.auth_user()

        gender_component = GenderComponent(self.driver)
        gender_component.open_profile()
        gender_component.set_start_gender()
        gender_component.change_gender()
        gender_component.save()
        self.assertTrue(gender_component.get_current_gender(),
                        "Gender didn't changed!")

    def test_group(self):
        self.auth_user()

        group_component = GroupComponent(self.driver)
        group_component.fill_search()
        group_component.search()
        group_component.follow()
        self.assertTrue(group_component.checkFollow(), "Follow group error")

    def test_language(self):
        self.auth_user()

        language_settings_page = LanguagePage(self.driver)
        language_settings_page.PATH = 'settings'
        language_settings_page.open()

        language_form = LanguageForm(self.driver)
        language_form.open()
        inactive_language = language_form.get_inactive_language()
        language_form.change()
        active_language = language_form.get_active_language()
        self.assertNotEqual(inactive_language.lower(),
                            active_language.lower(), "Language haven't changed")

    def test_like(self):
        self.auth_user()

        like_page = LikePage(self.driver)
        like_page.PATH = 'feed'
        like_component = LikeComponent(self.driver)
        like_page.open()
        likes_from_btn_by_owner = int(
            like_component.get_likes_from_btn_by_owner())
        like_component.like_first_found_post()
        like_page.open()
        likes_count = int(
            like_component.likes_count)
        self.assertEqual(likes_from_btn_by_owner, likes_count, "like error!")

    def test_message(self):
        self.auth_user()

        messagePage = MessagePage(self.driver)
        messagePage.PATH = 'messages'
        messageComponent = MessageComponent(self.driver)
        messagePage.open()
        messageComponent.selectFirstDialog()
        messageComponent.writeMessage()
        messageComponent.send_message()
        DEFAULT_MESSAGE = "KEK"

        messageComponent.open_dialog()
        self.assertEqual(DEFAULT_MESSAGE,
                         messageComponent.get_last_message())

    def test_note(self):
        self.auth_user()

        note_page = NoteComponent(self.driver)
        note_page.open_notes()
        note_page.focus_note()
        note_page.set_note_text()
        note_page.upload_note()
        self.driver.refresh()
        self.assertEqual(note_page.get_last_post(),
                         note_page.DEFAULT_NOTE_TEXT, "Note post error")

    def test_blacklist(self):
        self.auth_user()
        black_man = BlackList(self.driver)
        black_man.open_friend_page()
        black_man.blacklist_choose()
        value = black_man.check_in_blacklist()
        self.assertTrue(value)

    def test_relations(self):
        self.auth_user()
        relations = Relations(self.driver)
        relations.friends_classmates()
        self.assertTrue(relations.classmates_checker())

    def test_share(self):
        self.auth_user()
        share = Share(self.driver)
        share_message = "What is the better than Qa ?"
        share.make_share(share_message)
        if share.share_checker(share_message):
            self.log_out()
            self.auth_user(False)
            share.make_share(share_message)
            self.assertTrue(share.share_checker(share_message))
        else:
            return False

    def test_adding_video(self):
        self.auth_user()
        audio = VideoAdd(self.driver)
        audio.open_video()
        self.assertTrue(audio.add_video())

    def test_creating_chanel(self):
        self.auth_user()
        chanel = CreateChanel(self.driver)
        chanel.open_chanel()
        value_before = chanel.before_chanel()
        chanel.chanel_name("test")

        if chanel.after_chanel() <= value_before:
            return False

        chanel.delete_clicker()

        self.assertTrue(chanel.after_chanel() > chanel.value_check())

    def test_mood(self):
        self.auth_user()
        mood = Mood(self.driver)
        mood.open_theme()
        mood.create_mood("End testing OK")
        self.log_out()
        self.auth_user(False)
        self.assertTrue(mood.mood_checker("End testing OK"))

    def test_interview(self):
        self.auth_user()

        interview = Interview(self.driver)
        interview.open_tab()
        interview.input_value("QA is a cool ?", "Yes", "Of Course")
        interview.vote_interview()
        self.assertTrue(interview.vote_value() > 0)

    def test_music_collections(self):
        self.auth_user()
        music = AddMusic(self.driver)
        music.open_music()
        music.add_playlist()
        self.assertTrue(music.check_music())

    def test_adding_music(self):
        self.auth_user()
        audio = AudioAdd(self.driver)
        self.assertTrue(audio.before_click() < audio.after_click())

    def test_event_message(self):
        self.auth_user()
        event = Events(self.driver)
        event.open_event()
        event.send_message("What about your diplom ?")
        self.log_out()
        self.auth_user(False)
        self.assertTrue(event.mr_checker())

    def test_comment_class(self):
        self.auth_user()
        myPage = CommentClass(self.driver)
        myPage.create_comment()
        myPage.add_like()
        myPage.like_checker()
        self.log_out()
        self.auth_user(False)
        self.assertTrue(myPage.event_like_checker())

    def test_theme(self):
        self.auth_user()

        themePage = ThemePage(self.driver)
        themePage.PATH = "themes"
        themePage.open()
        themeForm = ThemeComponent(self.driver)
        start_theme_name = themeForm.get_selected_theme()
        themeForm.select()
        themeForm.apply()

        self.assertNotEqual(start_theme_name,
                            themeForm.get_selected_theme(), "Theme apply error")
