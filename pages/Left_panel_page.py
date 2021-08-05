from pages.base_page import BasePage
from pages.locators import LeftPanelLocators


import time, os


class LeftpanelPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://www.labirint.ru"
        driver.get(url)
        self.book_cashback = driver.find_element(*LeftPanelLocators.book_cashback)
        self.top_sale = driver.find_element(*LeftPanelLocators.top_sale)
        self.top_knizhnaya_svyaz = driver.find_element(*LeftPanelLocators.top_knizhnaya_svyaz)
        self.top_govori_fantaziruy = driver.find_element(*LeftPanelLocators.top_govori_fantaziruy)
        self.additional_month_actions = driver.find_element(*LeftPanelLocators.additional_month_actions)
        time.sleep(3)

    def btn_book_cashback_click(self):
        self.book_cashback.click()

    def btn_top_sale_click(self):
        self.top_sale.click()

    def btn_top_knizhnaya_svyaz_click(self):
        self.top_knizhnaya_svyaz.click()

    def btn_top_govori_fantaziruy_click(self):
        self.top_govori_fantaziruy.click()

    def btn_additional_month_actions_click(self):
        self.additional_month_actions.click()

    time.sleep(3)