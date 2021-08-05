from pages.base_page import BasePage
from pages.locators import MenuLocators, CategoriesLocators


import time, os


class MenuHouseholdPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://www.labirint.ru/household/"
        driver.get(url)
        self.menu_household_btn = driver.find_element(*MenuLocators.menu_household)
        self.switch_to_soap = driver.find_element(*CategoriesLocators.soap)
        self.switch_to_other = driver.find_element(*CategoriesLocators.other)
        self.switch_to_tissues = driver.find_element(*CategoriesLocators.tissues)
        self.switch_to_tooth_paste = driver.find_element(*CategoriesLocators.tooth_paste)
        time.sleep(3)

    def btn_menu_household_click(self):
        self.menu_household_btn.click()

    def btn_switch_to_soap(self):
        self.switch_to_soap.click()

    def btn_switch_to_other(self):
        self.switch_to_other.click()

    def btn_switch_to_tissues(self):
        self.switch_to_tissues.click()

    def btn_switch_to_tooth_paste(self):
        self.switch_to_tooth_paste.click()

    time.sleep(3)