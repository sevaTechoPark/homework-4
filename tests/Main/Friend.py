from tests.models.Component import Component


class FriendComponent(Component):

    friend_id = 'imyarek.chelovekovich'
    base = 'https://www.ok.ru/'
    add_btn_css = '.view_lvl1 .icon_cnt'
    cancel_btn_css = '[data-l] [data-entity-id]'
    pending_friends_css = ".ellip-i a[data-l='t,e2']"
    pending_url = 'https://www.ok.ru/vasidmi/outgoingFriendRequests'

    def open_friend_page(self):
        self.driver.get("%s/%s" %(self.base,self.friend_id))

    def add_to_friends(self):
        self.jsClick(self.driver.find_element_by_css_selector(self.add_btn_css))

    def get_pending_friends(self):
        self.driver.get(self.pending_url)
        pending_friends = self.driver.find_elements_by_css_selector(self.pending_friends_css)
        ids = []
        for f in pending_friends:
            ids.append(f.get_attribute("href").split("/")[-1])
        return self.friend_id in ids

    def cancel_request(self):
        self.driver.get(self.pending_url)
        self.driver.find_element_by_css_selector("a[href*='%s']" % self.friend_id)
        self.jsClick(self.driver.find_elements_by_css_selector(self.cancel_btn_css)[-1])