# coding=utf-8
from tests.Libs.Lib import Lib
from tests.models.Component import Component
from tests.models.Page import Page


class LikePage(Page):
    @property
    def page(self):
        return LikePage(driver=self.driver)


class LikeComponent(Component):

    DATA_ID = ''
    likes_count = 0
    LIKE_BTN_CSS = "span[class='widget_cnt controls-list_lk h-mod']"
    LIKE_BTN_OWNER = "span[data-id1='%s']"
    LIKE_BTN_ATTRIBUTE = 'data-id1'
    DATA_COUNT = 'data-count'

    def like_first_found_post(self):
        like_btn = Lib.simple_wait_element_css(self.driver, self.LIKE_BTN_CSS)
        self.DATA_ID = like_btn.get_attribute(self.LIKE_BTN_ATTRIBUTE)
        self.likes_count = like_btn.get_attribute(self.DATA_COUNT)
        if self.likes_count == None:
            self.likes_count = 0
        self.jsClick(like_btn)  # Здесь он нужен

    def get_likes_from_btn_by_owner(self):
        like_btn = Lib.simple_wait_element_css(
            self.driver, self.LIKE_BTN_OWNER % self.DATA_ID)
        return like_btn.get_attribute(self.DATA_COUNT)

    def remove_like(self):
        like_btn = Lib.simple_wait_element_css(
            self.driver, self.LIKE_BTN_OWNER % self.DATA_ID)
        like_btn.click()
