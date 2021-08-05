from pages.base_page import BasePage
from pages.locators import BasketLocators


import time, os


class BasketPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://www.labirint.ru"
        driver.get(url)
        self.first_book = driver.find_elements(*BasketLocators.choose_book)[0]
        self.basket_btn = driver.find_element(*BasketLocators.basket_btn)
        self.basket_book_name = driver.find_element(*BasketLocators.basket_book_name)
        time.sleep(3)

    def get_first_book_name(self):
        self.first_book.find_element("product-title.large-name").get_text()

    def click_on_the_first_book(self):
        self.first_book.click()

    def btn_basket_click(self):
        self.basket_btn.click()

    def get_basket_book_name(self):
        self.basket_book_name.text()

    def refresh_basket_page(self):
        self.get_cart_link()
