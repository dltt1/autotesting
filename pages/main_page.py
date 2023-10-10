import time

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Main
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):

    # def click_button(self):
    #     while True:
    #         self.element_is_visible(Main.BUTTON_PAGINATION).click()
    #
    # def click_buttons(self):
    #     self.element_is_visible(Main.BUTTON).click()
    #     time.sleep(5)
    #     # self.element_is_visible(Main.BURGER_MENU).click()
    #     # self.element_is_visible(Main.BURGER_MENU_CATEGORIES).click()
    #     # self.element_is_visible(Main.CURRENCY).click()
    #     # self.element_is_visible(Main.GEO).click()
    #     # self.element_is_visible(Main.SWIPE).click()
    #     # self.element_is_visible(Main.SLIDE).click()
    #     # self.element_is_visible(Main.TOP_ITEM).click()
    #     self.element_is_visible(Main.LOGIN).click()

    def geolocation(self):
        self.element_is_visible(Main.GEO).click()
        time.sleep(3)
        return 'DONE' if self.element_is_visible(Main.MAP) else 'NONE'

    def burger(self):
        self.element_is_visible(Main.BURGER_MENU).click()
        self.move_to_el(Main.BURGER_CONTAINER)

    def result_burger_categories(self):
        result_categories = self.elements_are_visible(Main.BURGER_MENU_CATEGORIES)
        return [i.text for i in result_categories]

    def search_correct(self, item: str):
        shirt = self.element_is_visible(Main.SEARCH)
        shirt.click()
        shirt.send_keys(item)
        shirt.send_keys(Keys.ENTER)
        result_search = [i.text for i in self.elements_are_visible(Main.SEARCH_RESULT)][0]
        return result_search

    def search_incorrect(self, item):
        shirt = self.element_is_visible(Main.SEARCH)
        shirt.click()
        shirt.send_keys(item)
        shirt.send_keys(Keys.ENTER)
        result_search = [i.text for i in self.elements_are_visible(Main.SEARCH_RESULT_NOT_FOUND)][0]
        time.sleep(1)
        return result_search

    def form_login_incorrect(self):
        self.element_is_visible(Main.LOGIN).click()
        self.element_is_visible(Main.PHONE).send_keys('0000000000')
        self.element_is_visible(Main.REQ_CODE).click()
        time.sleep(1)
        return self.element_is_visible(Main.CAPTCHA).text

    def form_login_with_words(self):
        self.element_is_visible(Main.LOGIN).click()
        self.element_is_visible(Main.PHONE).send_keys('aaaaaa')
        self.element_is_visible(Main.REQ_CODE).click()
        return self.element_is_visible(Main.ERROR_MESSAGE).text

    def correct_currency(self):
        self.move_to_el(Main.CURRENCY_MENU)
        self.element_is_visible(Main.CURRENCY).click()
        return self.element_is_visible(Main.CURRENCY_NOW).text

    # def title_test(self):
    #     return self.get_attribute(Main.MAIN_CONTAINER, 'data-link')