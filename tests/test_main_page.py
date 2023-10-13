import time

from pages.main_page import MainPage


class TestMainPage:

    def test_geo(self, driver):
        """ПРОВЕРКА РАБОТЫ КАРТЫ"""
        main_page = MainPage(driver, 'https://www.wildberries.ru/')
        main_page.open()
        time.sleep(5)
        assert main_page.geolocation() == "DONE",\
            'Тест отображения карты не сооветсвует ожидаемому результату'

    def test_correct_search(self, driver):
        """
        ПРОВЕРКА КОРРЕКТНОГО ПОИСКА
        (при тестировании разного поиска меняй в результате тоже)
        """
        main_page = MainPage(driver, 'https://www.wildberries.ru/')
        main_page.open()
        time.sleep(5)
        assert main_page.search_correct('Рубашка') != f'Ничего не нашлось по запросу «Рубашка»',\
            "Отображение корректного поиска не соответсвует ожидаемому результату"

    def test_incorrect_search(self, driver):
        """ПРОВЕРКА НЕКОРРЕКТНОГО ПОИСКА"""
        main_page = MainPage(driver, 'https://www.wildberries.ru/')
        main_page.open()
        time.sleep(5)
        assert main_page.search_incorrect('////////////////////////////') == 'Ничего не нашлось по запросу «////////////////////////////»',\
            "Отображение некорректного поиска не соответсвует ожидаемому результату"

    def test_burger_menu(self, driver):
        """ПРОВЕРКА ОТКРЫТИЯ И ОТОБРАЖЕНИЯ БУРГЕР МЕНЮ"""
        main_page = MainPage(driver, 'https://www.wildberries.ru/')
        main_page.open()
        time.sleep(5)
        main_page.burger()
        assert main_page.result_burger_categories()[0] == 'Женщинам',\
            'Открытие "бургер-меню" и отображение категорий не соответсвует ожидаемому результату'

    def test_currency(self, driver):
        """ПРОВЕРКА ОТОБРАЖЕНИЯ КОРРЕКТНОЙ ВАЛЮТЫ"""
        main_page = MainPage(driver, 'https://www.wildberries.ru/')
        main_page.open()
        time.sleep(5)
        main_page.search_correct('Рубашка')
        assert len(main_page.correct_currency()) == 3,\
            'Проверка отображения корректной не соответсвует ожидаемому результату'

    def test_incorrect_phone(self, driver):
        """ПРОВЕРКА НЕКОРРЕКТНОГО ТЕЛЕФОНА ЦИФРАМИ (p.s. ТАМ КАПЧА)"""
        main_page = MainPage(driver, 'https://www.wildberries.ru/')
        main_page.open()
        assert main_page.form_login_incorrect() == 'Введите код с картинки',\
            "Проверка ввода некорректного телефона не соответсвует ожидаемому результату"

    def test_incorrect_phone_with_words(self, driver):
        """ПРОВЕРКА НЕКОРРЕКТНОГО ТЕЛЕФОНА БУКВАМИ"""
        main_page = MainPage(driver, 'https://www.wildberries.ru/')
        main_page.open()
        assert main_page.form_login_with_words() == 'Введите номер, чтобы получить код',\
            'Проверка ввода букв в строку телефона не соответсвует ожидаемому результату'
