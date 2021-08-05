from pages.menu_household_page import MenuHouseholdPage
import time


def test_menu_household(selenium):
    page = MenuHouseholdPage(selenium)
    page.btn_menu_household_click()
    page.btn_switch_to_soap()
    page.btn_switch_to_other()
    page.btn_switch_to_tissues()
    page.btn_switch_to_tooth_paste()

    time.sleep(5)