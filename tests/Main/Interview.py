from tests.models.Component import Component
from tests.Libs.Lib import Lib
from selenium import webdriver


class Interview(Component):
    INTERVIEW_BLOCK = "//div[@data-action = 'template_block_poll']"
    BUTTON_ADD = "//span[@class = 'mus-tr_add js-mus-tr_add']"
    QUESTION = "//textarea[@class ='js_input itx h-mod flipthis-highlight']"
    FIRST_INPUT = "//textarea[@class = 'js_input js_answer itx h-mod flipthis-highlight']"
    SECOND_INPUT = "//div[@class = 'itx_w posting_poll_i visible']//textarea[@data-module ='autosize']"
    SUBMIT = "//div[@class = 'posting_submit button-pro']"
    VOTE = "//div[@class = 'flipthis-wrapper']//span[@class = 'poll_check-vis flipthis-highlight']"
    CHECK_VALUE = "//ul[@class = 'poll_lst']//descendant::li[1]//a[@class = 'poll_i_count']"

    def open_tab(self):
        self.driver.get("https://www.ok.ru/post")
        Lib.simple_wait_element(self.driver, self.INTERVIEW_BLOCK).click()

    def input_value(self, main_question, first_answer, second_answer):
        Lib.visibility_wait_element(self.driver, self.QUESTION)
        Lib.simple_set_text_to_element(
            self.driver, self.QUESTION, main_question)
        Lib.simple_set_text_to_element(
            self.driver, self.FIRST_INPUT, first_answer)
        Lib.simple_set_text_to_element(
            self.driver, self.SECOND_INPUT, second_answer)
        Lib.visibility_wait_element(self.driver, self.SUBMIT)
        Lib.simple_wait_element(self.driver, self.SUBMIT).click()

    def vote_interview(self):
        Lib.simple_wait_element(self.driver, self.VOTE).click()
        self.driver.refresh()
        Lib.visibility_wait_element(self.driver, self.CHECK_VALUE)

    def vote_value(self):
        vote = Lib.visibility_wait_element(self.driver, self.CHECK_VALUE).text
        return vote
