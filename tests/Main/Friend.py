from tests.Lilbs.Lib import Lib
from tests.models.Component import Component


class FriendComponent(Component):

    friend_id = 'imyarek.chelovekovich'
    base = 'https://www.ok.ru/'
    add_btn_css = "span[class='dropdown_ac button-pro __wide']"
    cancel_btn_css = '[data-l] [data-entity-id]'
    pending_friends_css = "a[class='o']"
    pending_prefix = '/outgoingFriendRequests'
    user_url = ''
    outgoing_friends_count = -1
    pending_friends = []

    def open_friend_page(self):
        self.driver.get("%s/%s" %(self.base,self.friend_id))

    def add_to_friends(self):
        add_btn = Lib.simple_wait_element_css(self.driver,self.add_btn_css)
        self.jsClick(add_btn)

    def get_pending_friends(self):
        self.user_url = Lib.simple_wait_element_css(self.driver,"a[data-l='t,selectCurrentUser']").get_attribute('href')
        self.driver.get(self.user_url+self.pending_prefix)
        self.scroll_to_new()
        ids = []
        for f in self.pending_friends:
            ids.append(f.get_attribute("href").split("/")[-1])
        return self.friend_id in ids

    def scroll_to_new(self):
        self.outgoing_friends_count = int(
            Lib.simple_wait_element_css(self.driver, "span[id='counter_outgoingFriendRequestsPage'] span").text)
        self.pending_friends = self.driver.execute_script(
            'return document.querySelectorAll("%s")' % self.pending_friends_css)
        while len(self.pending_friends) < self.outgoing_friends_count:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            self.pending_friends = self.driver.execute_script(
                'return document.querySelectorAll("%s")' % self.pending_friends_css)

    def cancel_request(self):
        self.driver.get(self.user_url+self.pending_prefix)
        self.scroll_to_new()
        cancel_btn = Lib.simple_wait_elements_css(self.driver,self.cancel_btn_css)
        self.jsClick(cancel_btn[-1])