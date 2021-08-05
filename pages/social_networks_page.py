from pages.base_page import BasePage
from pages.locators import SocialNetworkLocators


import time, os


class SocialNetworksPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://www.labirint.ru"
        driver.get(url)
        self.Instagram = driver.find_element(*SocialNetworkLocators.Instagram)
        self.Youtube = driver.find_element(*SocialNetworkLocators.Youtube)
        self.Vkontakte = driver.find_element(*SocialNetworkLocators.Vkontakte)
        self.Facebook = driver.find_element(*SocialNetworkLocators.Facebook)
        time.sleep(3)

    def btn_Instagram_click(self):
        self.Instagram.click()

    def btn_Youtube_click(self):
        self.Youtube.click()

    def btn_Vkontakte_click(self):
        self.Vkontakte.click()

    def btn_Facebook_click(self):
        self.Facebook.click()

    time.sleep(3)