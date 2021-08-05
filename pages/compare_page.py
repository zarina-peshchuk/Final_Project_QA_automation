from pages.base_page import BasePage
from pages.locators import BasketLocators, ProductBuyAreaLocators, MyLabirintLocators


import time, os


class ComparePage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://www.labirint.ru"
        driver.get(url)
        self.first_book = driver.find_elements(*BasketLocators.choose_book)[0]
        self.second_book = driver.find_element(*BasketLocators.choose_book)[1]
        self.else_btn_first = driver.find_element(*ProductBuyAreaLocators.else_actions_first_book)
        self.else_btn_second = driver.find_element(*ProductBuyAreaLocators.else_actions_second_book)
        self.compare_btn_and_go_to_compare = driver.find_element(*ProductBuyAreaLocators.compare_btn)
        self.first_book_name_in_compare = driver.find_element(*MyLabirintLocators.compare_books)[0]
        self.second_book_name_in_compare = driver.find_element(*MyLabirintLocators.compare_books)[1]
        time.sleep(3)

    def get_first_book_name(self):
        self.first_book.find_element("product-title.large-name").get_text()

    def get_second_book_name(self):
        self.second_book.find_element("product-title.large-name").get_text()

    def click_else_btn_first_book(self):
        self.else_btn_first.click()

    def click_compare_btn(self):
        self.compare_btn_and_go_to_compare.click()

    def click_else_btn_second_book(self):
        self.else_btn_second.click()

    def click_compare_btn_second(self):
        self.compare_btn_and_go_to_compare.click()

    def click_go_to_compare(self):
        self.compare_btn_and_go_to_compare.click()

    def get_compare_first_book_name(self):
        self.first_book_name_in_compare.get_text()

    def get_compare_second_book_name(self):
        self.second_book_name_in_compare.get_text()