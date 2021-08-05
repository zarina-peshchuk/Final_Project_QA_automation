from pages.base_page import BasePage
from pages.locators import MenuLocators


import time, os


class SchoolPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://www.labirint.ru"
        driver.get(url)
        self.menu_school_btn = driver.find_element(*MenuLocators.menu_school)
        self.filters_type = driver.find_element(*MenuLocators.filters_school_type_mtr)
        self.filters_type_subject = driver.find_element(*MenuLocators.filters_school_subject)
        time.sleep(3)

    def btn_school_click(self):
        self.menu_school_btn.click()

    def btn_school_type_mtr_click(self):
        self.filters_type.click()

    def btn_subject(self):
        self.filters_type_subject.click()
    time.sleep(3)