from tests.Main.ExitMenu import ExitMenu
from tests.Main.TopMenu import TopMenu
from tests.models.Page import Page


class MainPage(Page):
    PATH = ''

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def exit_menu(self):
        return ExitMenu(self.driver)

