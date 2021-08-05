from pages.Left_panel_page import LeftpanelPage
import time


def test_btn_book_cashback(selenium):
    page = LeftpanelPage(selenium)
    page.btn_book_cashback_click()


def test_btn_top_sale(selenium):
    page = LeftpanelPage(selenium)
    page.btn_top_sale_click()


def test_btn_top_knizhnaya_svyaz(selenium):
    page = LeftpanelPage(selenium)
    page.btn_top_knizhnaya_svyaz_click()


def test_btn_top_govori_fantaziruy(selenium):
    page = LeftpanelPage(selenium)
    page.btn_top_govori_fantaziruy_click()


def test_btn_additional_month_actions(selenium):
    page = LeftpanelPage(selenium)
    page.btn_additional_month_actions_click()

    time.sleep(5)
