from tests.Lilbs.Lib import Lib
from tests.models.Component import Component
from tests.models.Page import Page


class LanguagePage(Page):
    @property
    def page(self):
        return LanguagePage(self.driver)


class LanguageForm(Component):
    LANGUAGE_ELEMENT_CSS = '.user-settings .user-settings_i:nth-of-type(6) .user-settings_i_lk'
    INACTIVE_LANGUAGE = ".sel-lang_list a"

    def open(self):

        changeBtn = self.driver.find_element_by_css_selector(
            self.LANGUAGE_ELEMENT_CSS)
        # self.driver.execute_script("arguments[0].style.visibility = 'visible';",
        #                            changeBtn)
        self.jsClick(changeBtn)

    def get_inactive_language(self):
        el = Lib.simple_wait_element_css(self.driver, self.INACTIVE_LANGUAGE)
        return el.text

    def change(self):
        el = Lib.simple_wait_element_css(self.driver, self.INACTIVE_LANGUAGE)
        self.jsClick(el)
