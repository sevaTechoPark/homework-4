from tests.models.Component import Component
# from tests.models.Page import Page


# class CommentPage(Page):
#     @property
#     def page(self):
#         return CommentPage(self.driver)

class CommentClass(Component):
    comment_element_css = 'div.flipthis-wrapper'
    comment_text = 'test'
    enter_comment = "smplBtnId6"
    def open(self):

        commentBtn = self.driver.find_element_by_css_selector(self.comment_element_css)
        # self.driver.execute_script("arguments[0].style.visibility = 'visible';",
        #                            changeBtn)
        self.jsClick(commentBtn)

    def add_comment(self):
        self.driver.find_element_by_id("fakeFocusId8").send_keys(self.comment_text)

    def change(self):
        self.jsClick(self.driver.find_element_by_id(self.enter_comment))
    
    def change(self):
        self.jsClick(self.driver.find_element_by_css_selector('div.klass_w'))
