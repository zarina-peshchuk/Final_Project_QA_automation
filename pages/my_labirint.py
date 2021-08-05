from pages.base_page import BasePage
from pages.locators import MyLabirintLocators


import time, os


class MyLabirintPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://www.labirint.ru/"
        driver.get(url)
        self.my_labirint = driver.find_element(*MyLabirintLocators.my_labirint)
        self.coupons = driver.find_elements(*MyLabirintLocators.coupons)
        self.all_coupons = driver.find_element(*MyLabirintLocators.all_coupons)
        self.balance = driver.find_element(*MyLabirintLocators.balance)
        self.recommendation = driver.find_element(*MyLabirintLocators.recommendation)
        self.put_order = driver.find_element(*MyLabirintLocators.put_order)
        self.visited = driver.find_element(*MyLabirintLocators.visited)
        self.compare = driver.find_element(*MyLabirintLocators.compare)
        self.comments = driver.find_element(*MyLabirintLocators.comments)
        self.personal_default = driver.find_element(*MyLabirintLocators.personal_default)
        time.sleep(3)

    def my_labirint_click(self):
        self.my_labirint.click()

    def coupons_click(self):
        self.coupons.click()

    def get_all_coupons(self):
        self.all_coupons.getAttribute()
        self.all_coupons.screenshot('123.png')

    def balance_click(self):
        self.balance.click()

    def recommendation_click(self):
        self.recommendation.click()

    def put_order_click(self):
        self.put_order.click()

    def visited_click(self):
        self.visited.click()

    def compare_click(self):
        self.compare.click()

    def comments_click(self):
        self.comments.click()

    def personal_default_click(self):
        self.personal_default.click()
