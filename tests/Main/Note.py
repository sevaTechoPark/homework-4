from random import randint

from tests.models.Component import Component
from tests.models.Page import Page


class NotePage(Page):
    @property
    def page(self):
        return NotePage(self.driver)

class NoteComponent(Component):
    default_note_text = "Random note %d %d %d" % (randint(0,100),randint(0,100),randint(0,100))
    user_url_css = '[data-l="t\,selectCurrentUser"]'

    def open_notes(self):
        self.driver.get(
            self.driver.find_element_by_css_selector(self.user_url_css).get_attribute("href") + '/statuses')

    def focus_note(self):
        self.jsClick(self.driver.find_element_by_css_selector('.posting-form_itx_w .input_placeholder'))

    def set_note_text(self):
        self.driver.find_element_by_css_selector("[data-initial-text-to-modify]").send_keys(self.default_note_text)

    def upload_note(self):
        self.jsClick(self.driver.find_element_by_css_selector("div .posting_f_r div"))
        self.driver.find_elements_by_css_selector("div")
