from pages.base_page import BasePage
from pages.locators import ProductBuyAreaLocators, BasketLocators


import time, os


class PutPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("https://www.labirint.ru")
        driver.get(url)
        self.first_book = driver.find_elements(*ProductBuyAreaLocators.put_first_book)[0]
        self.btn_put = driver.find_element(*ProductBuyAreaLocators.put_btn)
        self.put_book_name = driver.find_element(*BasketLocators.basket_book_name)
        self.choose_book_from_put = driver.find_element(*ProductBuyAreaLocators.choose_book_from_put_for_delete)
        self.delete_book_from_put = driver.find_element(*ProductBuyAreaLocators.delete_book_from_put)
        time.sleep(3)

    def get_first_book_name(self):
        self.first_book.find_element("product-title.large-name").text()

    def put_first_book(self):
        self.first_book.click()

    def put_btn_click(self):
        self.btn_put.click()

    def get_put_book_name(self):
        self.put_book_name.text()

    def btn_choose_book_from_put(self):
        self.choose_book_from_put.click()

    def btn_delete_book_from_put(self):
        self.delete_book_from_put.click()