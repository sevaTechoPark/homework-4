import os

from tests.Libs.Lib import Lib
from tests.models.Component import Component
from tests.models.Page import Page


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)


class AuthForm(Component):
    LOGIN_INPUT = '//input[@name="st.email"]'
    PASSWORD_INPUT = '//input[@name="st.password"]'
    SUBMIT_INPUT = '//input[@data-l="t,sign_in"]'

    LOGIN1 = os.environ.get('LOGIN1')
    PASSWORD1 = os.environ.get('PASSWORD1')
    TOOLBARS_CSS = '.toolbar_dropdown'

    def set_login(self):
        Lib.simple_set_text_to_element(
            self.driver, self.LOGIN_INPUT, self.LOGIN1)

    def set_password(self):
        Lib.simple_set_text_to_element(
            self.driver, self.PASSWORD_INPUT, self.PASSWORD1)

    def submit(self):
        Lib.simple_get_element(self.driver, self.SUBMIT_INPUT).click()

    def isAuth(self):
        toolbars = self.driver.find_elements_by_css_selector(
            self.TOOLBARS_CSS).__len__()
        return (len(toolbars) > 0)
