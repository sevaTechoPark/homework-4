from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from tests.constants.Constants import waitTime
from tests.models.Component import Component


class TopMenu(Component):
    NOTIFICATION = '//*[@id="ntf_toolbar_button"]/div[2]/div'
    FRIENDS2 = '//*[@id="ntf_toolbar_button"]/div[2]/div'
    TAB_TITLE = '//*[@id="hook_Block_NotificationsLayerTitle"]/div'
    TAB_CONTAINER = '//*[@id="hook_Block_NotificationsLayerContent"]'

    ALL_TAB = '//*[@id="ntf_layer_menu_link_All"]/span'
    FRIENDS_TAB = '//*[@id="ntf_layer_menu_link_Friendships"]/span[1]'
    GIFTS_TAB = '//*[@id="ntf_layer_menu_link_Presents"]'
    GROUPS_TAB = '//*[@id="ntf_layer_menu_link_Groups"]'
    GAMES_TAB = '//*[@id="ntf_layer_menu_link_Games"]/span[1]'
    PAYMENTS_TAB = '//*[@id="ntf_layer_menu_link_Payments"]'
    VIDEOS_TAB = '//*[@id="ntf_layer_menu_link_Video"]'
    OTHERS_TAB = '//*[@id="ntf_layer_menu_link_Other"]'

    def select_notification(self):
        element = WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.NOTIFICATION)
        )
        element.click()

    def select_friends(self):
        element = WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.NOTIFICATION)
        )
        element.click()

    def wait_process(self):
        try:
            WebDriverWait(self.driver, waitTime).until(
                lambda d: d.find_element_by_xpath(self.TAB_CONTAINER).get_attribute("__process")
            )
        except TimeoutException:
            print('wait process fail')

        try:
            WebDriverWait(self.driver, waitTime).until_not(
                lambda d: d.find_element_by_xpath(self.TAB_CONTAINER).get_attribute("__process")
            )
        except TimeoutException:
            print('wait not process fail')

    def choose_tab_all(self):
        element = WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.ALL_TAB)
        )
        element.click()

        self.wait_process()

    def choose_tab_friends(self):
        element = WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.FRIENDS_TAB)
        )
        element.click()

        self.wait_process()

    def choose_tab_gifts(self):
        element = WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.GIFTS_TAB)
        )
        element.click()

        self.wait_process()

    def choose_tab_groups(self):
        element = WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.GROUPS_TAB)
        )
        element.click()

        self.wait_process()

    def choose_tab_games(self):
        element = WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.GAMES_TAB)
        )
        element.click()

        self.wait_process()

    def choose_tab_payments(self):
        element = WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.PAYMENTS_TAB)
        )
        element.click()

        self.wait_process()

    def choose_tab_videos(self):
        element = WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.VIDEOS_TAB)
        )
        element.click()

        self.wait_process()

    def choose_tab_others(self):
        element = WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.OTHERS_TAB)
        )
        element.click()

        self.wait_process()

    def get_tab_title(self):
        return WebDriverWait(self.driver, waitTime).until(
            lambda d: d.find_element_by_xpath(self.TAB_TITLE).text
        )
