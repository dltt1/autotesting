import time

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Main
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):

    def geolocation(self):
        self.click(Main.GEO, 8)
        return 'DONE' if self.element_is_visible(Main.MAP, 8) else 'NONE'

    def burger(self):
        self.click(Main.BURGER_MENU, 8)
        self.move_to_el(Main.BURGER_CONTAINER, 8)

    def result_burger_categories(self):
        result_categories = self.elements_are_visible(Main.BURGER_MENU_CATEGORIES, 5)
        return [i.text for i in result_categories]

    def search_correct(self, item: str):
        shirt = self.element_is_visible(Main.SEARCH, 5)
        shirt.click()
        shirt.send_keys(item)
        shirt.send_keys(Keys.ENTER)
        result_search = [i.text for i in self.elements_are_visible(Main.SEARCH_RESULT, 8)][0]
        return result_search

    def search_incorrect(self, item):
        shirt = self.element_is_visible(Main.SEARCH, 5)
        shirt.click()
        shirt.send_keys(item)
        shirt.send_keys(Keys.ENTER)
        result_search = [i.text for i in self.elements_are_visible(Main.SEARCH_RESULT_NOT_FOUND, 8)][0]
        return result_search

    def form_login_incorrect(self):
        self.click(Main.LOGIN, 5)
        self.element_is_visible(Main.PHONE, 5).send_keys('0000000000')
        self.click(Main.REQ_CODE, 5)
        time.sleep(5)
        return self.element_is_visible(Main.CAPTCHA, 8).text

    def form_login_with_words(self):
        self.click(Main.LOGIN, 5)
        self.element_is_visible(Main.PHONE, 5).send_keys('aaaaaa')
        self.click(Main.REQ_CODE, 5)
        return self.element_is_visible(Main.ERROR_MESSAGE, 5).text

    def correct_currency(self):
        self.move_to_el(Main.CURRENCY_MENU, 5)
        self.click(Main.CURRENCY, 5)
        return self.element_is_visible(Main.CURRENCY_NOW, 5).text
