#! /usr/bin/env python
# -*- coding: utf-8 -*-
from tests.models.Component import Component
from tests.Lilbs.Lib import Lib
from selenium.webdriver.common.action_chains import ActionChains

class Mood(Component):

    # random_album_name = '%dalbum%d' % (randint(1,9999),randint(1,9999))
    # create_album_btn_css = 'span[class="tico"]'
    # album_name_css = '[class="form__gl-1-2 form photo-album-settings"] [type="text"]'
    # save_btn_css = '.formButtonContainer [type]'
    # albums_css = 'a[class="o"]'
    MY_PROFILE = "//a[@data-l = 't,userPage']"
    MOOD_HOVER = "//div[@class ='pform_actions']//descendant::span[8]"
    test ="//span[text()='Настроение']"
    def open_profile(self):
        Lib.simple_wait_element(self.driver,self.MY_PROFILE).click()
   # "//a[@class = 'add-stub al add-stub__hor __grayed]"
    def add_theme(self):
       #  wd = webdriver_connection.connection
         element = self.driver.find_element_by_link_text("Ещё")
         ActionChains(self.driver).move_to_element(element).perform()
         #hov.perform()
         print('work')
         Lib.visibility_wait_element(self.driver,"//a[@class = 'test']")


        # element = Lib.visibility_wait_element(self.driver,self.MOOD_HOVER)
        # #Lib.simple_wait_element(self.driver,self.MOOD_HOVER).click()
        # Lib.hover(self.driver, element)
        # Lib.visibility_wait_element(self.driver,self.test)
       # Lib.simple_wait_element(self.driver,self.test).click()
        #Lib.simple_wait_element(self.driver,self.MOOD_HOVER).click()
        #Lib.visibility_wait_element(self.driver,"//a[@class = 'test']")
       
    # def fill_name(self):
    #     self.driver.find_element_by_css_selector(self.album_name_css).send_keys(self.random_album_name)

    # def create_album(self):
    #     self.jsClick(self.driver.find_element_by_css_selector(self.create_album_btn_css))
    #     self.fill_name()
    #     self.jsClick(self.driver.find_element_by_css_selector(self.save_btn_css))

    # def get_albums(self):
    #     albums = []
    #     for album in self.driver.find_elements_by_css_selector(self.albums_css):
    #         albums.append(album.text)
    #     return albums
