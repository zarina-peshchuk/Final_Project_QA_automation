from pages.base_page import BasePage
from pages.locators import BasketLocators


import time, os


class DeletePage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://www.labirint.ru/cart/"
        driver.get(url)
        self.click_the_first_book_for_delete = driver.find_element(*BasketLocators.click_book_for_delete_from_basket)
        self.basket_delete_book = driver.find_element(*BasketLocators.delete_book)
        time.sleep(3)

    def click_on_the_first_book(self):
        self.click_the_first_book_for_delete.click()

    def btn_delete_basket_click(self):
        self.basket_delete_book.click()