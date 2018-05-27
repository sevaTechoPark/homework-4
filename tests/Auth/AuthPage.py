from tests.Auth.AuthForm import AuthForm
from tests.models.Page import Page


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)
