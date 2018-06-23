from tests.Libs.Lib import Lib
from tests.models.Component import Component
from tests.models.Page import Page


class ThemePage(Page):
    @property
    def page(self):
        return ThemePage(self.driver)


class ThemeComponent(Component):

    CONFIRM_BTN_CSS = '[data-l="t\,confirm"]'
    SELECT_CSS = 'div[class="covers_cat_lst_cnt"'
    SELECTED_THEME_CSS = 'div[class="covers_cat_lst_cnt"] div[class*="selected"]'

    def select(self):
        el = Lib.simple_wait_elements_css(self.driver, self.SELECT_CSS)[2]
        theme = el.find_element_by_css_selector("a")
        theme.click()

    def apply(self):
        el = Lib.simple_wait_element_css(self.driver, self.CONFIRM_BTN_CSS)
        el.click()

    def get_selected_theme(self):
        return self.driver.find_element_by_css_selector(self.SELECTED_THEME_CSS).text.split(
            "\n")[0]
