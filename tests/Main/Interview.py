from tests.models.Component import Component
from tests.Lilbs.Lib import Lib
from selenium import webdriver
class Interview(Component):
    INTERVIEW_BLOCK = "//div[@data-action = 'template_block_poll']"
    BUTTON_ADD = "//span[@class = 'mus-tr_add js-mus-tr_add']"
    QUESTION = "//div[@class = 'itx_w posting_poll_i __question']//descendant::textarea"
    FIRST_INPUT = "//div[@class='posting_poll h-mod ok-posting-handler']//descendant::div[4]//descendant::textarea"
    SECOND_INPUT = "//div[@class='posting_poll h-mod ok-posting-handler']//descendant::div[6]//descendant::textarea"
    SUBMIT = "//div[@class = 'posting_submit button-pro']"
    VOTE = "//ul[@class = 'poll_lst']//descendant::li[1]//div[@class = 'poll_n_w']//descendant::span[@class ='poll_check-vis']"
    CHECK_VALUE = "//ul[@class = 'poll_lst']//descendant::li[1]//a[@class = 'poll_i_count']"

    def open_tab(self):
         self.driver.get("https://www.ok.ru/post")
         Lib.simple_wait_element(self.driver, self.INTERVIEW_BLOCK).click()

    def input_value(self):
        Lib.visibility_wait_element(self.driver,self.QUESTION)
        Lib.simple_set_text_to_element(self.driver, self.QUESTION,"QA is cool ?")
        Lib.simple_set_text_to_element(self.driver, self.FIRST_INPUT,"Yes")
        Lib.simple_set_text_to_element(self.driver, self.SECOND_INPUT,"Of Course")
        Lib.visibility_wait_element(self.driver,self.SUBMIT)
        Lib.simple_wait_element(self.driver,self.SUBMIT).click()

    def vote_interview(self):
        Lib.simple_wait_element(self.driver,self.VOTE).click()
        self.driver.refresh();
        Lib.visibility_wait_element(self.driver,self.CHECK_VALUE)
        test = Lib.visibility_wait_element(self.driver,self.CHECK_VALUE).text
        if test < 0:return False
        return True