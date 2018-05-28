from tests.models.Component import Component
from tests.Lilbs.Lib import Lib

class AudioAdd(Component):
    MUSIC_BLOCK = "//div[@class = 'mus-tr_hld']//div[@class ='mus-tr_right-controls foh-s']"
    BUTTON_ADD = "//span[@class = 'mus-tr_add js-mus-tr_add']"
 
    def open_audio(self):
        self.driver.get("https://www.ok.ru/music")
    
    def add_audio(self):
  
        before_click =  Lib.visibility_wait_element(self.driver, "//div[@class ='mml_notif mml_notif__num __on']").text
        element = Lib.visibility_wait_element(self.driver, self.MUSIC_BLOCK)
        Lib.hover(self.driver, element)
        Lib.simple_wait_element(self.driver,self.BUTTON_ADD).click()
        after_click = Lib.visibility_wait_element(self.driver, "//div[@class ='mml_notif mml_notif__num __on']").text
        return (after_click > before_click)
     