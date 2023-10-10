import time

from pages.item_page import ItemPage
from conftest import driver


class TestItem:

    def test_add_and_del(self, driver):
        """ПРОВЕРКА ДОБАВЛЕНИЯ/УДАЛЕНИЯ ТОВАРА ИЗ КОРЗИНЫ"""
        item_page = ItemPage(driver, 'https://www.wildberries.ru/')
        item_page.open_js()
        time.sleep(5)
        assert item_page.add_and_del_item()[0] == 'В корзине пока пусто',\
            "Не получилось добавить/удалить товар, проверь тест"

    def test_correct_price(self, driver):
        """ПРОВЕРКА КОРРЕКТНОГО РАСЧЕТА ЦЕНЫ"""
        item_page = ItemPage(driver, 'https://www.wildberries.ru/')
        item_page.open_js()
        time.sleep(5)
        assert item_page.correct_price() == item_page.correct_total_price(),\
            "Проверка расчета цены в корзине сломалась"

    def test_click_buttons(self, driver):
        """ПРОВЕРКА ФУНКЦИОНАЛЬНОСТИ КНОПОК В КАРТОЧКЕ ТОВАРА"""
        item_page = ItemPage(driver, 'https://www.wildberries.ru/')
        item_page.open_js()
        time.sleep(5)
        assert item_page.correct_click_buttons() == 'DONE',\
            'Проверка кнопок сломалась'
