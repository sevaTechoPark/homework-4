from tests.models.Component import Component
from tests.Libs.Lib import Lib
from selenium import webdriver


class Events(Component):
    NOTIF_BLOCK = "//div [@data-l ='contentType,PHOTO,eventType,COMMENT']//descendant::img"
    BUTTON_MESSAGE = "//div[@class='entity-shortcut-menu_footer-group']//descendant::a[@data-l='t,message']"
    QUESTION = "//div[@class = 'itx_w posting_poll_i __question']//descendant::textarea"
    TEXT_INPUT = "//div[@data-l='t,ta']"
    SEND_TEXT = "//button[@class = 'button-pro comments_add-controls_save']"
    COUNTER_VALUE = "//div[@id = 'counter_ToolbarMessages']//*[contains(text(),'1')]"

    def open_event(self):
        self.driver.get("https://www.ok.ru/marks")

    def send_message(self, message):
        avatar = Lib.simple_wait_element(self.driver, self.NOTIF_BLOCK)
        Lib.hover(self.driver, avatar)
        Lib.simple_wait_element(self.driver, self.BUTTON_MESSAGE).click()
        Lib.simple_set_text_to_element(self.driver, self.TEXT_INPUT, message)
        Lib.simple_wait_element(self.driver, self.SEND_TEXT).click()

    def mr_checker(self):
        return Lib.check_exist_element(self.driver, self.COUNTER_VALUE)
