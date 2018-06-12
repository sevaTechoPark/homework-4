#! /usr/bin/env python
# -*- coding: utf-8 -*-
from tests.models.Component import Component
from tests.Lilbs.Lib import Lib

class Mood(Component):

    HAPPY_MOOD = "//div[@class = 'feeling-card_i flipthis-highlight']"
    TEXT_MOOD = "//textarea[@name = 'st.layer.fieldFeelingText']"
    ADD_BUTTON = "//button[@class = 'button-pro __sec']"
    INPUT_TEXT = "End testing OK"

    def open_theme(self):
        else_element = self.driver.find_element_by_link_text("Ещё")
        Lib.hover(self.driver,else_element)
        mood_element = self.driver.find_element_by_link_text("Настроение")
        Lib.simple_wait_element(self.driver,mood_element).click()

    def create_mood(self):
        Lib.simple_wait_element(self.driver,self.HAPPY_MOOD).click()
        Lib.simple_set_text_to_element(self.driver, self.TEXT_MOOD,self.INPUT_TEXT)
        Lib.simple_wait_element(self.driver,self.ADD_BUTTON).click()

    def mood_checker(self):
        mr_mood = self.driver.find_element_by_link_text(self.INPUT_TEXT)
        return Lib.check_exist_element(self.driver,mr_mood)