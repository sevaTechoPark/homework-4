from tests.Libs.Lib import Lib
from tests.constants.Constants import *
from tests.models.Component import Component


class Feed(Component):
    def __init__(self, driver):
        super(Feed, self).__init__(driver)
        for i in range(0, len(self.REACTIONS)):
            self.REACTIONS[i] = self.REACTION_PANEL + self.REACTIONS[i]

    LIKE_BUTTONS = '//div[@class="feed-list"]//li[@class="widget-list_i "][last()]'
    LIKE_INFO = LIKE_BUTTONS + \
        '//span[@class="widget_cnt controls-list_lk h-mod"]'

    LIKE_COUNT = '//span[contains(@class, "widget_count")]'
    LIKE_PANEL = '//div[@id="hook_Block_ShortcutMenuReact"]//div[contains(@class, "sc-menu")]//ul[@class="u-menu"]'
    LIKE_PANEL_LAST_LIKED_LINKS = '//li[@class="ucard-mini-list_li"]//a'
    LIKE_PANEL_LAST_LIKED_NAMES = '//li[@class="ucard-mini-list_li"]//div[@class="ellip o"]'

    LIST_ALL_LIKES = '//li[@class="ucard-mini-list_all"]//a'
    LIST_ALL_LIKES_NAMES = '//div[@class="modal-new_hld"]//div[@class="ellip"]//a'

    REACTION_PANEL = '//div[@class="reactions"]'
    REACTIONS = ['//span[@data-l="t,reaction0"]', '//span[@data-l="t,reaction1"]', '//span[@data-l="t,reaction2"]',
                 '//span[@data-l="t,reaction3"]', '//span[@data-l="t,reaction4"]']
    REACTION_ICON = '//span[contains(@class, "widget_ico")]'
    WALL_CONTENT = '//div[@data-block="MainFeedsContent"]'

    def add_like(self):
        element = Lib.simple_wait_elements(self.driver, self.LIKE_BUTTONS)[0]
        if self.get_number_emotion() == REACTIONS_CLASS:
            element.click()
        return Lib.simple_wait_elements(self.driver, self.LIKE_INFO)[0].get_attribute("data-id1")

    def remove_like(self):
        element = Lib.simple_wait_elements(self.driver, self.LIKE_BUTTONS)[0]
        element.click()

    def add_emotion_to_like(self, old_reaction=-1):
        element = Lib.visibility_wait_element(self.driver, self.WALL_CONTENT)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        reaction_number = REACTIONS_LIKE
        while reaction_number == old_reaction:
            reaction_number = REACTIONS_LOL
        element = Lib.simple_wait_elements(self.driver, self.LIKE_BUTTONS)[0]
        Lib.hover(self.driver, element)
        Lib.visibility_wait_element(self.driver, self.REACTION_PANEL)
        Lib.simple_wait_element(
            self.driver, self.REACTIONS[reaction_number]).click()

    def get_number_emotion(self):
        reaction_class = Lib.visibility_wait_element(
            self.driver, self.REACTION_ICON).get_attribute("class")
        if reaction_class == 'widget_ico __react __react-like':
            return REACTIONS_LIKE
        if reaction_class == 'widget_ico __react __react-lol':
            return REACTIONS_LOL
        if reaction_class == 'widget_ico __react __react-sorrow':
            return REACTIONS_SORROW
        if reaction_class == 'widget_ico __react __react-heart':
            return REACTIONS_HEART
        if reaction_class == 'widget_ico __react __react-wow':
            return REACTIONS_WOW
        if reaction_class == 'widget_ico widget_ico ic_klass' or reaction_class == 'widget_ico ic_klass':
            return REACTIONS_CLASS
        return REACTIONS_NOT_FOUND

    def create_xpath_for_id_like(self, id):
        return self.LIKE_BUTTONS + '//span[@data-id1="' + str(id) + '"]'

    def open_who_likes(self, id):
        xpath = self.create_xpath_for_id_like(id) + self.LIKE_COUNT
        element = Lib.simple_wait_element(self.driver, xpath)
        Lib.hover(self.driver, element)
        Lib.visibility_wait_element(self.driver, self.LIKE_PANEL)

    def get_names_last_liked(self, id):
        self.open_who_likes(id)
        elements = Lib.simple_wait_elements(
            self.driver, self.LIKE_PANEL_LAST_LIKED_NAMES)
        names = []
        for element in elements:
            names.append(element.text)
        return names

    def get_links_last_liked(self, id):
        self.open_who_likes(id)
        elements = Lib.simple_wait_elements(
            self.driver, self.LIKE_PANEL_LAST_LIKED_LINKS)
        links = []
        for element in elements:
            links.append(element.get_attribute("href"))
        return links

    def open_all_likes(self, id):
        self.open_who_likes(id)
        Lib.visibility_wait_element(self.driver, self.LIST_ALL_LIKES).click()

    def get_all_names(self):
        elements = Lib.simple_wait_elements(
            self.driver, self.LIST_ALL_LIKES_NAMES)
        names = []
        for element in elements:
            names.append(element.text)
        return names

    def get_all_links(self):
        elements = Lib.simple_wait_elements(
            self.driver, self.LIST_ALL_LIKES_NAMES)
        names = []
        for element in elements:
            names.append(element.get_attribute("href"))
        return names
