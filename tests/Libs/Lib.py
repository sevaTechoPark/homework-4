# coding=utf-8
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from tests.constants.Constants import waitTime
from tests.models.Component import Component
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class Lib(Component):
    @staticmethod
    def simple_get_element(driver, x_path):
        return driver.find_element_by_xpath(x_path)

    @staticmethod
    def simple_get_elements(driver, x_path):
        return driver.find_elements_by_xpath(x_path)

    @staticmethod
    def simple_get_elements_css(driver, css):
        return driver.find_elements_by_css_selector(css)

    @staticmethod
    def simple_set_text_to_element(driver, x_path, text):
        driver.find_element_by_xpath(x_path).send_keys(text)

    @staticmethod
    def simple_wait_element(driver, x_path):
        return WebDriverWait(driver, waitTime).until(
            lambda d: d.find_element_by_xpath(x_path)
        )

    @staticmethod
    def simple_wait_element_css(driver, css):
        return WebDriverWait(driver, waitTime).until(
            lambda d: d.find_element_by_css_selector(css)
        )

    @staticmethod
    def simple_wait_elements_css(driver, css):
        return WebDriverWait(driver, waitTime).until(
            lambda d: d.find_elements_by_css_selector(css)
        )

    @staticmethod
    def wait_element_with_attribute(driver, until, x_path, attribute):
        if until:
            return WebDriverWait(driver, waitTime).until(
                lambda d: d.find_element_by_xpath(
                    x_path).get_attribute(attribute)
            )
        else:
            return WebDriverWait(driver, waitTime).until_not(
                lambda d: d.find_element_by_xpath(
                    x_path).get_attribute(attribute)
            )

    @staticmethod
    def simple_wait_elements(driver, x_path):
        return WebDriverWait(driver, waitTime).until(
            lambda d: d.find_elements_by_xpath(x_path)
        )

    @staticmethod
    def visibility_wait_element(driver, x_path):
        return WebDriverWait(driver, waitTime).until(
            expected_conditions.visibility_of_element_located((By.XPATH, x_path)))

    @staticmethod
    def visibility_wait_element_css(driver, css):
        return WebDriverWait(driver, waitTime).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, css)))

    @staticmethod
    def hover(driver, element):
        ActionChains(driver).move_to_element(element).perform()

    @staticmethod
    def check_not_exist_element(driver, x_path):
        try:
            driver.find_element_by_xpath(x_path)
            return False
        except NoSuchElementException:
            return True
