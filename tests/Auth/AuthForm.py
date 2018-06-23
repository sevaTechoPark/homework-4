import os


from tests.Libs.Lib import Lib
from tests.models.Component import Component


class AuthForm(Component):
    LOGIN_INPUT = '//input[@name="st.email"]'
    PASSWORD_INPUT = '//input[@name="st.password"]'
    SUBMIT_INPUT = '//input[@data-l="t,sign_in"]'

    LOGIN1 = os.environ.get('LOGIN1')
    PASSWORD1 = os.environ.get('PASSWORD1')
    LOGIN2 = os.environ.get('LOGIN2')
    PASSWORD2 = os.environ.get('PASSWORD2')

    def set_login(self, login):
        Lib.simple_set_text_to_element(self.driver, self.LOGIN_INPUT, login)

    def set_password(self, password):
        Lib.simple_set_text_to_element(
            self.driver, self.PASSWORD_INPUT, password)

    def submit(self):
        Lib.simple_get_element(self.driver, self.SUBMIT_INPUT).click()

    def authorized(self, who=True):
        Lib.simple_wait_element(self.driver, self.LOGIN_INPUT)

        if who:
            self.set_login(self.LOGIN1)
            self.set_password(self.PASSWORD1)
        else:
            self.set_login(self.LOGIN2)
            self.set_password(self.PASSWORD2)
        self.submit()
