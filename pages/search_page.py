from pages.base_page import BasePage
from pages.locators import SearchLocators


import time, os


class SearchPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://www.labirint.ru"
        driver.get(url)
        self.search_field = driver.find_element(*SearchLocators.search_field)
        self.search_btn = driver.find_element(*SearchLocators.search_btn)
        self.contain_text_positive = driver.find_element(*SearchLocators.search_positive_result)
        self.contain_text_negative = driver.find_element(*SearchLocators.search_negative_result)
        time.sleep(3)

    def enter_word(self, value):
        self.search_field.click()
        self.search_field.clear()
        self.search_field.send_keys(value)

    def btn_search_click(self):
        self.search_btn.click()

    def contain_text_in_search(self, value):
        self.contain_text_positive.find_element()

    def contain_negative_result_in_search(self, value):
        self.contain_text_negative.find_element()