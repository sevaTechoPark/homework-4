from tests.models.Component import Component
from tests.models.Page import Page


class MessagePage(Page):
    @property
    def page(self):
        return MessagePage(driver=self.driver)

class MessageComponent(Component):
    default_message = "KEK!"
    first_dialog_css = '[data-l] .h-mod:nth-of-type(1) .chats_i_ovr'
    send_btn_css = '[title="Send"]'
    message_field_css = '[data-check-attach-on-submit="true"] [contenteditable]'
    dialog_id = ''

    def selectFirstDialog(self):
        self.jsClick(self.driver.find_element_by_css_selector(self.first_dialog_css))
        self.dialog_id = self.driver.find_element_by_css_selector(self.first_dialog_css).get_attribute('href').split("/")[-1]

    def writeMessage(self):
        self.driver.find_element_by_css_selector(self.message_field_css).send_keys(self.default_message)

    def send_message(self):
        self.jsClick(self.driver.find_element_by_css_selector(self.send_btn_css))

    def open_dialog(self):
        self.driver.get("https://ok.ru/messages/%s" % self.dialog_id)

    def get_last_message(self):
        messages = self.driver.find_elements_by_css_selector('.js-msg-text')
        return messages[-1].text