from pages.compare_page import ComparePage
from pages.auth_page import AuthPage
import time


def test_basket(selenium):
    page = ComparePage(selenium)
    first_book_name = page.get_first_book_name()
    second_book_name = page.get_second_book_name()
    page.click_else_btn_first_book()
    page.click_compare_btn()
    page.click_else_btn_second_book()
    page.click_compare_btn()
    page.click_go_to_compare()

    assert first_book_name == page.first_book_name_in_compare
    assert second_book_name == page.second_book_name_in_compare

    time.sleep(5)