from tests.models.Component import Component
from tests.Libs.Lib import Lib


class VideoAdd(Component):
    VIDEO_BLOCK = "//div[@class = 'vid-card_img__link']"
    BUTTON_ADD = "//div[@class = 'vid-card_cnt soh-s js-droppable']//descendant::a[3]"
    VIDEO_LIST = "//li[@class ='mml_subcat_li __interac']"

    def open_video(self):
        self.driver.get("https://www.ok.ru/video/channels")

    def add_video(self):
        before_click = len(self.driver.find_elements_by_xpath(self.VIDEO_LIST))
        element = Lib.visibility_wait_element(self.driver, self.VIDEO_BLOCK)
        Lib.hover(self.driver, element)
        Lib.simple_wait_element(self.driver, self.BUTTON_ADD).click()
        after_click = len(self.driver.find_elements_by_xpath(self.VIDEO_LIST))
        return (after_click != before_click)
