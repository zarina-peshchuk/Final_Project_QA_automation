from pages.base_page import BasePage
from pages.locators import MenuLocators, SearchLocators


import time, os


class MenuGames(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://www.labirint.ru"
        driver.get(url)
        self.menu_games = driver.find_element(*MenuLocators.menu_games)
        self.search_field_in_games = driver.find_element(*SearchLocators.search_field_in_games)
        time.sleep(3)
        self.btn_search_field_in_games = driver.find_element(*SearchLocators.search_btn_in_games)
        self.check_btn_search_without_words_in_field = driver.find_element(*SearchLocators.search_field_in_games)

    def menu_games_click(self):
        self.menu_games.click()

    def enter_word_in_games(self, value):
        self.search_field_in_games.click()
        self.search_field_in_games.clear()
        self.search_field_in_games.send_keys(value)

    def btn_search_in_games(self):
        self.btn_search_field_in_games.click()

    def clear_field(self):
        self.check_btn_search_without_words_in_field.click()
        self.check_btn_search_without_words_in_field.clear()

    def is_btn_clickable(self):
        return self.btn_search_field_in_games.is_clickable()

    time.sleep(3)