from tests.models.Component import Component
from tests.models.Page import Page


class AuthPage(Page):
    @property
    def page(self):
        return AuthPage(self.driver)

class AuthForm(Component):

    email_field = '/html//input[@id="field_email"]'
    password_field = '/html//input[@id="field_password"]'
    login_btn = '[value="Log in"]'

    def fillEmail(self,email):
        self.driver.find_element_by_xpath(self.email_field).send_keys(email)

    def fillPassword(self,password):
        self.driver.find_element_by_xpath(self.password_field).send_keys(password)

    def submit(self):
        submit_btn = self.driver.find_element_by_css_selector(self.login_btn)
        self.jsClick(submit_btn)