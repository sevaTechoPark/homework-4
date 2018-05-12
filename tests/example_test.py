# -*- coding: utf-8 -*-

import os

import unittest
import urlparse

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

wait_time = 5


class Page(object):
    BASE_URL = 'http://ok.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)


class MainPage(Page):
    PATH = ''

    @property
    def top_menu(self):
        return TopMenu(self.driver)


class AuthForm(Component):
    LOGIN = '//input[@name="st.email"]'
    PASSWORD = '//input[@name="st.password"]'
    SUBMIT = '//input[@value="Войти"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class TopMenu(Component):
    NOTIFICATION = '//*[@id="ntf_toolbar_button"]/div[2]/div'
    TAB_TITLE = '//*[@id="hook_Block_NotificationsLayerTitle"]/div'

    ALL = '//*[@id="ntf_layer_menu_link_All"]/span'
    FRIENDS = '//*[@id="ntf_layer_menu_link_Friendships"]/span[1]'
    GIFTS = '//*[@id="ntf_layer_menu_link_Presents"]'
    GROUPS = '//*[@id="ntf_layer_menu_link_Groups"]'
    GAMES = '//*[@id="ntf_layer_menu_link_Games"]/span[1]'
    PAYMENTS = '//*[@id="ntf_layer_menu_link_Payments"]'
    VIDEOS = '//*[@id="ntf_layer_menu_link_Video"]'
    OTHERS = '//*[@id="ntf_layer_menu_link_Other"]'

    def select_notification(self):
        element = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.NOTIFICATION)
        )
        element.click()

    def wait_process(self):
        try:
            WebDriverWait(self.driver, wait_time).until(
                expected_conditions.visibility_of_element_located((By.CLASS_NAME, '__process')))
        except TimeoutException:
            print('wait process fail')

        try:
            WebDriverWait(self.driver, wait_time).until_not(
                expected_conditions.visibility_of_element_located((By.CLASS_NAME, '__process')))
        except TimeoutException:
            print('wait process fail')

    def choose_tab_all(self):
        element = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.ALL)
        )
        element.click()

        self.wait_process()

    def choose_tab_friends(self):
        element = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.FRIENDS)
        )
        element.click()

        self.wait_process()

    def choose_tab_gifts(self):
        element = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.GIFTS)
        )
        element.click()

        self.wait_process()

    def choose_tab_groups(self):
        element = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.GROUPS)
        )
        element.click()

        self.wait_process()

    def choose_tab_games(self):
        element = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.GAMES)
        )
        element.click()

        self.wait_process()

    def choose_tab_payments(self):
        element = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.PAYMENTS)
        )
        element.click()

        self.wait_process()

    def choose_tab_videos(self):
        element = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.VIDEOS)
        )
        element.click()

        self.wait_process()

    def choose_tab_others(self):
        element = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.OTHERS)
        )
        element.click()

        self.wait_process()

    def get_tab_title(self):
        return WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_xpath(self.TAB_TITLE).text
        )


class ExampleTest(unittest.TestCase):
    LOGIN = os.environ['LOGIN1']
    PASSWORD = os.environ['PASSWORD1']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        pass
        # self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_login(self.LOGIN)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        main_page = MainPage(self.driver)
        top_menu = main_page.top_menu
        top_menu.select_notification()

        title = top_menu.get_tab_title()
        self.assertEqual(u"Все оповещения", title)

        top_menu.choose_tab_friends()
        title = top_menu.get_tab_title()
        self.assertEqual(u"Дружбы", title)

        top_menu.choose_tab_gifts()
        title = top_menu.get_tab_title()
        self.assertEqual(u"Подарки", title)

        top_menu.choose_tab_groups()
        title = top_menu.get_tab_title()
        self.assertEqual(u"Группы", title)

        top_menu.choose_tab_games()
        title = top_menu.get_tab_title()
        self.assertEqual(u"Игры", title)

        top_menu.choose_tab_payments()
        title = top_menu.get_tab_title()
        self.assertEqual(u"Платежи", title)

        top_menu.choose_tab_videos()
        title = top_menu.get_tab_title()
        self.assertEqual(u"Видео", title)

        top_menu.choose_tab_others()
        title = top_menu.get_tab_title()
        self.assertEqual(u"Другие оповещения", title)

        main_page.open()
