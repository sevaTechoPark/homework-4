# coding=utf-8
from selenium.common.exceptions import TimeoutException

from tests.Libs.Lib import Lib
from tests.models.Component import Component


class TopMenu(Component):
    NOTIFICATION_TOOLBAR = '//ul[@class="toolbar_nav"]//li[@data-l="t,notifications"]'
    FRIENDS_TOOLBAR = '//ul[@class="toolbar_nav"]//li[@data-l="t,friends"]'

    NOTIFICATION_CONTAINER = '//div[@class="notifs_cnt"]'
    NOTIFICATION_TAB_TITLE = '//*[@id="hook_Block_NotificationsLayerTitle"]/div'
    NOTIFICATION_TAB_CONTENT = '//*[@id="hook_Block_NotificationsLayerContent"]'

    NOTIFICATION_ELEMENT = '//div[@id="ntf_layer_content_inner"]/div[position() = 1]'
    NOTIFICATION_ELEMENT_WITH_ID = NOTIFICATION_ELEMENT + '/div'
    NOTIFICATION_REPORT = '//div[@class="notif_ac fade-on-hover"]//i[@data-l="t,spam"]'
    NOTIFICATION_REPORT_SPAM = '//div[@class="notif_ac fade-on-hover"]//div[@data-l="t,shortcutMenu"]//a'
    NOTIFICATION_REMOVED = '//div[@data-module="NotificationRemoved"]'

    NOTIFICATION_BUTTON_CLOSE = '//button[@data-l="t,btn_ignore"]'

    NOTIFICATION_TABS = ['//*[@id="ntf_layer_menu_link_All"]/span',
                         '//*[@id="ntf_layer_menu_link_Friendships"]/span[1]',
                         '//*[@id="ntf_layer_menu_link_Presents"]',
                         '//*[@id="ntf_layer_menu_link_Groups"]',
                         '//*[@id="ntf_layer_menu_link_Games"]/span[1]',
                         '//*[@id="ntf_layer_menu_link_Payments"]',
                         '//*[@id="ntf_layer_menu_link_Video"]',
                         '//*[@id="ntf_layer_menu_link_Other"]']

    def select_notification(self):
        Lib.simple_wait_element(self.driver, self.NOTIFICATION_TOOLBAR).click()
        Lib.simple_wait_element(self.driver, self.NOTIFICATION_CONTAINER)

    def select_friends(self):
        Lib.simple_wait_element(self.driver, self.FRIENDS_TOOLBAR).click()

    def report_notification(self):

        element = Lib.simple_wait_element(
            self.driver, self.NOTIFICATION_ELEMENT)
        Lib.hover(self.driver, element)
        Lib.visibility_wait_element(
            self.driver, self.NOTIFICATION_REPORT).click()
        Lib.visibility_wait_element(
            self.driver, self.NOTIFICATION_REPORT_SPAM).click()

    def place_first_notification(self):
        return Lib.simple_wait_element(self.driver, self.NOTIFICATION_REMOVED).text

    def close_notification(self):

        Lib.simple_wait_element(self.driver, self.NOTIFICATION_ELEMENT_WITH_ID)
        Lib.simple_wait_element(
            self.driver, self.NOTIFICATION_BUTTON_CLOSE).click()

    def check_notification_close(self):
        if self.wait_process_after_choose_tab() == True:
            return Lib.check_not_exist_element(self.driver, self.NOTIFICATION_ELEMENT_WITH_ID)
        else:
            return False

    def wait_process_after_choose_tab(self):
        try:
            Lib.wait_element_with_attribute(
                self.driver, True, self.NOTIFICATION_TAB_CONTENT, "__process")
            return True
        except TimeoutException:
            return False

        try:
            Lib.wait_element_with_attribute(
                self.driver, False, self.NOTIFICATION_TAB_CONTENT, "__process")
            return True
        except TimeoutException:
            return False

    def choose_tab_notification(self, index):
        Lib.simple_get_element(
            self.driver, self.NOTIFICATION_TABS[index]).click()

    def get_tab_content_title(self):
        return Lib.visibility_wait_element(self.driver, self.NOTIFICATION_TAB_TITLE).text
