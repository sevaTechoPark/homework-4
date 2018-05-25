from selenium.webdriver.support.wait import WebDriverWait

from tests.models.Component import Component


class GenderComponent(Component):

    new_first_name = 'Vasiliy'
    profile_css = '[data-l="t\,selectCurrentUser"]'
    edit_btn_css = 'div[class="user-profile_i_value"] a[class="user-profile_lk-o"]'
    start_gender = -1

    def open_profile(self):
        self.driver.get(
            self.driver.find_element_by_css_selector(self.profile_css).get_attribute("href") + '/about')

    def click_edit(self):
        self.jsClick(
            self.driver.find_element_by_css_selector(self.edit_btn_css))
        self.set_start_gender()

    def set_start_gender(self):

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_id("field_gender_1"))
        isChecked = self.driver.execute_script('return document.getElementById("field_gender_1").checked')
        if isChecked:
            self.start_gender = 1
        else: self.start_gender = 2

    def change_gender(self):
        new_gender = -1
        if self.start_gender == 1:
            new_gender = 2
        else: new_gender = 1
        _id = "field_gender_%d" % new_gender
        self.driver.execute_script("document.getElementById('%s').checked = true" % _id)

    def save(self):
        self.jsClick(self.driver.find_element_by_css_selector('[data-l="t\,confirm"]'))
        self.jsClick(self.driver.find_element_by_css_selector('#buttonId_button_close'))