from pages.menu_school_page import SchoolPage
import time


def test_menu_school(selenium):
    page = SchoolPage(selenium)
    page.btn_school_click()
    page.btn_school_type_mtr_click()
    page.btn_subject()

    time.sleep(5)