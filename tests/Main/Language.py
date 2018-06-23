# coding=utf-8
from tests.Libs.Lib import Lib
from tests.models.Component import Component
from tests.models.Page import Page


class LanguagePage(Page):
    @property
    def page(self):
        return LanguagePage(self.driver)


class LanguageForm(Component):
    LANGUAGE_ELEMENT_CSS = '.user-settings_i:nth-of-type(6) .user-settings_i_lk'
    INACTIVE_LANGUAGE = ".sel-lang_list a"
    ACTIVE_LANGUAGE = '.user-settings_i:nth-of-type(6) .user-settings_i_tx'

    def open(self):
        changeBtn = Lib.simple_wait_element_css(
            self.driver, self.LANGUAGE_ELEMENT_CSS)
        self.jsClick(changeBtn)  # Здесь он нужен

    def get_inactive_language(self):
        el = Lib.simple_wait_element_css(self.driver, self.INACTIVE_LANGUAGE)
        return el.text

    def get_active_language(self):
        el = Lib.simple_wait_element_css(self.driver, self.ACTIVE_LANGUAGE)
        return el.text

    def change(self):
        el = Lib.simple_wait_element_css(self.driver, self.INACTIVE_LANGUAGE)
        el.click()
