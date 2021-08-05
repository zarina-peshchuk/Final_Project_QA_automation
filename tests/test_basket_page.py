from pages.basket_page import BasketPage
from pages.auth_page import AuthPage
import time


def test_basket(selenium):
    page = BasketPage(selenium)
    first_book_name = page.get_first_book_name()
    page.click_on_the_first_book()
    page.btn_basket_click()
    basket_book_name = page.get_basket_book_name()

    assert first_book_name == basket_book_name
    time.sleep(5)


def test_basket_close(selenium):
    page = BasketPage(selenium)
    first_book_name = page.get_first_book_name()
    page.click_on_the_first_book()
    page.btn_basket_click()
    page.refresh_basket_page()
    basket_book_name = page.get_basket_book_name()

    assert first_book_name == basket_book_name


def test_basket_auth_user(selenium):
    page = AuthPage(selenium)
    page.enter_email("baidekenova2@gmail.com")
    page.btn_click()
    page.enter_code("D24C-4F6C-B84F")
    page.btn_code_click()
    page = BasketPage(selenium)
    first_book_name = page.get_first_book_name()
    page.click_on_the_first_book()
    page.btn_basket_click()
    basket_book_name = page.get_basket_book_name()

    assert first_book_name == basket_book_name
    time.sleep(5)


def test_basket_close_auth_user(selenium):
    page = AuthPage(selenium)
    page.enter_email("baidekenova2@gmail.com")
    page.btn_click()
    page.enter_code("D24C-4F6C-B84F")
    page.btn_code_click()
    page = BasketPage(selenium)
    first_book_name = page.get_first_book_name()
    page.click_on_the_first_book()
    page.btn_basket_click()
    page.refresh_basket_page()
    basket_book_name = page.get_basket_book_name()

    assert first_book_name == basket_book_name