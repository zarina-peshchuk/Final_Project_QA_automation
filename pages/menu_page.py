from pages.base_page import BasePage
from pages.locators import MenuLocators, SwitchitemsLocators


import time, os


class CheckMenuPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://www.labirint.ru"
        driver.get(url)
        self.menu_btn = driver.find_element(*MenuLocators.menu_books)
        self.flick_banners = driver.find_element(*MenuLocators.scroll_banners)
        self.genre_adventure = driver.find_element(*MenuLocators.genre_adventure)
        self.btn_next = driver.find_element(*SwitchitemsLocators.btn_next)
        self.top_read = driver.find_element(*MenuLocators.top_read)
        self.number_of_top_read_books = driver.find_element(*MenuLocators.number_of_top_read_books)
        time.sleep(3)

    def btn_menu_books_click(self):
        self.menu_btn.click()

    def btn_flick_banners_click(self):
        self.flick_banners.click(4)

    def scroll_to_element(self):
        self.genre_adventure.scroll_to_element()

    def screenshot(self):
        self.genre_adventure.save_screenshot('Adventure.png')

    def btn_genre_adventure_click(self):
        self.genre_adventure.click()
        self.genre_adventure.scroll_down()

    def btn_next_click(self):
        self.btn_next.click()

    def top_read_click(self):
        self.top_read.click()

    def number_of_top_read_books(self):
        self.number_of_top_read_books.get_text()

    time.sleep(3)