import time

from pages.base_page import BasePage
from locators.item_locators import ItemLocators as Item


class ItemPage(BasePage):

    def add_and_del_item(self):
        self.element_is_visible(Item.FIRST_SALE_BUTTON).click()
        time.sleep(3)
        self.element_is_visible(Item.ITEM_ID).click()
        time.sleep(3)
        self.element_is_visible(Item.ADD_TO_CART).click()
        time.sleep(1)
        self.element_is_visible(Item.GO_TO_CART).click()
        time.sleep(2)
        self.move_to_el(Item.OLD_PRICE_IN_CART)
        time.sleep(1)
        self.element_is_visible(Item.DEL_ITEM_FROM_CART).click()
        time.sleep(1)
        empty = [self.element_is_visible(Item.EMPTY_CART).text]
        return empty

    def correct_price(self):
        self.element_is_visible(Item.FIRST_SALE_BUTTON).click()
        time.sleep(3)
        self.element_is_visible(Item.ITEM_ID).click()
        time.sleep(3)
        self.element_is_visible(Item.ADD_TO_CART).click()
        first_item_price = int(self.element_is_visible(Item.ITEM_PRICE).text[:-2].replace(' ', ''))
        time.sleep(1)
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(2)
        self.element_is_visible(Item.ITEM_SECOND_ID).click()
        time.sleep(1)
        self.element_is_visible(Item.ADD_TO_CART).click()
        second_item_price = int(self.element_is_visible(Item.ITEM_PRICE).text[:-2].replace(' ', ''))
        total = first_item_price + second_item_price
        time.sleep(1)
        self.element_is_visible(Item.GO_TO_CART).click()
        time.sleep(3)
        return total

    def correct_total_price(self):
        return int(self.element_is_visible(Item.TOTAL).text[:-2].replace(' ', ''))

    def correct_click_buttons(self):
        self.element_is_visible(Item.FIRST_SALE_BUTTON).click()
        time.sleep(3)
        self.element_is_visible(Item.ITEM_ID).click()
        time.sleep(3)
        self.element_is_visible(Item.ITEM_IMAGE).click()
        time.sleep(2)
        self.element_is_visible(Item.NEXT_IMAGE).click()
        time.sleep(1)
        self.element_is_visible(Item.NEXT_IMAGE).click()
        time.sleep(1)
        self.element_is_visible(Item.CLOSE_IMAGE).click()
        time.sleep(1)
        self.element_is_visible(Item.SELLER).click()
        time.sleep(2)
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(2)
        self.move_in_page_by_pexels(1000)
        time.sleep(3)
        self.element_is_visible(Item.IMAGE_REVIEW).click()
        time.sleep(1)
        self.element_is_visible(Item.CLOSE_IMAGE).click()
        time.sleep(1)
        self.move_in_page_by_pexels(300)
        self.element_is_visible(Item.ALL_REVIEWS).click()
        time.sleep(2)
        return 'DONE'

