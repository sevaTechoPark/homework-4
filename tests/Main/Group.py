from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from tests.Lilbs.Lib import Lib
from tests.models.Component import Component


class GroupComponent(Component):
    DEFAULT_GROUP_SEARCH = "Android"
    SEARCH_BTN_CSS = "input[class='toolbar_search_lupa']"
    FIRST_GROUP_XPATH = "//div[@id='gs_result_list']/div[1]"
    JOIN_BTN_CSS = "span[class='button-pro __sec']"
    ARROW_UNFOLLOW_BTN_CSS = ".__with-arrow"
    UNFOLLOW_CSS = ".__show .dropdown_n"
    SEARCH_QUERY = 'https://ok.ru/search?st.query=%s' % DEFAULT_GROUP_SEARCH

    def fill_search(self):
        search_field = self.driver.find_element_by_id("field_query")
        search_field.send_keys(self.DEFAULT_GROUP_SEARCH)

    def search(self):
        search_btn = self.driver.find_element_by_css_selector(
            self.SEARCH_BTN_CSS)
        self.jsClick(search_btn)

    def follow(self):
        first_group = Lib.simple_wait_element(
            self.driver, self.FIRST_GROUP_XPATH)
        try:
            join_btn = first_group.find_element_by_css_selector(
                self.JOIN_BTN_CSS)
            join_btn.click()
        except NoSuchElementException:
            pass

    def unfollow(self):
        self.driver.get(self.driver.find_element_by_xpath(
            "//div[@id='gs_result_list']/div[1]//a[@title]").get_attribute("href"))
        self.jsClick(self.driver.find_element_by_css_selector(
            self.ARROW_UNFOLLOW_BTN_CSS))
        self.jsClick(
            self.driver.find_element_by_css_selector(self.UNFOLLOW_CSS))

    def getFollowBtn(self):
        self.driver.get(self.SEARCH_QUERY)
        if len(self.driver.find_element_by_xpath(self.FIRST_GROUP_XPATH).find_elements_by_css_selector(self.JOIN_BTN_CSS)) == 0:
            return False
        return True
