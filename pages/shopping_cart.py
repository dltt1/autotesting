import time

from pages.base_page import BasePage
from locators.shopping_cart_locators import CartLocators as Cart
from selenium.webdriver.common.keys import Keys


class CartPage(BasePage):

    def correct_work_buttons(self):
        element = self.driver.execute_script(
            f"return {Cart.ADD_ITEM};"
        )
        self.driver.execute_script("arguments[0].click();", element)
        self.element_is_visible(Cart.PLUS_ITEM_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(Cart.PLUS_ITEM_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(Cart.MINUS_ITEM_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(Cart.CONFIRM_ORDER).click()
        time.sleep(2)
        self.element_is_visible(Cart.PAYING).click()
        time.sleep(2)
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(2)
        self.element_is_visible(Cart.MY_DATA).click()
        time.sleep(2)
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(3)
        self.element_is_visible(Cart.HOW_TO_ORDER).click()
        time.sleep(2)
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(2)
        return 'DONE'

    def add_item_to_cart_more_then_one(self):
        element = self.driver.execute_script(
            f"return {Cart.ADD_ITEM};"
        )
        self.driver.execute_script("arguments[0].click();", element)
        self.element_is_visible(Cart.PLUS_ITEM_BUTTON).click()
        self.element_is_visible(Cart.PLUS_ITEM_BUTTON).click()
        time.sleep(2)
        self.element_is_visible(Cart.MINUS_ITEM_BUTTON).click()
        time.sleep(2)
        return self.element_is_visible(Cart.TOTAL_PRICE).text

    def total_price_in_cart(self):
        return self.element_is_visible(Cart.TOTAL).text

    def add_address(self):
        element = self.driver.execute_script(
            f"return {Cart.ADD_ITEM};"
        )
        self.driver.execute_script("arguments[0].click();", element)
        self.element_is_visible(Cart.ADD_ADDRESS).click()
        time.sleep(4)
        self.element_is_visible(Cart.BUTTON_FIRST_ADDRESS).click()
        time.sleep(3)
        result = [self.element_is_visible(Cart.ADDRESS_IN_TEXT).text]
        self.element_is_visible(Cart.BUTTON_ADD_ADDRESS).click()
        time.sleep(3)
        return result[0]

    def result_address(self):
        return self.element_is_visible(Cart.ADDED_ADDRESS_IN_TEXT).text[:-1]

    def add_max_item(self):
        element = self.driver.execute_script(
            f"return {Cart.ADD_ITEM};"
        )
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        price = int(self.element_is_visible(Cart.TOTAL_PRICE).text[:-1].replace(' ', '')) * 255
        time.sleep(2)
        while True:
            if self.element_is_visible(Cart.NUMBER_OF_ITEMS).text == 'Товары, 255 шт.':
                break
            else:
                self.element_is_visible(Cart.PLUS_ITEM_BUTTON).click()
        time.sleep(2)
        return price

    def result_max_item(self):
        return int(self.element_is_visible(Cart.TOTAL).text[:-1].replace(' ', ''))

    def correct_currency(self):
        element = self.driver.execute_script(
            f"return {Cart.ADD_ITEM};"
        )
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        self.move_to_el(Cart.CURRENCY_MENU)
        time.sleep(1)
        self.element_is_visible(Cart.CURRENCY).click()
        time.sleep(2)
        if self.element_is_visible(Cart.CURRENCY_NOW).text == 'UZS':
            return self.element_is_visible(Cart.TOTAL).text[-3:]
        elif self.element_is_visible(Cart.CURRENCY_NOW).text == 'BYN':
            return self.element_is_visible(Cart.TOTAL).text[-2:]
        elif self.element_is_visible(Cart.CURRENCY_NOW).text == 'KZT':
            return self.element_is_visible(Cart.TOTAL).text[-3:]
        elif self.element_is_visible(Cart.CURRENCY_NOW).text == 'AMD':
            return self.element_is_visible(Cart.TOTAL).text[-4:]
        elif self.element_is_visible(Cart.CURRENCY_NOW).text == 'KGS':
            return self.element_is_visible(Cart.TOTAL).text[-3:]

    def result_currency(self):
        if self.element_is_visible(Cart.CURRENCY_NOW).text == 'UZS':
            return 'сум'
        elif self.element_is_visible(Cart.CURRENCY_NOW).text == 'BYN':
            return 'р.'
        elif self.element_is_visible(Cart.CURRENCY_NOW).text == 'KZT':
            return 'тг.'
        elif self.element_is_visible(Cart.CURRENCY_NOW).text == 'AMD':
            return 'драм'
        elif self.element_is_visible(Cart.CURRENCY_NOW).text == 'KGS':
            return 'сом'