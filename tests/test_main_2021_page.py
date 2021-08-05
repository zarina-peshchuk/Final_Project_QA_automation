from pages.main_books_page import MainBooks
import time


def test_menu(selenium):
    page = MainBooks(selenium)
    page.main_click()

    assert len(page.get_main_2021_link()) > 0

    time.sleep(5)