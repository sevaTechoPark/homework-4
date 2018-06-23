# coding=utf-8
from tests.Libs.Lib import Lib
from tests.models.Component import Component
from tests.models.Page import Page


class AlbumPage(Page):
    @property
    def page(self):
        return AlbumPage(driver=self.driver)


class AlbumComponent(Component):
    CREATE_ALBUM_BTN_CSS = '.portlet_h_ac .tico'
    ALBUM_NAME_CSS = '[class="photo-album-settings"] [type="text"]'
    SAVE_BTN_CSS = '.formButtonContainer [type]'
    ALBUMS_CSS = 'a[class="o"]'
    EDIT_ALBUM_CSS = "div[class='photo-menu_edit'] a"
    ALBUM_LINK_CSS = "a[title='new_album']"
    DELETE_ALBUM_CSS = "li[class='controls-list_item']:nth-of-type(2)"
    DELETE_CONFIRM_BTN = "input[name='button_delete_confirm']"
    PHOTOS_URL_CSS = "a[data-l='t,userPhotos']"

    def open_photos_page(self):
        el = Lib.simple_wait_element_css(self.driver, self.PHOTOS_URL_CSS)
        el.click()

    def fill_name(self, name_album):
        album_name_el = Lib.visibility_wait_element_css(
            self.driver, self.ALBUM_NAME_CSS)
        album_name_el.send_keys(name_album)

    def create_album(self):
        create_album_btn = Lib.simple_wait_element_css(
            self.driver, self.CREATE_ALBUM_BTN_CSS)
        create_album_btn.click()
        save_btn = Lib.simple_wait_element_css(self.driver, self.SAVE_BTN_CSS)
        save_btn.click()

    def get_albums(self):
        albums = []
        found_albums = Lib.simple_wait_elements_css(
            self.driver, self.ALBUMS_CSS)
        for album in found_albums:
            albums.append(album.text)
        return albums

    def select_created_album(self):
        album = Lib.simple_wait_element_css(self.driver, self.ALBUM_LINK_CSS)
        album.click()

    def set_edit_album(self):
        edit_btn = Lib.simple_wait_element_css(
            self.driver, self.EDIT_ALBUM_CSS)
        edit_btn.click()

    def delete_album(self):
        self.select_created_album()
        self.set_edit_album()
        delete_link = Lib.simple_wait_element_css(
            self.driver, self.DELETE_ALBUM_CSS)
        delete_link.click()
        delete_btn = Lib.simple_wait_element_css(
            self.driver, self.DELETE_CONFIRM_BTN)
        delete_btn.click()
