from selenium.webdriver.common.by import By


class AuthLocators:
    AUTH_NAME = (By.CLASS_NAME, "formvalidate-error")
    AUTH_BTN = (By.ID, "g-recap-0-btn")
    AUTH_CODE = (By.CLASS_NAME, "full-input__input")
    AUTH_BTN_CODE = (By.CLASS_NAME, "js-submit-by-code")
    AUTH_EXIT = (By.CSS_SELECTOR, "div.popup-window-content.user-top-menu-cont.user-top-menu-link_logout")


class SearchLocators:
    search_field = (By.ID, "search-field")
    search_btn = (By.CLASS_NAME, "b-header-b-search-e-btn")
    search_field_in_games = (By.CSS_SELECTOR, "navisort-find-here__find.js-navisort-analytics")
    search_btn_in_games = (By.XPATH, "//input[@value='Найти здесь']")
    search_positive_result = (By.XPATH, "//*[contains(text(),'Все, что мы нашли в Лабиринте по запросу')]")
    search_negative_result = (By.XPATH, "//*[contains(text(),'Мы ничего не нашли по вашему запросу! Что делать?')]")


class MenuLocators:
    menu_books = (By.LINK_TEXT, "Книги")
    menu_main_2021 = (By.LINK_TEXT, "Главное 2021")
    menu_school = (By.LINK_TEXT, "Школа")
    filters_school_type_mtr = (By.XPATH,".bl-name[@text='Типы материалов']")
    filters_school_subject = (By.XPATH, ".checkbox-ui[@text='Математика']")
    menu_games = (By.LINK_TEXT, "Игрушки")
    menu_office = (By.LINK_TEXT, "Канцтовары")
    menu_household = (By.LINK_TEXT, "Товары для дома")
    scroll_banners = (By.CLASS_NAME, "fotorama__arr--next")
    genre_adventure = (By.LINK_TEXT, "Приключения. Лучшие книги для детей")
    top_read = (By.LINK_TEXT, "Что почитать: выбор редакции")
    number_of_top_read_books = (By.CLASS_NAME, "navisort-head-text")


class ClubLocators:
    menu_club = (By.LINK_TEXT, "Клуб")
    labirint_now = (By.LINK_TEXT, "Лабиринт. Сейчас")
    number_of_labirint_now_books = (By.CLASS_NAME, "js-b-goodssets-finded-e-count")
    booklympics = (By.CLASS_NAME, "b-goodssets-head-e-button")
    child_now = (By.LINK_TEXT, "Детский навигатор")
    news = (By.LINK_TEXT, "Новости Лабиринта")
    news_books = (By.LINK_TEXT, "Книжные обзоры")
    reviews = (By.LINK_TEXT, "Рецензии читателей")
    recommendations = (By.LINK_TEXT, "Подборки читателей")
    journals = (By.LINK_TEXT, "Литературные журналы")
    award = (By.LINK_TEXT, "Литературные премии")
    list_of_awards = (By.CLASS_NAME, "grid-list-name")
    certificates = (By.LINK_TEXT, "Подарочные сертификаты")
    lit_tests = (By.LINK_TEXT, "Литтесты")


class FiltersClubLocators:
    mood_funny = (By.CLASS_NAME, "b-goodssets-tags-e-tag-1")
    mood_sad = (By.CLASS_NAME, "b-goodssets-tags-e-tag-2")
    mood_inspiration = (By.CLASS_NAME, "b-goodssets-tags-e-tag-3")
    mood_scary = (By.CLASS_NAME, "b-goodssets-tags-e-tag-4")
    about_love = (By.CLASS_NAME, "b-goodssets-tags-e-tag-5")
    about_investigations = (By.CLASS_NAME, "b-goodssets-tags-e-tag-133")
    about_loneliness = (By.CLASS_NAME, "b-goodssets-tags-e-tag-6")
    about_cinema = (By.CLASS_NAME, "b-goodssets-tags-e-tag-7")
    about_health = (By.CLASS_NAME, "b-goodssets-tags-e-tag-8")
    about_family = (By.CLASS_NAME, "b-goodssets-tags-e-tag-10")
    about_incredible = (By.CLASS_NAME, "b-goodssets-tags-e-tag-11")
    about_business = (By.CLASS_NAME, "b-goodssets-tags-e-tag-12")
    about_history = (By.CLASS_NAME, "b-goodssets-tags-e-tag-13")
    about_creativity = (By.CLASS_NAME, "b-goodssets-tags-e-tag-24")
    about_personal_growth = (By.CLASS_NAME, "b-goodssets-tags-e-tag-25")
    result_filters = (By.CLASS_NAME, "b-goodssets-finded-tags")


