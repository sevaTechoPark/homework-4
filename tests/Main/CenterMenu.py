from selenium.common.exceptions import NoSuchElementException, TimeoutException

from tests.Lilbs.Lib import Lib
from tests.models.Component import Component


class CenterMenu(Component):
    WALL_TOOLBAR = '//div[@id="mainContentLeftColumn"]//div[@id="hook_Block_SideNavigation"]//div[@data-l="t,navigation"]//a[@data-l="t,userPage"]'
    WALL_CONTENT = '//div[@id="hook_Block_UserFeed"]//div[contains(@data-l, "feedLocation,self,")]'
    FEED_LIST = '//div[@class="feed-list"][@data-l="feedLocation,self"]'
    MY_ACCOUNT_NAME = '//div[@id="mainContentLeftColumn"]//div[@id="hook_Block_SideNavigation"]//div[@data-l="t,navigation"]//a[@data-l="t,userPage"]'
    ANOTHER_ACCOUNT_NAME = '//h1[@class="mctc_name_tx bl"]'

    def select_wall(self):
        Lib.simple_wait_element(self.driver, self.WALL_TOOLBAR).click()
        Lib.visibility_wait_element(self.driver, self.WALL_CONTENT)
        element = Lib.visibility_wait_element(self.driver, self.FEED_LIST)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_nickname(self):
        try:
            element = Lib.simple_wait_element(self.driver, self.ANOTHER_ACCOUNT_NAME)
            return element.text
        except TimeoutException, NoSuchElementException:
            element = Lib.simple_wait_element(self.driver, self.MY_ACCOUNT_NAME)
            return element.text


