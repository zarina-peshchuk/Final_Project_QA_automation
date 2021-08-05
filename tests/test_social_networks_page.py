from pages.social_networks_page import SocialNetworksPage
import time


def test_btn_Instagram(selenium):
    page = SocialNetworksPage(selenium)
    page.btn_Instagram_click()


def test_btn_Youtube(selenium):
    page = SocialNetworksPage(selenium)
    page.btn_Youtube_click()


def test_btn_Vkontakte(selenium):
    page = SocialNetworksPage(selenium)
    page.btn_Vkontakte_click()


def test_btn_Facebook(selenium):
    page = SocialNetworksPage(selenium)
    page.btn_Facebook_click()

    time.sleep(5)
