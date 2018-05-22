from tests.models.Component import Component
from tests.models.Page import Page


class ThemePage(Page):
    @property
    def page(self):
        return ThemePage(self.driver)

class ThemeComponent(Component):

    start_theme_name = ''

    def select(self):
        self.start_theme_name = self.get_selected_theme()
        theme = self.driver.find_elements_by_css_selector('div[class="covers_cat_lst_cnt"')[2].find_element_by_css_selector("a")
        self.jsClick(theme)
    def apply(self):
        self.jsClick(self.driver.find_element_by_css_selector('[data-l="t\,confirm"]'))

    def get_selected_theme(self):
        return self.driver.find_element_by_css_selector('div[class="covers_cat_lst_cnt"] div[class*="selected"]').text.split(
            "\n")[0]
