from tests.models.Component import Component
from tests.Libs.Lib import Lib
from selenium import webdriver


class BlackList(Component):
    BUTTON_FRIEND = "//a [@class ='toolbar_nav_a toolbar_nav_a__friends']"
    PAGE_FRIEND = "//a[@class='dblock']//descendant::div[@class = 'photo']"
    MENU_CLICK = "//em[@class ='tico_simb_txt flipthis-highlight']"
    COMPLAIN_BUTTON = "//span[@class = 'tico flipthis-highlight']"
    BLACKLIST = "//input[@name = 'st.layer.addToBlackList']"
    MR_SENDER = "//input[@data-l = 't,confirm']"
    MAN_IN_BLACKLIST = "//img[@class = 'photo_img flipthis-highlight']"

    def open_friend_page(self):
        Lib.simple_wait_element(self.driver, self.BUTTON_FRIEND).click()
        Lib.simple_wait_element(self.driver, self.PAGE_FRIEND).click()

    def blacklist_choose(self):
        Lib.simple_wait_element(self.driver, self.MENU_CLICK).click()
        Lib.simple_wait_element(self.driver, self.COMPLAIN_BUTTON).click()
        Lib.visibility_wait_element(self.driver, self.BLACKLIST)
        Lib.simple_wait_element(self.driver, self.BLACKLIST).click()
        Lib.simple_wait_element(self.driver, self.MR_SENDER).click()

    def check_in_blacklist(self):
        self.driver.get("https://www.ok.ru/blacklist")
        return Lib.check_exist_element(self.driver, self.MAN_IN_BLACKLIST)