class BasketLocators:
    choose_book = (By.CSS_SELECTOR, "cover")
    basket_btn = (By.CLASS_NAME, "btn-buy")
    click_book_for_delete_from_basket = (By.CSS_SELECTOR, "b-product-check.checkbox-ui")
    delete_book = (By.LINK_TEXT, "Удалить")
    basket_book_name = (By.CSS_SELECTOR, "product-title")


class SwitchitemsLocators:
    switch_to_checked = (By.CSS_SELECTOR, "radioitems .checked")
    switch_to_table = (By.CSS_SELECTOR, "radioitems .view-table")
    btn_next = (By.CLASS_NAME, "pagination-next__text")
    btn_to_begin = (By.CLASS_NAME, "to-begin")
    btn_load_more = (By.CLASS_NAME, "pushstate")


class CategoriesLocators:
    soap = (By.LINK_TEXT, "Мыло")
    other = (By.LINK_TEXT, "Другое")
    tooth_paste = (By.LINK_TEXT, "Паста зубная")
    tissues = (By.LINK_TEXT, "Салфетки влажные")


class ProductBuyAreaLocators:
    put_first_book = (By.CLASS_NAME, "icon-fave ")
    add_to_cart = (By.CLASS_NAME, "product-buy")
    else_actions_first_book = (By.XPATH, "//.icon-compare[@aria-describedby='qtip-1']")
    else_actions_second_book = (By.XPATH, "//.icon-compare[@aria-describedby='qtip-3']")
    compare_btn = (By.XPATH, "//*[@id='body-top']//.js-card-block-actions-compare")
    put_btn = (By.CLASS_NAME, "b-header-b-personal-e-text")
    choose_book_from_put_for_delete = (By.CLASS_NAME, "test_basket_page.py")
    delete_book_from_put = (By.LINK_TEXT, "Удалить")


class MyLabirintLocators:
    my_labirint = (By.CSS_SELECTOR, "div.top-link-main_cabinet.js-b-autofade-wrap.b-header-b-personal-e-icon-wrapper")
    orders = (By.XPATH, "//*[text()='Заказы']")
    coupons = (By.XPATH, "//*[text()='Купоны']")
    all_coupons = (By.CLASS_NAME, "cabinet-coupons")
    balance = (By.XPATH, "//*[text()='Баланс']")
    recommendation = (By.XPATH, "//*[text()='Рекомендации']")
    put_order = (By.XPATH, "//*[text()='Отложенные']")
    visited = (By.XPATH, "//*[text()='История просмотра']")
    compare = (By.XPATH, "//*[text()='Сравнение']")
    compare_books = (By.CLASS_NAME, "compare-container__item__name")
    comments = (By.XPATH, "//*[contains(text(),'Рецензии')]")
    personal_default = (By.XPATH, "//*[contains(text(),'Мои данные')]")


class SocialNetworkLocators:
    Instagram = (By.CLASS_NAME, "b-header-b-social-e-icon-m-inst")
    Youtube = (By.CLASS_NAME, "b-header-b-social-e-icon-m-yt")
    Vkontakte = (By.CLASS_NAME, "b-header-b-social-e-icon-m-vk")
    Facebook = (By.CLASS_NAME, "b-header-b-social-e-icon-m-fb")


class LeftPanelLocators:
    book_cashback = (By.XPATH, "//.action-block[@data-position='1']")
    top_sale = (By.XPATH, "//.action-block[@data-position='2']")
    top_knizhnaya_svyaz = (By.XPATH, "//.action-block[@data-position='3']")
    top_govori_fantaziruy = (By.XPATH, "//.action-block[@data-position='4']")
    additional_month_actions = (By.XPATH, "//.analytics-click-js[@data-event-type='211']")