class Component(object):
    def __init__(self, driver):
        self.driver = driver

    def jsClick(self, element):
        self.driver.execute_script(
            "arguments[0].style.visibility = 'visible';", element)
        self.driver.execute_script("arguments[0].click();", element)
