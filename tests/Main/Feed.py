# coding=utf-8
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from tests.Lilbs.Lib import Lib
from tests.constants.Constants import waitTime
from tests.models.Component import Component
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class Feed(Component):
    LIKE_BUTTONS = '//div[@class="feed-list"]//div[@class="feed-w"]//ul[@class="widget-list"]//li[@class="widget-list_i "][last()]'
    REACTION_PANEL = '//div[@class="hook_Blocl_ShortcutMenuReact"]//div[@class="reactions"]'
    REACTIONS = ['//span[@data-l="t,reaction0"]', '//span[@data-l="t,reaction1"]', '//span[@data-l="t,reaction2"]',
                 '//span[@data-l="t,reaction3"]', '//span[@data-l="t,reaction4"]']
    for reaction in REACTIONS:
        reaction += REACTION_PANEL

    def add_emotion_to_like(self):
        element = Lib.simple_wait_element(self.driver, self.LIKE_BUTTONS)
        Lib.hover(self.driver, element)
        Lib.visibility_wait_element(self.driver, self.REACTION_PANEL)
        Lib.visibility_wait_element(self.driver, self.REACTIONS[0]).click()
