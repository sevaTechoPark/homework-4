from random import randint

from tests.Lilbs.Lib import Lib
from tests.models.Component import Component
from tests.models.Page import Page


class NotePage(Page):
    @property
    def page(self):
        return NotePage(self.driver)


class NoteComponent(Component):
    default_note_text = "Random note %d %d %d" % (
        randint(0, 100), randint(0, 100), randint(0, 100))
    user_url_css = '[data-l="t\,selectCurrentUser"]'

    def open_notes(self):
        el = Lib.simple_wait_element_css(self.driver, self.user_url_css)
        self.driver.get(
            el.get_attribute("href") + '/statuses')

    def focus_note(self):
        el = Lib.simple_wait_element_css(
            self.driver, '.posting-form_itx_w .input_placeholder')
        self.jsClick(el)

    def set_note_text(self):
        el = Lib.simple_wait_element_css(
            self.driver, "[data-initial-text-to-modify]")
        el.send_keys(self.default_note_text)

    def upload_note(self):
        el = Lib.simple_wait_element_css(self.driver, "div .posting_f_r div")
        self.jsClick(el)

    def get_last_post(self):
        last_post = Lib.simple_wait_element_css(
            self.driver, "div[class='media-text_cnt']")
        return last_post.text
