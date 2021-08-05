from pages.base_page import BasePage
from pages.locators import MenuLocators


import time, os


class MainBooks(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://www.labirint.ru"
        driver.get(url)
        self.menu_main = driver.find_element(*MenuLocators.menu_main_2021)
        time.sleep(3)

    def main_click(self):
        self.menu_main.click()

    time.sleep(3)