from tests.models.Component import Component
from tests.Libs.Lib import Lib
from selenium import webdriver


class CommentClass(Component):
    COMMENT_BUTTON = "//div[@class = 'widget_tx flipthis-highlight']"
    INPUT_TEXT = "//div[@class = 'ok-e js-ok-e add-placeholder add-caret __empty flipthis-highlight']"
    SEND_BUTTON = " //div[@id = 'ok-e-d_button']"
    HOVER_ELEMENT = "//div[@id = 'd-id-cmnt-local--100-rp']"
    LIKE_BUTTON = "//span[@class = 'tico_img ic ic_klass-o flipthis-highlight']"
    COMMENT = "//div[@class = 'feedback_type __left __comment']"

    def create_comment(self):
        Lib.simple_wait_element(self.driver, self.COMMENT_BUTTON).click()
        Lib.simple_set_text_to_element(
            self.driver, self.TEXT_INPUT, "test-test-teeest")
        Lib.simple_wait_element(self.driver, self.SEND_BUTTON).click()

    def add_like(self):
        Lib.hover(self.driver, self.HOVER_ELEMENT)
        Lib.simple_wait_element(self.driver, self.LIKE_BUTTON).click()

    def like_checker(self):
        if Lib.check_exist_element(self.driver, self.LIKE_BUTTON):
            return True
        else:
            return False

    def event_like_checker(self):
        self.driver.get("https://www.ok.ru/marks")
        if Lib.check_exist_element(self.driver, self.COMMENT):
            return True
        else:
            return False
