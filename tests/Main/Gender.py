from selenium.webdriver.support.wait import WebDriverWait

from tests.models.Component import Component
from tests.Lilbs.Lib import Lib


class GenderComponent(Component):

    PROFILE_CSS = '[data-l="t\,selectCurrentUser"]'
    EDIT_BTN_CSS = 'div[class="user-profile_i_value"] a[class="user-profile_lk-o"]'
    START_GENDER = -1

    def open_profile(self):
        self.driver.get(
            self.driver.find_element_by_css_selector(self.PROFILE_CSS).get_attribute("href") + '/about')

    def click_edit(self):
        self.jsClick(
            self.driver.find_element_by_css_selector(self.EDIT_BTN_CSS))

    def set_start_gender(self):

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id("field_gender_1"))
        isChecked = self.driver.execute_script(
            'return document.getElementById("field_gender_1").checked')
        if isChecked:
            self.START_GENDER = 1
        else:
            self.START_GENDER = 2

    def get_current_gender(self):
        self.click_edit()
        Lib.simple_wait_element_css(self.driver, '#field_gender_1')
        isChecked = self.driver.execute_script(
            'return document.getElementById("field_gender_1").checked')
        cur_gender = -1
        if isChecked:
            cur_gender = 1
        else:
            cur_gender = 2
        return cur_gender != self.START_GENDER

    def change_gender(self):
        new_gender = -1
        if self.START_GENDER == 1:
            new_gender = 2
        else:
            new_gender = 1
        _id = "field_gender_%d" % new_gender
        self.driver.execute_script(
            "document.getElementById('%s').checked = true" % _id)

    def save(self):
        self.jsClick(self.driver.find_element_by_css_selector(
            '[data-l="t\,confirm"]'))
        el = Lib.simple_wait_element_css(
            self.driver, css='#buttonId_button_close')
        self.jsClick(el)
