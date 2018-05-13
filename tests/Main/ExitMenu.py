# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait

from tests.constants.Constants import waitTime
from tests.models.Component import Component


class ExitMenu(Component):
    TOOLBAR_EXIT_MENU = '//*[@id="hook_Block_ToolbarUserDropdown"]/div/div[1]'
    EXIT_MENU = '//*[@id="hook_Block_ToolbarUserDropdown"]/div/div[2]/div/div[1]'
    LOG_OUT = '//*[@id="hook_Block_ToolbarUserDropdown"]/div/div[2]/div/div[1]/div[1]/a'
    EXIT_MENU_SUBMIT = '//*[@id="hook_Modal_popLayerModal"]/div[2]/div[1]/div'
    LOG_OUT_SUBMIT = '//*[@id="hook_FormButton_logoff.confirm_not_decorate"]'

    def log_out(self):
        self.driver.find_element_by_xpath(self.TOOLBAR_EXIT_MENU).click()
        WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.EXIT_MENU)
        )
        self.driver.find_element_by_xpath(self.LOG_OUT).click()
        WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.EXIT_MENU_SUBMIT)
        )
        self.driver.find_element_by_xpath(self.LOG_OUT_SUBMIT).click()


