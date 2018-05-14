# coding=utf-8
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from tests.constants.Constants import waitTime
from tests.models.Component import Component
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class TopMenu(Component):
    NOTIFICATION_TOOLBAR = '//ul[@class="toolbar_nav"]//li[@data-l="t,notifications"]'
    FRIENDS_TOOLBAR = '//ul[@class="toolbar_nav"]//li[@data-l="t,friends"]'

    NOTIFICATION_CONTAINER = '//div[@class="notifs_cnt"]'
    NOTIFICATION_TAB_TITLE = '//*[@id="hook_Block_NotificationsLayerTitle"]/div'
    NOTIFICATION_TAB_CONTENT = '//*[@id="hook_Block_NotificationsLayerContent"]'

    FIRST_ACCOUNT_NAME = '//ul[@class="ugrid_cnt"]//li//div[@class="ellip"]//a[text()="Name Female"]'
    INVITE_TO_GROUP = '//div[@class="gwt-shortcutMenu-content"]//ul//li[@class="ic_group"]//a'
    GROUP_TO_INVITE = '//div[@id="hook_Block_InviteUserToGroup2GroupsList"]//div[@class="ugrid_i"]//a'

    NOTIFICATION_ELEMENT = '//div[@id="ntf_layer_content_inner"]/div[position() = 1]'
    NOTIFICATION_ELEMENT_WITH_ID = NOTIFICATION_ELEMENT + '/div'
    NOTIFICATION_REPORT = NOTIFICATION_ELEMENT + '//div[@class="notif_ac fade-on-hover"]//i[@data-l="t,spam"]'
    NOTIFICATION_REPORT_SPAM = NOTIFICATION_ELEMENT + '//div[@class="notif_ac fade-on-hover"]//div[@data-l="t,shortcutMenu"]//a'
    NOTIFICATION_REMOVED = NOTIFICATION_ELEMENT + '//div[@data-module="NotificationRemoved"]'

    NOTIFICATION_CLOSE = NOTIFICATION_ELEMENT + '//button[@data-l="t,btn_ignore"]'

    NOTIFICATION_TABS = ['//*[@id="ntf_layer_menu_link_All"]/span',
                         '//*[@id="ntf_layer_menu_link_Friendships"]/span[1]',
                         '//*[@id="ntf_layer_menu_link_Presents"]',
                         '//*[@id="ntf_layer_menu_link_Groups"]',
                         '//*[@id="ntf_layer_menu_link_Games"]/span[1]',
                         '//*[@id="ntf_layer_menu_link_Payments"]',
                         '//*[@id="ntf_layer_menu_link_Video"]',
                         '//*[@id="ntf_layer_menu_link_Other"]']

    def select_notification(self):
        element = WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.NOTIFICATION_TOOLBAR)
        )
        element.click()

        WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.NOTIFICATION_CONTAINER)
        )

    def select_friends(self):
        element = WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.FRIENDS_TOOLBAR)
        )
        element.click()

    def invite_to_group(self):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)

        element = WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.FIRST_ACCOUNT_NAME)
        )

        ActionChains(self.driver).move_to_element(element).perform()

        element = WebDriverWait(self.driver, waitTime, ignored_exceptions=ignored_exceptions).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.INVITE_TO_GROUP)))
        element.click()

        elements = WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_elements_by_xpath(self.GROUP_TO_INVITE)
        )

        elements[0].click()

    def report_notification(self):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)

        self.wait_process_after_choose_tab()

        element = WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.NOTIFICATION_ELEMENT)
        )

        ActionChains(self.driver).move_to_element(element).perform()

        element = WebDriverWait(self.driver, waitTime, ignored_exceptions=ignored_exceptions).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.NOTIFICATION_REPORT)))
        element.click()

        element = WebDriverWait(self.driver, waitTime, ignored_exceptions=ignored_exceptions).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.NOTIFICATION_REPORT_SPAM)))
        element.click()

    def place_first_notification(self):
        return WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.NOTIFICATION_REMOVED).text
        )

    def close_notification(self):
        self.wait_process_after_choose_tab()

        WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.NOTIFICATION_ELEMENT_WITH_ID)
        )

        element = WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.NOTIFICATION_CLOSE)
        )
        element.click()

    def check_notification_close(self):
        self.wait_process_after_choose_tab()

        try:
            self.driver.find_element_by_xpath(self.NOTIFICATION_ELEMENT_WITH_ID)
            return False
        except NoSuchElementException:
            return True

    def wait_process_after_choose_tab(self):
        try:
            WebDriverWait(self.driver, waitTime).until(
                lambda d: d.find_element_by_xpath(self.NOTIFICATION_TAB_CONTENT).get_attribute("__process")
            )
        except TimeoutException:
            print('wait process fail')

        try:
            WebDriverWait(self.driver, waitTime).until_not(
                lambda d: d.find_element_by_xpath(self.NOTIFICATION_TAB_CONTENT).get_attribute("__process")
            )
        except TimeoutException:
            print('wait not process fail')

    def choose_tab_notification(self, index):
        tab_name = self.NOTIFICATION_TABS[index]
        self.driver.find_element_by_xpath(tab_name).click()
        self.wait_process_after_choose_tab()

    def get_tab_content_title(self):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        element = WebDriverWait(self.driver, waitTime, ignored_exceptions=ignored_exceptions).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.NOTIFICATION_TAB_TITLE)))

        return element.text
