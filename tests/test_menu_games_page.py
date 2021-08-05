from pages.menu_games_page import MenuGames
import time


def test_menu_games(selenium):
    page = MenuGames(selenium)
    page.menu_games_click()
    page.enter_word_in_games("домино")
    page.btn_search_in_games()

    assert page.get_books_link() != '0', 'error'

    page.check_btn_search_without_words_in_field()
    page.btn_search_field_in_games()

    assert page.is_btn_enabled()

    time.sleep(5)