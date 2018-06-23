import os

from selenium.common.exceptions import NoSuchElementException

from tests.Libs.Lib import Lib
from tests.models.Component import Component
import odnoklassniki


class GroupComponent(Component):
    DEFAULT_GROUP_SEARCH = "Android"
    DEFAULT_GROUP_ID = "54499418374389"
    SEARCH_BTN_CSS = "input[class='toolbar_search_lupa']"
    FIRST_GROUP_XPATH = "//div[@id='gs_result_list']/div[1]"
    JOIN_BTN_CSS = "span[class='button-pro __sec']"
    ARROW_UNFOLLOW_BTN_CSS = ".__with-arrow"
    UNFOLLOW_CSS = ".__show .dropdown_n"
    SEARCH_QUERY = 'https://ok.ru/search?st.query=%s' % DEFAULT_GROUP_SEARCH
    URL_CSS = "//div[@id='gs_result_list']//a[@title]"
    SEARCH_FIELD_ID = "field_query"

    def fill_search(self):
        search_field = self.driver.find_element_by_id(self.SEARCH_FIELD_ID)
        search_field.send_keys(self.DEFAULT_GROUP_SEARCH)

    def search(self):
        search_btn = Lib.simple_wait_element_css(
            self.driver, self.SEARCH_BTN_CSS)
        search_btn.click()

    def follow(self):
        first_group = Lib.simple_wait_element(
            self.driver, self.FIRST_GROUP_XPATH)
        if not self.checkFollow():
            join_btn = first_group.find_element_by_css_selector(
                self.JOIN_BTN_CSS)
            join_btn.click()

    def unfollow(self):
        url = Lib.simple_wait_element(
            self.driver, self.URL_CSS)
        self.driver.get(url.get_attribute('href'))
        unfollow_arrow_btn = Lib.simple_wait_element_css(
            self.driver, self.ARROW_UNFOLLOW_BTN_CSS)
        unfollow_arrow_btn.click()
        unfollow_btn = Lib.simple_wait_element_css(
            self.driver, self.UNFOLLOW_CSS)
        unfollow_btn.click()

    def getFollowBtn(self):
        self.driver.get(self.SEARCH_QUERY)
        el = self.driver.find_element_by_xpath(self.FIRST_GROUP_XPATH)
        if len(el.find_elements_by_css_selector(self.JOIN_BTN_CSS)) == 0:
            return False
        return True

    def checkFollow(self):

        CLIENT_KEY = os.environ.get('CLIENT_KEY')
        CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
        ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
        isFollowed = False

        ok = odnoklassniki.Odnoklassniki(
            CLIENT_KEY, CLIENT_SECRET, ACCESS_TOKEN)
        groups = ok.group.getUserGroupsV2()['groups']
        for group in groups:
            if group['groupId'] == self.DEFAULT_GROUP_ID:
                isFollowed = True
                break
        return isFollowed
