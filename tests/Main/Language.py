from tests.models.Component import Component
from tests.models.Page import Page


class LanguagePage(Page):
    @property
    def page(self):
        return LanguagePage(self.driver)

class LanguageForm(Component):
    language_element_css = '.user-settings .user-settings_i:nth-of-type(6) .user-settings_i_lk'
    inactive_language = ".sel-lang_list a"

    def open(self):

        changeBtn = self.driver.find_element_by_css_selector(self.language_element_css)
        self.driver.execute_script("arguments[0].style.visibility = 'visible';",
                                   changeBtn)
        self.jsClick(changeBtn)

    def get_inactive_language(self):
        return self.driver.find_element_by_css_selector(self.inactive_language).text

    def change(self):
        self.jsClick(self.driver.find_element_by_css_selector(self.inactive_language))
