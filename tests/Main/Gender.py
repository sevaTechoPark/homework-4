from selenium.webdriver.support.wait import WebDriverWait

from tests.models.Component import Component
from tests.Libs.Lib import Lib


class GenderComponent(Component):

    PROFILE_CSS = '[data-l="t\,selectCurrentUser"]'
    EDIT_BTN_CSS = 'div[class="user-profile_i_value"] a[class="user-profile_lk-o"]'
    START_GENDER = -1
    BTN_CONFIRM_CSS = '[data-l="t\,confirm"]'
    BTN_CLOSE_CSS = '#buttonId_button_close'

    def open_profile(self):
        self.driver.get(
            self.driver.find_element_by_css_selector(self.PROFILE_CSS).get_attribute("href") + '/about')

    def click_edit(self):
        el = Lib.simple_wait_element_css(self.driver, self.EDIT_BTN_CSS)
        el.click()

    def set_start_gender(self):
        self.START_GENDER = self.get_current_gender()

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
        return cur_gender

    def change_gender(self):
        new_gender = -1
        if self.START_GENDER == 1:
            new_gender = 2
        else:
            new_gender = 1
        _id = "field_gender_%d" % new_gender
        gender_radio = Lib.simple_wait_element_css(
            self.driver, "input[id='%s']" % _id)
        gender_radio.click()

    def save(self):
        btn_confirm = Lib.simple_wait_element_css(
            self.driver, self.BTN_CONFIRM_CSS)
        btn_confirm.click()
        btn_close = Lib.simple_wait_element_css(
            self.driver, self.BTN_CLOSE_CSS)
        btn_close.click()

    def back_to_start_gender(self):
        self.open_profile()
        current_id = self.get_current_gender()
        _id = 1
        if current_id == 1:
            _id = 2
        Lib.simple_wait_element_css(
            self.driver, "input[id='field_gender_%d']" % _id).click()
