# coding=utf-8
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from tests.Lilbs.Lib import Lib
from tests.constants.Constants import waitTime
from tests.models.Component import Component
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class CenterMenu(Component):
    WALL_TOOLBAR = '//div[@id="mainContentLeftColumn"]//div[@id="hook_Block_SideNavigation"]//div[@data-l="t,navigation"]//a[@data-l="t,userPage"]'
    WALL_CONTENT = '//div[@id="hook_Block_UserFeed"]//div[contains(@data-l, "feedLocation,self,")]'
    FEED_LIST = '//div[@class="feed-list"][@data-l="feedLocation,self"]'

    def select_wall(self):
        Lib.simple_wait_element(self.driver, self.WALL_TOOLBAR).click()
        Lib.visibility_wait_element(self.driver, self.WALL_CONTENT)
        element = Lib.visibility_wait_element(self.driver, self.FEED_LIST)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_nickname(self):
        return Lib.simple_wait_element(self.driver, self.WALL_TOOLBAR).text

