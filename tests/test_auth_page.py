from pages.auth_page import AuthPage
import time


def test_auth_page(selenium):
    page = AuthPage(selenium)
    page.enter_email("baidekenova2@gmail.com")
    page.btn_click()
    page.enter_code("D24C-4F6C-B84F")
    page.btn_code_click()

    assert page.get_relative_link() != '/cabinet/', "login error"

    time.sleep(5)