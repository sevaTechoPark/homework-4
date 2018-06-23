from tests.models.Component import Component
from tests.Libs.Lib import Lib


class CreateChanel(Component):
    BUTTON_ADD = "//a[@class = 'ml-4x tico wl']"
    INPUT_BLOCK = "//div[@class= 'it_w it_w__3gc']//descendant::input"
    SUBMIT_BUTTON = "//input[@class= 'vl_btn']"
    DELETE_BUTTON = "//div[@class = 'flipthis-wrapper']//descendant::a"
    CHECK_VALUE = "//li[@class ='mml_subcat_li js-droppable ui-droppable']"

    def open_chanel(self):
        self.driver.get("https://www.ok.ru/video/myVideo")

    def before_chanel(self):
        before_create = len(
            self.driver.find_elements_by_xpath(self.CHECK_VALUE))
        return before_create

    def chanel_name(self, name):
        before_click = len(
            self.driver.find_elements_by_xpath(self.CHECK_VALUE))
        Lib.simple_wait_element(self.driver, self.BUTTON_ADD).click()
        Lib.visibility_wait_element(self.driver, self.INPUT_BLOCK)
        Lib.simple_set_text_to_element(self.driver, self.INPUT_BLOCK, name)
        Lib.simple_wait_element(self.driver, self.SUBMIT_BUTTON).click()

    def after_chanel(self):
        after_create = len(
            self.driver.find_elements_by_xpath(self.CHECK_VALUE))
        return after_create

    def delete_clicker(self):
        Lib.simple_wait_element(self.driver, self.DELETE_BUTTON).click()

    def value_check(self):
        return len(self.driver.find_elements_by_xpath(self.CHECK_VALUE))
