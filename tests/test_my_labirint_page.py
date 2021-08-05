from pages.my_labirint import MyLabirintPage
import time


def test_coupons_click(selenium):
    page = MyLabirintPage(selenium)
    page.my_labirint_click()
    page.coupons_click()
    page.get_all_coupons()

def test_balance_click(selenium):
    page = MyLabirintPage(selenium)
    page.my_labirint_click()
    page.balance_click()

def test_recommendation_click(selenium):
    page = MyLabirintPage(selenium)
    page.my_labirint_click()
    page.recommendation_click()

def test_put_order_click(selenium):
    page = MyLabirintPage(selenium)
    page.my_labirint_click()
    page.put_order_click()

def test_visited_click(selenium):
    page = MyLabirintPage(selenium)
    page.my_labirint_click()
    page.visited_click()

def test_compare_click(selenium):
    page = MyLabirintPage(selenium)
    page.my_labirint_click()
    page.compare_click()

def test_comments_click(selenium):
    page = MyLabirintPage(selenium)
    page.my_labirint_click()
    page.comments_click()

def test_personal_default_click(selenium):
    page = MyLabirintPage(selenium)
    page.my_labirint_click()
    page.personal_default_click()