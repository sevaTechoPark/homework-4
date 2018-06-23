from tests.models.Component import Component
from tests.Libs.Lib import Lib


class AddMusic(Component):
    ADD_BUTTON = "//div[@class = 'mus_card_ac_i mus_card_ac_i__add flipthis-highlight']"
    HOVER_BLOCK = "//div[@class = 'mus_card_img_w mus_card_img_w__col']"
    VISIBLE_PLAYLISTS = "//ul[@class='mml_subcat_ul __inner mus_playlist_lst mus_playlist_lst__on']"

    def open_music(self):
        self.driver.get("https://www.ok.ru/music/collections")

    def add_playlist(self):
        Lib.hover(self.driver, self.HOVER_BLOCK)
        Lib.visibility_wait_element(self.driver, self.ADD_BUTTON)
        Lib.simple_wait_element(self.driver, self.ADD_BUTTON).click()

    def check_music(self):
        return Lib.check_exist_element(self.driver, self.VISIBLE_PLAYLISTS)
