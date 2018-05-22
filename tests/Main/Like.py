from tests.models.Component import Component
from tests.models.Page import Page


class LikePage(Page):
    @property
    def page(self):
        return LikePage(driver=self.driver)

class LikeComponent(Component):

    data_id = ''
    likes_count = 0
    like_btn_css = "span[class='widget_cnt controls-list_lk h-mod']"

    def like_first_found_post(self):
        like_btn = self.driver.find_element_by_css_selector(self.like_btn_css)
        self.data_id = like_btn.get_attribute('data-id1')
        self.likes_count = like_btn.get_attribute('data-count')
        self.jsClick(like_btn)

    def get_likes_from_btn_by_owner(self,id):
        like_btn = self.driver.find_element_by_css_selector("span[data-id1='%s']" % id)
        return like_btn.get_attribute('data-count')

    def remove_like(self,id):
        like_btn = self.driver.find_element_by_css_selector("span[data-id1='%s']" % id)
        self.jsClick(like_btn)