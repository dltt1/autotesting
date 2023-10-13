import time
from pages.item_page import ItemPage
import allure


class TestItemPage:

    @allure.feature('Страница товара')
    @allure.story('Добавляю и удаляю товар')
    def test_add_and_del(self, driver):
        """ПРОВЕРКА ДОБАВЛЕНИЯ/УДАЛЕНИЯ ТОВАРА ИЗ КОРЗИНЫ"""
        item_page = ItemPage(driver, 'https://www.wildberries.ru/')
        item_page.open_js()
        time.sleep(5)
        with allure.step('Прогон теста'):
            assert item_page.add_and_del_item()[0] == 'В корзине пока пусто',\
                "Не получилось добавить/удалить товар"

    @allure.feature('Страница товара')
    @allure.story('Корректная цена')
    def test_correct_price(self, driver):
        """ПРОВЕРКА КОРРЕКТНОГО РАСЧЕТА ЦЕНЫ"""
        item_page = ItemPage(driver, 'https://www.wildberries.ru/')
        item_page.open_js()
        time.sleep(5)
        with allure.step('Прогон теста'):
            assert item_page.correct_price() == item_page.correct_total_price(),\
                "Проверка расчета цены не соответсвует ожидаемому результату"

    @allure.feature('Страница товара')
    @allure.story('Функциональность кнопок')
    def test_click_buttons(self, driver):
        """ПРОВЕРКА ФУНКЦИОНАЛЬНОСТИ КНОПОК В КАРТОЧКЕ ТОВАРА"""
        item_page = ItemPage(driver, 'https://www.wildberries.ru/')
        item_page.open_js()
        time.sleep(5)
        with allure.step('Прогон теста'):
            assert item_page.correct_click_buttons() == 'DONE',\
                'Проверка функциональности кнопок не прошла'
