from tests.models.Component import Component
from tests.Lilbs.Lib import Lib
from selenium import webdriver

class Relations(Component):
    BUTTON_FRIEND = "//a [@class ='toolbar_nav_a toolbar_nav_a__friends']"
    ELSE_BUTTON = "//span[@class = 'mctc_navMenuDropdownSecLabelText flipthis-highlight']"
    CLASSMATES = "//a[@class = 'mctc_navMenuDDLIL flipthis-highlight']"
    BUTTON_CLASSMATES = "//span[@class = 'add-stub_tx flipthis-highlight']"

    def friends_classmates(self):
        Lib.simple_wait_element(self.driver,self.BUTTON_FRIEND).click()
        Lib.simple_wait_element(self.driver,self.ELSE_BUTTON ).click()
        Lib.simple_wait_element(self.driver,self.CLASSMATES ).click()
        Lib.simple_wait_element(self.driver,self.BUTTON_CLASSMATES ).click()


    def blacklist_choose(self):
        Lib.simple_wait_element(self.driver,self.MENU_CLICK).click()
        Lib.simple_wait_element(self.driver,self.COMPLAIN_BUTTON).click()
        Lib.visibility_wait_element(self.driver, self.BLACKLIST)
        Lib.simple_wait_element(self.driver,self.BLACKLIST).click()
        Lib.simple_wait_element(self.driver,self.MR_SENDER).click()

    def check_in_blacklist(self):
        self.driver.get("https://www.ok.ru/blacklist")
        return Lib.check_exist_element(self.driver, self.MAN_IN_BLACKLIST)