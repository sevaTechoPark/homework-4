from tests.Main.Feed import Feed
from tests.Main.TopMenu import TopMenu
from tests.models.Page import Page


class MainPage(Page):
    PATH = ''

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def feed(self):
        return Feed(self.driver)
