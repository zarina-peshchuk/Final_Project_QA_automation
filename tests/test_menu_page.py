from pages.menu_page import CheckMenuPage
import time


def test_menu_books(selenium):
    page = CheckMenuPage(selenium)
    page.btn_menu_books_click()

    assert page.get_books_link() != '0', 'error'

    time.sleep(5)


def test_banners(selenium):
    page = CheckMenuPage(selenium)
    page.btn_flick_banners_click()


def test_scroll_to_element(selenium):
    page = CheckMenuPage(selenium)
    page.scroll_to_element()
    page.screenshot()


def test_check_btn_next(selenium):
    page = CheckMenuPage(selenium)
    page.scroll_to_element()
    page.screenshot()
    page.btn_genre_adventure_click()
    page.btn_next_click()


def test_number_of_top_read_books(selenium):
    page = CheckMenuPage(selenium)
    page.top_read_click()

    assert len(page.number_of_top_read_books()) != 0


