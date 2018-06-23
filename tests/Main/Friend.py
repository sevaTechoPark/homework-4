# coding=utf-8
from tests.Libs.Lib import Lib
from tests.models.Component import Component


class FriendComponent(Component):

    FRIEND_ID = 'imyarek.chelovekovich'
    BASE = 'https://www.ok.ru/'
    ADD_BTN_CSS = "span[class='dropdown_ac button-pro __wide']"
    CANCEL_BTN_CSS = '[data-l] [data-entity-id]'
    OUTGOING_FRIENDS_COUNT_CSS = "span[id='counter_outgoingFriendRequestsPage'] span"
    PENDING_FRIENDS_CSS = "a[class='o']"
    PENDING_PREFIX = '/outgoingFriendRequests'
    USER_URL = ''
    OUTGOING_FRIENDS_COUNT = -1
    PENDING_FRIENDS = []
    CURRENT_USER_CSS = "a[data-l='t,selectCurrentUser']"

    def open_friend_page(self):
        self.driver.get("%s/%s" % (self.BASE, self.FRIEND_ID))

    def add_to_friends(self):
        add_btn = Lib.simple_wait_element_css(self.driver, self.ADD_BTN_CSS)
        add_btn.click()

    def get_pending_friends(self):
        self.USER_URL = Lib.simple_wait_element_css(
            self.driver, self.CURRENT_USER_CSS).get_attribute('href')
        self.driver.get(self.USER_URL+self.PENDING_PREFIX)
        self.scroll_to_new()
        ids = []
        for f in self.PENDING_FRIENDS:
            ids.append(f.get_attribute("href").split("/")[-1])
        return self.FRIEND_ID in ids

    def scroll_to_new(self):
        self.OUTGOING_FRIENDS_COUNT = int(
            Lib.simple_wait_element_css(self.driver, self.OUTGOING_FRIENDS_COUNT_CSS).text)
        self.PENDING_FRIENDS = Lib.simple_get_elements_css(
            self.driver, self.PENDING_FRIENDS_CSS)
        while len(self.PENDING_FRIENDS) < self.OUTGOING_FRIENDS_COUNT:
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight)")
            self.PENDING_FRIENDS = Lib.simple_get_elements_css(
                self.driver, self.PENDING_FRIENDS_CSS)

    def cancel_request(self):
        self.driver.get(self.USER_URL+self.PENDING_PREFIX)
        self.scroll_to_new()
        cancel_btn = Lib.simple_wait_elements_css(
            self.driver, self.CANCEL_BTN_CSS)
        self.jsClick(cancel_btn[-1])  # Здесь он нужен
