from tests.Libs.Lib import Lib
from tests.models.Component import Component


class Friends(Component):
    FIRST_ACCOUNT_NAME = '//ul[@class="ugrid_cnt"]//li//div[@class="ellip"]//a[text()="Name Female"]'
    INVITE_TO_GROUP = '//div[@class="gwt-shortcutMenu-content"]//ul//li[@class="ic_group"]//a'
    GROUP_TO_INVITE = '//div[@id="hook_Block_InviteUserToGroup2GroupsList"]//div[@class="ugrid_i"]//a'

    def select_friend(self):
        Lib.simple_wait_element(self.driver, self.FIRST_ACCOUNT_NAME).click()

    def invite__friend_to_group(self):
        element = Lib.simple_wait_element(self.driver, self.FIRST_ACCOUNT_NAME)
        Lib.hover(self.driver, element)
        Lib.visibility_wait_element(self.driver, self.INVITE_TO_GROUP).click()
        Lib.simple_wait_elements(self.driver, self.GROUP_TO_INVITE)[0].click()
