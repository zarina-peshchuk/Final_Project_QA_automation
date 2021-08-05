from urllib.parse import urlparse


class BasePage(object):
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def get_cart_link(self):
        url_cart = urlparse('https://www.labirint.ru/cart/')
        return url_cart.path

    def get_books_link(self):
        url_menu = urlparse('https://www.labirint.ru/books/')
        return url_menu.path

    def get_main_2021_link(self):
        url_main_2021 = urlparse('https://www.labirint.ru/best/')
        return url_main_2021.path