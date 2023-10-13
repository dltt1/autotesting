import time

from pages.base_page import BasePage
from locators.item_locators import ItemLocators as Item


class ItemPage(BasePage):

    def add_and_del_item(self):
        self.click(Item.FIRST_SALE_BUTTON, 8)
        self.click(Item.ITEM_ID, 8)
        self.click(Item.ADD_TO_CART, 8)
        self.click(Item.GO_TO_CART, 8)
        self.move_to_el(Item.OLD_PRICE_IN_CART, 8)
        self.click(Item.DEL_ITEM_FROM_CART, 8)
        empty = [self.element_is_visible(Item.EMPTY_CART, 8).text]
        return empty

    def correct_price(self):
        self.click(Item.FIRST_SALE_BUTTON, 5)
        self.click(Item.ITEM_ID, 8)
        self.click(Item.ADD_TO_CART, 5)
        first_item_price = int(self.element_is_visible(Item.ITEM_PRICE, 5).text[:-2].replace(' ', ''))
        self.driver.execute_script("window.history.go(-1)")
        self.click(Item.ITEM_SECOND_ID, 6)
        self.click(Item.ADD_TO_CART, 5)
        second_item_price = int(self.element_is_visible(Item.ITEM_PRICE, 5).text[:-2].replace(' ', ''))
        total = first_item_price + second_item_price
        self.click(Item.GO_TO_CART, 6)
        time.sleep(5)
        return total

    def correct_total_price(self):
        return int(self.element_is_visible(Item.TOTAL,5).text[:-2].replace(' ', ''))

    def correct_click_buttons(self):
        self.click(Item.FIRST_SALE_BUTTON, 5)
        self.click(Item.ITEM_ID, 8)
        self.click(Item.ITEM_IMAGE, 8)
        self.click(Item.NEXT_IMAGE, 7)
        self.click(Item.NEXT_IMAGE, 6)
        self.click(Item.CLOSE_IMAGE, 6)
        self.click(Item.SELLER, 6)
        time.sleep(2)
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(2)
        self.move_in_page_by_pexels(1000)
        self.click(Item.IMAGE_REVIEW, 8)
        self.click(Item.CLOSE_IMAGE, 6)
        time.sleep(1)
        self.move_in_page_by_pexels(300)
        self.click(Item.ALL_REVIEWS, 8)
        time.sleep(2)
        return 'DONE'

