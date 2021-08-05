from pages.menu_office_page import MenuOfficePage
import time


def test_menu_office(selenium):
    page = MenuOfficePage(selenium)
    page.btn_office_click()
    page.btn_office_switch_to_table()
    page.btn_office_switch_to_check()

    time.sleep(5)