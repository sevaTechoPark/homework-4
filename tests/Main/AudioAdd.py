from tests.models.Component import Component
from tests.Libs.Lib import Lib


class AudioAdd(Component):
    MUSIC_BLOCK = "//div[@class = 'mus-tr_hld']//div[@class ='mus-tr_right-controls foh-s']"
    BUTTON_ADD = "//span[@class = 'mus-tr_add js-mus-tr_add']"
    MUSIC_NUMBER = "//div[@class ='mml_notif mml_notif__num __on']"

    def open_audio(self):
        self.driver.get("https://www.ok.ru/music")

    def before_click(self):
        before_number = Lib.visibility_wait_element(
            self.driver, self.MUSIC_NUMBER).text
        return before_number

    def after_click(self):
        element = Lib.visibility_wait_element(self.driver, self.MUSIC_BLOCK)
        Lib.hover(self.driver, element)
        Lib.simple_wait_element(self.driver, self.BUTTON_ADD).click()
        after_number = Lib.visibility_wait_element(
            self.driver, self.MUSIC_NUMBER).text
        return after_number
