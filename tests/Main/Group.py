from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from tests.Lilbs.Lib import Lib
from tests.models.Component import Component


class GroupComponent(Component):
    default_group_search = "Android"
    search_field_id = "field_query"
    search_btn_css = "input[class='toolbar_search_lupa']"
    first_group_xpath = "//div[@id='gs_result_list']/div[1]"
    group_link_xpath = "//div[@id='gs_result_list']/div[1]//a[@title]"
    join_btn_css = "span[class='button-pro __sec']"
    arrow_unfollow_btn_css = ".__with-arrow"
    unfollow_css = ".__show .dropdown_n"
    search_query = 'https://ok.ru/search?st.query=%s' % default_group_search

    def fill_search(self):
        search_field = self.driver.find_element_by_id("field_query")
        search_field.send_keys(self.default_group_search)

    def search(self):
        search_btn = self.driver.find_element_by_css_selector(
            self.search_btn_css)
        self.jsClick(search_btn)

    def follow(self):
        first_group = Lib.simple_wait_element(
            self.driver, self.first_group_xpath)
        try:
            join_btn = first_group.find_element_by_css_selector(
                self.join_btn_css)
            join_btn.click()
        except NoSuchElementException:
            pass

    def unfollow(self):
        self.driver.get(self.driver.find_element_by_xpath(
            "//div[@id='gs_result_list']/div[1]//a[@title]").get_attribute("href"))
        self.jsClick(self.driver.find_element_by_css_selector(
            self.arrow_unfollow_btn_css))
        self.jsClick(
            self.driver.find_element_by_css_selector(self.unfollow_css))

    def getFollowBtn(self):
        self.driver.get(self.search_query)
        if len(self.driver.find_element_by_xpath(self.first_group_xpath).find_elements_by_css_selector(self.join_btn_css)) == 0:
            return False
        return True
