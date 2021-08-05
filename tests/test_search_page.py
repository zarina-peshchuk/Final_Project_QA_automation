from pages.search_page import SearchPage
import time


def test_search(selenium):
    page = SearchPage(selenium)
    page.enter_word("детские")
    page.btn_search_click()

    assert page.get_relative_link() != '/search/детские/?stype=0', "error"

    time.sleep(5)


def test_numbers_search(selenium):
    page = SearchPage(selenium)
    page.enter_word("123456789")
    page.btn_search_click()

    assert page.contain_text_in_search() == 'Все, что мы нашли в Лабиринте по запросу'


def test_negative_many_words_search(selenium):
    page = SearchPage(selenium)
    page.enter_word("привет пока детские женские романы канцтовары")
    page.btn_search_click()

    assert page.contain_text_in_search() == 'Мы ничего не нашли по вашему запросу! Что делать?'


def test_negative_any_symbols_search(selenium):
    page = SearchPage(selenium)
    page.enter_word("dfghjkl12358/*-+")
    page.btn_search_click()

    assert page.contain_text_in_search() == 'Мы ничего не нашли по вашему запросу! Что делать?'

