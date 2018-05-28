from tests.Lilbs.Lib import Lib
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
    DIALOG_ID = ''

    def selectFirstDialog(self):
        el = Lib.simple_wait_element_css(self.driver, self.FIRST_DIALOG_CSS)
        self.jsClick(el)
        self.DIALOG_ID = el.get_attribute('href').split("/")[-1]

    def writeMessage(self):
        message_field = Lib.simple_wait_element_css(
            self.driver, self.MESSAGE_FIELD_CSS)
        message_field.send_keys(self.DEFAULT_MESSAGE)

    def send_message(self):
        el = Lib.simple_wait_element_css(self.driver, self.SEND_BTN_CSS)
        self.jsClick(el)

    def open_dialog(self):
        self.driver.get("https://ok.ru/messages/%s" % self.DIALOG_ID)

    def get_last_message(self):
        el = Lib.simple_wait_elements_css(self.driver, '.js-msg-text')
        return el[-1].text
