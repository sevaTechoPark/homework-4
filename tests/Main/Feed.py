from tests.Lilbs.Lib import Lib
from tests.models.Component import Component
from random import randint


class Feed(Component):
    def __init__(self, driver):
        super(Feed, self).__init__(driver)
        for i in range(0, len(self.REACTIONS)):
            self.REACTIONS[i] = self.REACTION_PANEL + self.REACTIONS[i]

    LIKE_BUTTONS = '//div[@class="feed-list"]//div[@class="feed-w"]//ul[@class="widget-list"]//li[@class="widget-list_i "][last()]'
    LIKE_INFO = LIKE_BUTTONS + '//span[@class="widget_cnt controls-list_lk h-mod"]'

    LIKE_COUNT = '//span[contains(@class, "widget_count")]'
    LIKE_PANEL = '//div[@id="hook_Block_ShortcutMenuReact"]//div[contains(@class, "sc-menu")]//ul[@class="u-menu"]'
    LIKE_PANEL_LAST_LIKED_LINKS = LIKE_PANEL + '//li[@class="u-menu_li"]//ul[@class="ucard-mini-list __redesign __react"]//li[@class="ucard-mini-list_li"]//a'
    LIKE_PANEL_LAST_LIKED_NAMES = LIKE_PANEL + '//li[@class="ucard-mini-list_li"]//div[@class="ucard-mini_cnt"]//div[@class="ellip o"]'

    REACTION_PANEL = '//div[@class="reactions"]'
    REACTIONS = ['//span[@data-l="t,reaction0"]', '//span[@data-l="t,reaction1"]', '//span[@data-l="t,reaction2"]',
                 '//span[@data-l="t,reaction3"]', '//span[@data-l="t,reaction4"]']
    REACTION_ICON = '//span[contains(@class, "widget_ico")]'

    def add_like(self):
        element = Lib.simple_wait_elements(self.driver, self.LIKE_BUTTONS)[0]
        if self.get_number_emotion() == 5:
            element.click()
        return Lib.simple_wait_elements(self.driver, self.LIKE_INFO)[0].get_attribute("data-id1")

    def remove_like(self):
        element = Lib.simple_wait_elements(self.driver, self.LIKE_BUTTONS)[0]
        if self.get_number_emotion() != 5:
            element.click()

    def add_emotion_to_like(self, old_reaction=-1):
        reaction_number = randint(0, 4)
        while reaction_number == old_reaction:
            reaction_number = randint(0, 4)
        element = Lib.simple_wait_elements(self.driver, self.LIKE_BUTTONS)[0]
        Lib.hover(self.driver, element)
        Lib.visibility_wait_element(self.driver, self.REACTION_PANEL)
        Lib.simple_get_element(self.driver, self.REACTIONS[reaction_number]).click()
        return reaction_number

    def get_number_emotion(self):
        reaction_class = Lib.visibility_wait_element(self.driver, self.REACTION_ICON).get_attribute("class")
        if reaction_class == 'widget_ico __react __react-like':
            return 0
        if reaction_class == 'widget_ico __react __react-lol':
            return 1
        if reaction_class == 'widget_ico __react __react-sorrow':
            return 2
        if reaction_class == 'widget_ico __react __react-heart':
            return 3
        if reaction_class == 'widget_ico __react __react-wow':
            return 4
        if reaction_class == 'widget_ico widget_ico ic_klass' or reaction_class == 'widget_ico ic_klass':
            return 5
        return 6

    def create_xpath_for_id_like(self, id):
        return self.LIKE_BUTTONS + '//span[@data-id1="' + str(id) + '"]'

    def open_who_likes(self, id):
        xpath = self.create_xpath_for_id_like(id) + self.LIKE_COUNT
        element = Lib.simple_wait_element(self.driver, xpath)
        Lib.hover(self.driver, element)
        Lib.visibility_wait_element(self.driver, self.LIKE_PANEL)

    def get_names_last_liked(self, id):
        self.open_who_likes(id)
        elements = Lib.simple_wait_elements(self.driver, self.LIKE_PANEL_LAST_LIKED_NAMES)
        links = []
        for element in elements:
            links.append(element.text)
        return links

    def get_links_last_liked(self, id):
        self.open_who_likes(id)
        elements = Lib.simple_wait_elements(self.driver, self.LIKE_PANEL_LAST_LIKED_LINKS)
        links = []
        for element in elements:
            links.append(element.get_attribute("href"))
        return links
