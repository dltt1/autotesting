from selenium.webdriver.common.by import By
import random

CURRENCY_LIST = [
    'Узбекский сум',
    'Белорусский рубль',
    'Казахстанский тенге',
    'Армянский драм',
    'Киргизский сом'
]

# тестовое биба
class CartLocators:

    # BUTTONS
    PAYING = (
        By.XPATH,
        f'//div[@class="basket-form__basket-section basket-section basket-pay '
        f'j-b-basket-payment basket-section--flex basket-section--error"]//p/a[1]'
    )
    MY_DATA = (
        By.XPATH,
        f'//div[@class ="basket-form__basket-section basket-section '
        f'j-b-basket-user-data basket-user-data basket-section--flex basket-section--error"]//p/a[1]'
    )
    CONFIRM_ORDER = (By.XPATH, '//button[@name="ConfirmOrderByRegisteredUser"]')
    HOW_TO_ORDER = (By.XPATH, '//section[@class="footer__list-wrap footer__list-wrap--buyers"]//li[1]/a')

    # ITEM
    ADD_ITEM = "document.getElementsByClassName('product-card__add-basket j-add-to-basket btn-main-sm')[0]"
    PLUS_ITEM_BUTTON = (By.XPATH, '//button[@class="count__plus plus"]')
    MINUS_ITEM_BUTTON = (By.XPATH, '//button[@class="count__minus minus"]')
    NUMBER_OF_ITEMS = (By.XPATH, '//div[@class="b-top__count line"]/span')
    TOTAL = (By.XPATH, '//p[@class="b-top__total line"]/span[2]')
    TOTAL_PRICE = (By.XPATH, '//div[@class="list-item__price"]/div[1]')

    # DELIVERY
    ADD_ADDRESS = (By.XPATH, '//div[@class="basket-delivery__choose-address j-btn-choose-address"]')
    BUTTON_FIRST_ADDRESS = (By.XPATH, '//div[@data-id="2249"]')
    BUTTON_ADD_ADDRESS = (By.XPATH, '//button[@class="details-self__btn btn-main"]')
    ADDRESS_IN_TEXT = (By.XPATH, '//span[@class="details-self__name-text"]')
    ADDED_ADDRESS_IN_TEXT = (By.XPATH, '//div[@class="selected-address__data"]/span[1]')

    # CURRENCY
    CURRENCY_MENU = (By.XPATH, '//li[@class="simple-menu__item j-b-header-country"]')
    CURRENCY = (By.XPATH, f'//span[text()="{random.choice(CURRENCY_LIST)}"]')
    CURRENCY_NOW = (By.XPATH, '//span[@class="simple-menu__currency"]')
