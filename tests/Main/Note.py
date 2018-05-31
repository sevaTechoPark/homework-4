from random import randint

from tests.Lilbs.Lib import Lib
from tests.models.Component import Component
from tests.models.Page import Page


class NotePage(Page):
    @property
    def page(self):
        return NotePage(self.driver)


class NoteComponent(Component):
    DEFAULT_NOTE_TEXT = "Random note %d %d %d" % (
        randint(0, 100), randint(0, 100), randint(0, 100))
    USER_URL_CSS = '[data-l="t\,selectCurrentUser"]'
    FOCUS_NOTE_CSS = '.posting-form_itx_w .input_placeholder'
    SET_NOTE_TEXT_CSS = "[data-initial-text-to-modify]"
    UPLOAD_NOTE_CSS = "div .posting_f_r div"
    LAST_POST_CSS = "div[class='media-text_cnt']"

    def open_notes(self):
        el = Lib.simple_wait_element_css(self.driver, self.USER_URL_CSS)
        self.driver.get(
            el.get_attribute("href") + '/statuses')

    def focus_note(self):
        el = Lib.simple_wait_element_css(
            self.driver, self.FOCUS_NOTE_CSS)
        el.click()

    def set_note_text(self):
        el = Lib.simple_wait_element_css(
            self.driver, self.SET_NOTE_TEXT_CSS)
        el.send_keys(self.DEFAULT_NOTE_TEXT)

    def upload_note(self):
        el = Lib.simple_wait_element_css(self.driver, self.UPLOAD_NOTE_CSS)
        el.click()

    def get_last_post(self):
        last_post = Lib.simple_wait_element_css(
            self.driver, self.LAST_POST_CSS)
        return last_post.text
