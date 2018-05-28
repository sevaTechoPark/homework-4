from tests.models.Component import Component
from tests.Lilbs.Lib import Lib

class Interview(Component):
    INTERVIEW_BLOCK = "//div[@data-action = 'template_block_poll']"
    BUTTON_ADD = "//span[@class = 'mus-tr_add js-mus-tr_add']"
    QUESTION = "//div[@class = 'itx_w posting_poll_i __question']//descendant::textarea"
    def open_tab(self):
         self.driver.get("https://www.ok.ru/post")
         Lib.simple_wait_element(self.driver, self.INTERVIEW_BLOCK).click()
         
    def input_value(self):
        Lib.visibility_wait_element(self.driver,self.QUESTION)
        Lib.simple_set_text_to_element(self.driver, self.QUESTION,"QA is cool ?")
        Lib.visibility_wait_element(self.driver, "//span[@class = 'mus-trjs-mus-tr_add']")

            # def add_audio(self):
  
    #     before_click =  Lib.visibility_wait_element(self.driver, "//div[@class ='mml_notif mml_notif__num __on']").text
    #     element = Lib.visibility_wait_element(self.driver, self.MUSIC_BLOCK)
    #     Lib.hover(self.driver, element)
    #     Lib.simple_wait_element(self.driver,self.BUTTON_ADD).click()
    #     after_click = Lib.visibility_wait_element(self.driver, "//div[@class ='mml_notif mml_notif__num __on']").text
    #     return (after_click > before_click)
     