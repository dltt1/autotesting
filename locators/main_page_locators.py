from selenium.webdriver.common.by import By
import random

CURRENCY_LIST = [
    'Узбекский сум',
    'Белорусский рубль',
    'Казахстанский тенге',
    'Армянский драм',
    'Киргизский сом'
]


class MainPageLocators:

    # SEARCH
    SEARCH = (By.CSS_SELECTOR, '#searchInput')
    SEARCH_RESULT = (By.XPATH, '//div[@class="searching-results__inner"]//span[1]')
    SEARCH_RESULT_NOT_FOUND = (By.XPATH, '//h1[@class="not-found-search__title"]')

    # BURGER MENU
    BURGER_MENU = (By.XPATH, '//button[@data-wba-header-name="Catalog"]')
    BURGER_CONTAINER = (By.XPATH, '//div[@class="menu-burger__main j-menu-burger-main j-menu-active"]')
    BURGER_MENU_CATEGORIES = (
        By.XPATH,
        '//li[@class="menu-burger__main-list-item j-menu-main-item menu-burger__main-list-item--subcategory"]'
    )

    # CURRENCY
    CURRENCY_MENU = (By.XPATH, '//li[@class="simple-menu__item j-b-header-country"]')
    CURRENCY = (By.XPATH, f'//span[text()="{random.choice(CURRENCY_LIST)}"]')
    CURRENCY_NOW = (By.XPATH, '//span[@class="simple-menu__currency"]')

    # GEO
    GEO = (By.XPATH, '//li[@class="simple-menu__item j-geocity-wrap"]')
    MAP = (By.XPATH, '//div[@class="geo-block__map"]/ymaps/ymaps/ymaps/ymaps[1]')

    # AUTHORIZATION
    LOGIN = (By.XPATH, '//a[@data-wba-header-name="Login"]')
    PHONE = (By.XPATH, '//input[@class="input-item"]')
    ERROR_MESSAGE = (By.XPATH, '//span[@class="j-error-full-phone field-validation-error"]')
    REQ_CODE = (By.XPATH, '//button[@id="requestCode"]')
    CAPTCHA = (By.XPATH, '//h2[@class="sign-in-page__title"]')

