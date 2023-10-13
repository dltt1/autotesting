import time

from pages.base_page import BasePage
from locators.shopping_cart_locators import CartLocators as Cart


class CartPage(BasePage):

    def correct_work_buttons(self):
        element = self.driver.execute_script(
            f"return {Cart.ADD_ITEM};"
        )
        self.driver.execute_script("arguments[0].click();", element)
        self.click(Cart.PLUS_ITEM_BUTTON, 5)
        self.click(Cart.PLUS_ITEM_BUTTON, 6)
        self.click(Cart.MINUS_ITEM_BUTTON, 6)
        self.click(Cart.CONFIRM_ORDER, 6)
        self.click(Cart.PAYING, 7)
        self.driver.execute_script("window.history.go(-1)")
        self.click(Cart.MY_DATA, 7)
        self.driver.execute_script("window.history.go(-1)")
        self.click(Cart.HOW_TO_ORDER, 8)
        self.driver.execute_script("window.history.go(-1)")
        return 'DONE'

    def add_item_to_cart_more_then_one(self):
        element = self.driver.execute_script(
            f"return {Cart.ADD_ITEM};"
        )
        self.driver.execute_script("arguments[0].click();", element)
        self.click(Cart.PLUS_ITEM_BUTTON, 5)
        self.click(Cart.PLUS_ITEM_BUTTON, 5)
        self.click(Cart.MINUS_ITEM_BUTTON, 8)
        time.sleep(5)
        return self.element_is_visible(Cart.TOTAL_PRICE, 8).text

    def total_price_in_cart(self):
        return self.element_is_visible(Cart.TOTAL, 8).text

    def add_address(self):
        element = self.driver.execute_script(
            f"return {Cart.ADD_ITEM};"
        )
        self.driver.execute_script("arguments[0].click();", element)
        self.click(Cart.ADD_ADDRESS, 5)
        self.click(Cart.BUTTON_FIRST_ADDRESS, 10)
        result = [self.element_is_visible(Cart.ADDRESS_IN_TEXT, 8).text]
        self.click(Cart.BUTTON_ADD_ADDRESS, 8)
        return result[0]

    def result_address(self):
        return self.element_is_visible(Cart.ADDED_ADDRESS_IN_TEXT, 8).text[:-1]

    def add_max_item(self):
        element = self.driver.execute_script(
            f"return {Cart.ADD_ITEM};"
        )
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        price = int(self.element_is_visible(Cart.TOTAL_PRICE, 8).text[:-1].replace(' ', '')) * 255
        while True:
            if self.element_is_visible(Cart.NUMBER_OF_ITEMS, 8).text == 'Товары, 255 шт.':
                break
            else:
                self.click(Cart.PLUS_ITEM_BUTTON, 5)
        time.sleep(5)
        return price

    def result_max_item(self):
        return int(self.element_is_visible(Cart.TOTAL, 8).text[:-1].replace(' ', ''))

    def correct_currency(self):
        element = self.driver.execute_script(
            f"return {Cart.ADD_ITEM};"
        )
        self.driver.execute_script("arguments[0].click();", element)
        self.move_to_el(Cart.CURRENCY_MENU, 8)
        self.click(Cart.CURRENCY, 6)
        if self.element_is_visible(Cart.CURRENCY_NOW, 7).text == 'UZS':
            return self.element_is_visible(Cart.TOTAL, 7).text[-3:]
        elif self.element_is_visible(Cart.CURRENCY_NOW, 7).text == 'BYN':
            return self.element_is_visible(Cart.TOTAL, 7).text[-2:]
        elif self.element_is_visible(Cart.CURRENCY_NOW, 7).text == 'KZT':
            return self.element_is_visible(Cart.TOTAL, 7).text[-3:]
        elif self.element_is_visible(Cart.CURRENCY_NOW, 7).text == 'AMD':
            return self.element_is_visible(Cart.TOTAL, 7).text[-4:]
        elif self.element_is_visible(Cart.CURRENCY_NOW, 7).text == 'KGS':
            return self.element_is_visible(Cart.TOTAL, 7).text[-3:]

    def result_currency(self):
        if self.element_is_visible(Cart.CURRENCY_NOW, 7).text == 'UZS':
            return 'сум'
        elif self.element_is_visible(Cart.CURRENCY_NOW, 7).text == 'BYN':
            return 'р.'
        elif self.element_is_visible(Cart.CURRENCY_NOW, 7).text == 'KZT':
            return 'тг.'
        elif self.element_is_visible(Cart.CURRENCY_NOW, 7).text == 'AMD':
            return 'драм'
        elif self.element_is_visible(Cart.CURRENCY_NOW, 7).text == 'KGS':
            return 'сом'
