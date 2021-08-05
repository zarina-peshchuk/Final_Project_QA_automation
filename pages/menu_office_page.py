from pages.base_page import BasePage
from pages.locators import SwitchitemsLocators, MenuLocators


import time, os


class MenuOfficePage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://www.labirint.ru"
        driver.get(url)
        self.menu_office_btn = driver.find_element(*MenuLocators.menu_office)
        self.office_switch_to_table = driver.find_element(*SwitchitemsLocators.switch_to_table)
        self.office_switch_to_check = driver.find_element(*SwitchitemsLocators.switch_to_checked)
        time.sleep(3)

    def btn_office_click(self):
        self.menu_office_btn.click()

    def btn_office_switch_to_table(self):
        self.office_switch_to_table.click()

    def btn_office_switch_to_check(self):
        self.office_switch_to_check.click()

    time.sleep(3)