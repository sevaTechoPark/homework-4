from tests.Lilbs.Lib import Lib
from tests.models.Component import Component
from tests.models.Page import Page


class MessagePage(Page):
    @property
    def page(self):
        return MessagePage(driver=self.driver)


class MessageComponent(Component):
    default_message = "KEK!"
    first_dialog_css = '[data-l] .h-mod:nth-of-type(1) .chats_i_ovr'
    send_btn_css = "button[class='button-pro comments_add-controls_save']"
    message_field_css = '[data-check-attach-on-submit="true"] [contenteditable]'
    dialog_id = ''

    def selectFirstDialog(self):
        el = Lib.simple_wait_element_css(self.driver, self.first_dialog_css)
        self.jsClick(el)
        self.dialog_id = el.get_attribute('href').split("/")[-1]

    def writeMessage(self):
        message_field = Lib.simple_wait_element_css(
            self.driver, self.message_field_css)
        message_field.send_keys(self.default_message)

    def send_message(self):
        el = Lib.simple_wait_element_css(self.driver, self.send_btn_css)
        self.jsClick(el)

    def open_dialog(self):
        self.driver.get("https://ok.ru/messages/%s" % self.dialog_id)

    def get_last_message(self):
        el = Lib.simple_wait_elements_css(self.driver, '.js-msg-text')
        return el[-1].text
