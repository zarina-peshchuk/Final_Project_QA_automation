from pages.club_page import ClubPage
import time


def test_labirint_now(selenium):
    page = ClubPage(selenium)
    page.labirint_now_click()

    assert page.number_of_labirint_now_books_get_text() != '0'

    page.filter_funny_click()
    page.filter_inspiration_click()
    results = page.get_result_filters()

    # Проверяем наличие текстов "смешных" и "вдохновляющих" на странице, после применения фильтров
    assert "смешных" and "вдохновляющих" in results


# Проверяем кликабельность ссылки на "книжные игры"
def test_booklympics(selenium):
    page = ClubPage(selenium)
    page.booklympics_click()


# Проверяем кликабельность ссылки на "детский навигатор" и кнопки "в начало"
def test_child_now(selenium):
    page = ClubPage(selenium)
    page.child_now_click()
    page.btn_to_begin_click()


def test_news(selenium):
    page = ClubPage(selenium)
    page.news_click()


def test_news_books(selenium):
    page = ClubPage(selenium)
    page.news_books_click()


def test_reviews(selenium):
    page = ClubPage(selenium)
    page.reviews_click()


def test_recommendations(selenium):
    page = ClubPage(selenium)
    page.recommendations_click()


def test_journals(selenium):
    page = ClubPage(selenium)
    page.journals_click()
    page.btn_load_more_scroll_and_click()


def test_award(selenium):
    page = ClubPage(selenium)
    page.award_click()
    elements = page.get_list_of_awards()

    assert "Нобелевская премия" and "Ясная поляна" in elements


def test_certificates(selenium):
    page = ClubPage(selenium)
    page.certificates_click()


def test_lit_tests(selenium):
    page = ClubPage(selenium)
    page.lit_tests_click()

    time.sleep(5)

