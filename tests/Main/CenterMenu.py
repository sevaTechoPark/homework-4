from tests.Libs.Lib import Lib
from tests.models.Component import Component


class CenterMenu(Component):
    WALL_TOOLBAR = '//div[@data-l="t,navigation"]//a[@data-l="t,userPage"]'
    WALL_CONTENT = '//div[@id="hook_Block_UserFeed"]//div[contains(@data-l, "feedLocation,self,")]'
    FEED_LIST = '//div[@class="feed-list"][@data-l="feedLocation,self"]'
    ANOTHER_ACCOUNT_NAME = '//h1[@class="mctc_name_tx bl"]'

    def select_wall(self):
        element = Lib.visibility_wait_element(self.driver, self.FEED_LIST)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_nickname(self):
        return Lib.simple_wait_element(self.driver, self.WALL_TOOLBAR).text

    def get_another_nickname(self):
        return Lib.simple_wait_element(self.driver, self.ANOTHER_ACCOUNT_NAME).text
