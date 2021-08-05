from pages.put_books_aside_page import PutPage
from pages.auth_page import AuthPage
import time


def test_put(selenium):
    page = PutPage(selenium)
    first_book_name = page.get_first_book_name()
    page.put_first_book()
    page.put_btn_click()
    put_book_name = page.get_put_book_name()

    assert page.get_cart_link != '0'
    assert first_book_name == put_book_name
    time.sleep(5)

    page.btn_choose_book_from_put()
    page.btn_delete_book_from_put()


def test_put_auth_user(selenium):
    page = AuthPage(selenium)
    page.enter_email("baidekenova2@gmail.com")
    page.btn_click()
    page.enter_code("D24C-4F6C-B84F")
    page.btn_code_click()
    page = PutPage(selenium)
    first_book_name = page.get_first_book_name()
    page.put_first_book()
    page.put_btn_click()
    put_book_name = page.get_put_book_name()

    assert first_book_name == put_book_name

    page.btn_choose_book_from_put()
    page.btn_delete_book_from_put()


def test_put_auth_user(selenium):
    page = AuthPage(selenium)
    page.enter_email("baidekenova2@gmail.com")
    page.btn_click()
    page.enter_code("D24C-4F6C-B84F")
    page.btn_code_click()
    page = PutPage(selenium)
    first_book_name = page.get_first_book_name()
    page.put_first_book()
    page.put_btn_click()
    put_book_name = page.get_put_book_name()

    assert first_book_name == put_book_name

    page.btn_choose_book_from_put()
    page.btn_delete_book_from_put()
