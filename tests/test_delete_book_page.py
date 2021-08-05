from pages.basket_delete_page import DeletePage
from pages.auth_page import AuthPage
import time


def test_search(selenium):
    page = DeletePage(selenium)
    page.click_the_first_book_for_delete()
    page.btn_delete_basket_click()


def test_search_auth_user(selenium):
    page = AuthPage(selenium)
    page.enter_email("baidekenova2@gmail.com")
    page.btn_click()
    page.enter_code("D24C-4F6C-B84F")
    page.btn_code_click()
    page = DeletePage(selenium)
    page.click_the_first_book_for_delete()
    page.btn_delete_basket_click()

    time.sleep(5)