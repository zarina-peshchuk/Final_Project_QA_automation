from pages.base_page import BasePage
from pages.locators import AuthLocators


import time, os


class AuthPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://www.labirint.ru/cabinet/"
        driver.get(url)
        self.enter_values = driver.find_element(*AuthLocators.AUTH_NAME)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.code = driver.find_element(*AuthLocators.AUTH_CODE)
        self.btn_code = driver.find_element(*AuthLocators.AUTH_BTN_CODE)
        self.btn_exit = driver.find_element(*AuthLocators.AUTH_EXIT)
        time.sleep(3)

    def enter_email(self, value):
        self.enter_values.clear()
        self.enter_values.send_keys(value)

    def btn_click(self):
        self.btn.click()

    def enter_code(self, value):
        self.code.send_keys(value)

    def btn_code_click(self, value):
        self.btn_code.click()

    def btn_exit(self):
        self.btn_exit.click()
    time.sleep(3)