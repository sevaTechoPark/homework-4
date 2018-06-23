from tests.Libs.Lib import Lib
from tests.models.Component import Component
from tests.models.Page import Page


class MessagePage(Page):
    @property
    def page(self):
        return MessagePage(driver=self.driver)


class MessageComponent(Component):
    DEFAULT_MESSAGE = "KEK!"
    FIRST_DIALOG_CSS = '[data-l] .h-mod:nth-of-type(1) .chats_i_ovr'
    SEND_BTN_CSS = "button[class='button-pro comments_add-controls_save']"
    MESSAGE_FIELD_CSS = '[data-check-attach-on-submit="true"] [contenteditable]'
    dialog_id = ''
    MESSAGES_URL = "https://ok.ru/messages/%s"
    LAST_MESSAGE_CSS = '.js-msg-text'

    def selectFirstDialog(self):
        el = Lib.simple_wait_element_css(self.driver, self.FIRST_DIALOG_CSS)
        el.click()
        self.dialog_id = el.get_attribute('href').split("/")[-1]

    def writeMessage(self):
        message_field = Lib.simple_wait_element_css(
            self.driver, self.MESSAGE_FIELD_CSS)
        message_field.send_keys(self.DEFAULT_MESSAGE)

    def send_message(self):
        el = Lib.simple_wait_element_css(self.driver, self.SEND_BTN_CSS)
        el.click()

    def open_dialog(self):
        self.driver.get(self.MESSAGES_URL % self.dialog_id)

    def get_last_message(self):
        el = Lib.simple_wait_elements_css(self.driver, self.LAST_MESSAGE_CSS)
        return el[-1].text
