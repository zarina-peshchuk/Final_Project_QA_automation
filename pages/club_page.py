from pages.base_page import BasePage
from pages.locators import ClubLocators, SwitchitemsLocators, FiltersClubLocators


import time, os


class ClubPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://www.labirint.ru/club/"
        driver.get(url)
        self.labirint_now = driver.find_element(*ClubLocators.labirint_now)
        self.number_of_labirint_now_books = driver.find_element(*ClubLocators.number_of_labirint_now_books)
        self.filter_funny = driver.find_element(*FiltersClubLocators.mood_funny)
        self.filter_inspiration = driver.find_element(*FiltersClubLocators.mood_inspiration)
        self.result_filters = driver.find_elements(*FiltersClubLocators.result_filters)
        self.booklympics = driver.find_element(*ClubLocators.booklympics)
        self.child_now = driver.find_element(*ClubLocators.child_now)
        self.btn_to_begin = driver.find_element(*SwitchitemsLocators.btn_to_begin)
        self.news = driver.find_element(*ClubLocators.news)
        self.news_books = driver.find_element(*ClubLocators.news_books)
        self.reviews = driver.find_element(*ClubLocators.reviews)
        self.recommendations = driver.find_element(*ClubLocators.recommendations)
        self.journals = driver.find_element(*ClubLocators.journals)
        self.btn_load_more = driver.find_element(*SwitchitemsLocators.btn_load_more)
        self.award = driver.find_element(*ClubLocators.award)
        self.list_of_awards = driver.find_elements(*ClubLocators.list_of_awards)
        self.certificates = driver.find_element(*ClubLocators.certificates)
        self.lit_tests = driver.find_element(*ClubLocators.lit_tests)

        time.sleep(3)

    def labirint_now_click(self):
        self.labirint_now.click()

    def number_of_labirint_now_books_get_text(self):
        self.number_of_labirint_now_books.get_text()

    def filter_funny_click(self):
        self.filter_funny.click()

    def filter_inspiration_click(self):
        self.filter_inspiration.click()

    def get_result_filters(self):
        self.result_filters.get_text()

    def booklympics_click(self):
        self.booklympics.click()

    def child_now_click(self):
        self.child_now.click()
        self.child_now.scroll_down()

    def btn_to_begin_click(self):
        self.btn_to_begin.click()

    def news_click(self):
        self.news.click()

    def news_books_click(self):
        self.news_books.click()

    def reviews_click(self):
        self.reviews.click()

    def recommendations_click(self):
        self.recommendations.click()

    def journals_click(self):
        self.journals.click()

    def btn_load_more_scroll_and_click(self):
        self.btn_load_more.scroll_to_element()
        self.btn_load_more.click()
        self.btn_load_more.save_screenshot('screenJournal.png')

    def award_click(self):
        self.award.click()

    def get_list_of_awards(self):
        self.list_of_awards.get_text()

    def certificates_click(self):
        self.certificates.click()

    def lit_tests_click(self):
        self.lit_tests.click()

    time.sleep(3)