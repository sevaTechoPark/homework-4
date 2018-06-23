#! /usr/bin/env python
# -*- coding: utf-8 -*-

from tests.models.Component import Component
from tests.Libs.Lib import Lib
from selenium import webdriver


class Share(Component):
    COMMENT_CLICK = "//div[@class = 'widget_tx flipthis-highlight']"
    INPUT_TEXT = "//div[@class = 'ok-e js-ok-e add-placeholder add-caret __empty flipthis-highlight']"
    TEXT_INPUT = "What is the better than Qa ?"
    MR_SEND = " //div[@id = 'ok-e-d_button']"
    GROUP_BUTTON = "//div[@id = 'd-id-cmnt-local--100-rp']"
    SHARE_BUTTON = "//div[@class='u-menu_tx flipthis-highlight']"
    PROFILE = "//span[@class = 'tico flipthis-highlight']"

    def make_share(self, share_comment):
        Lib.simple_wait_element(self.driver, self.COMMENT_CLICK).click()
        Lib.simple_set_text_to_element(
            self.driver, self.INPUT_TEXT, share_comment)
        Lib.simple_wait_element(self.driver, self.MR_SEND).click()
        Lib.hover(self.driver, self.GROUP_BUTTON)
        share_element = self.driver.find_element_by_link_text("Поделиться")
        Lib.simple_wait_element(self.driver, share_element).click()
        Lib.simple_wait_element(self.driver, self.SHARE_BUTTON).click()

    def share_checker(self, share_comment):
        Lib.simple_wait_element(self.driver, self.PROFILE).click()
        check_share = self.driver.find_element_by_link_text(self.share_comment)
        return Lib.check_exist_element(self.driver, check_share)
