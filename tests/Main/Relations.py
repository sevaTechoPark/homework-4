from tests.models.Component import Component
from tests.Libs.Lib import Lib
from selenium import webdriver


class Relations(Component):
    BUTTON_FRIEND = "//a [@class ='toolbar_nav_a toolbar_nav_a__friends']"
    ELSE_BUTTON = "//span[@class = 'mctc_navMenuDropdownSecLabelText flipthis-highlight']"
    CLASSMATES = "//a[@class = 'mctc_navMenuDDLIL flipthis-highlight']"
    BUTTON_CLASSMATES = "//span[@class = 'add-stub_tx flipthis-highlight']"
    CHOOSE_TARGET = "//div[@id = 'hook_InviteChangeCardRel_1320956988']//div[@class = 'avatar user']"
    TARGET = "//input[@class = 'button-pro __disabled']"
    PAGE_FRIEND = "//a[@class='dblock']//descendant::div[@class = 'photo']"
    FRIEND_CLICK = "//span[@class = 'dropdown_ac button-pro __sec __with-arrow flipthis-highlight']"

    def friends_classmates(self):
        Lib.simple_wait_element(self.driver, self.BUTTON_FRIEND).click()
        Lib.simple_wait_element(self.driver, self.ELSE_BUTTON).click()
        Lib.simple_wait_element(self.driver, self.CLASSMATES).click()
        Lib.simple_wait_element(self.driver, self.BUTTON_CLASSMATES).click()
        Lib.simple_wait_element(self.driver, self.CHOOSE_TARGET).click()

    def classmates_checker(self):
        Lib.simple_wait_element(self.driver, self.BUTTON_FRIEND).click()
        Lib.simple_wait_element(self.driver, self.PAGE_FRIEND).click()
        Lib.simple_wait_element(self.driver, self.FRIEND_CLICK).click()
        Lib.hover(self.driver, "//div[@class = 'dropdown_cnt __show']")
        return Lib.check_exist_element(self.driver, "//input[@checked]")
