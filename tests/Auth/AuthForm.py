# coding=utf-8
import os

from selenium.webdriver.support.wait import WebDriverWait

from tests.constants.Constants import waitTime
from tests.models.Component import Component


class AuthForm(Component):
    LOGIN_INPUT = '//input[@name="st.email"]'
    PASSWORD_INPUT = '//input[@name="st.password"]'
    SUBMIT_INPUT = '//input[@value="Войти"]'

    LOGIN1 = os.environ['LOGIN1']
    PASSWORD1 = os.environ['PASSWORD1']
    LOGIN2 = os.environ['LOGIN2']
    PASSWORD2 = os.environ['PASSWORD2']

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN_INPUT).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT_INPUT).click()

    def authorized(self, who=True):
        WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.LOGIN_INPUT)
        )

        if who:
            self.set_login(self.LOGIN1)
            self.set_password(self.PASSWORD1)
        else:
            self.set_login(self.LOGIN2)
            self.set_password(self.PASSWORD2)
        self.submit()
