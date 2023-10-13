import time
from pages.shopping_cart import CartPage


class TestCartPage:

    def test_correct_buttons(self, driver):
        """ПРОВЕРКА РАБОТЫ КНОПОК"""
        cart_page = CartPage(driver, 'https://www.wildberries.ru/lk/basket')
        cart_page.open_js()
        time.sleep(5)
        assert cart_page.correct_work_buttons() == 'DONE',\
            'Проверка функциональности кнопок не прошла'

    def test_correct_item(self, driver):
        """ПРОВЕРКА ДОБАВЛЕНИЯ/УДАЛЕНИЯ ТОВАРА В/ИЗ КОРЗИНУ/Ы"""
        cart_page = CartPage(driver, 'https://www.wildberries.ru/lk/basket')
        cart_page.open_js()
        time.sleep(5)
        assert cart_page.add_item_to_cart_more_then_one() == cart_page.total_price_in_cart(),\
            'Не получилось добавить/удалить товар'

    def test_add_address_for_delivery(self, driver):
        """ПРОВЕРКА ДОБАВЛЕНИЯ АДРЕССА"""
        cart_page = CartPage(driver, 'https://www.wildberries.ru/lk/basket')
        cart_page.open_js()
        time.sleep(5)
        assert cart_page.add_address() == cart_page.result_address(),\
            'Отображение адреса не соответсвует ожидаемому результату'

    def test_correct_max_item(self, driver):
        """
        ПРОВЕРКА ДОБАВЛЕНИЯ МАКСИМАЛЬНОГО ЧИСЛА ТОВАРОВ
        МАКСИМАЛЬНО - 255 шт.
        """
        cart_page = CartPage(driver, 'https://www.wildberries.ru/lk/basket')
        cart_page.open_js()
        time.sleep(5)
        assert cart_page.add_max_item() == cart_page.result_max_item(),\
            "Проверка добавления максимального значения не соответсвует ожидаемому результату"

    def test_correct_currency(self, driver):
        """ПРОВЕРКА ПРАВИЛЬНОСТИ ОТОБРАЖЕНИЯ ВАЛЮТЫ"""
        cart_page = CartPage(driver, 'https://www.wildberries.ru/lk/basket')
        cart_page.open_js()
        time.sleep(3)
        assert cart_page.correct_currency() == cart_page.result_currency(), \
            'Проверка отображения корректной не соответсвует ожидаемому результату'
