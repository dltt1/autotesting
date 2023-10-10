import time

from pages.main_page import MainPage
from conftest import driver


class TestMainPage:

    # def test_main_page_button(self, driver):
    #     main_page = MainPage(driver, 'https://www.wildberries.ru/')
    #     main_page.open()
    #     time.sleep(5)
    #     main_page.click_button()
    #     time.sleep(5)

    # def test_main_page_buttons(self, driver):
    #     main_page = MainPage(driver, 'https://www.wildberries.ru/')
    #     main_page.open()
    #     time.sleep(5)
    #     main_page.click_buttons()
    #     time.sleep(5)

    def test_geo(self, driver):
        """ПРОВЕРКА РАБОТЫ КАРТЫ"""
        main_page = MainPage(driver, 'https://www.wildberries.ru/')
        main_page.open()
        time.sleep(5)
        assert main_page.geolocation() == "DONE",\
            'Тест отображения карты не прошел'

    def test_correct_search(self, driver):
        """
        ПРОВЕРКА КОРРЕКТНОГО ПОИСКА
        (при тестировании разного поиска меняй в результате тоже)
        """
        main_page = MainPage(driver, 'https://www.wildberries.ru/')
        main_page.open()
        time.sleep(5)
        assert main_page.search_correct('Рубашка') != f'Ничего не нашлось по запросу «Рубашка»', "Поиск не корректный"

    def test_incorrect_search(self, driver):
        """ПРОВЕРКА НЕКОРРЕКТНОГО ПОИСКА"""
        main_page = MainPage(driver, 'https://www.wildberries.ru/')
        main_page.open()
        time.sleep(5)
        assert main_page.search_incorrect('//-/-142/412-4/-') == 'Ничего не нашлось по запросу «//-/-142/412-4/-»',\
            "Проверка не сработала"

    def test_burger_menu(self, driver):
        """ПРОВЕРКА ОТКРЫТИЯ И ОТОБРАЖЕНИЯ БУРГЕР МЕНЮ"""
        main_page = MainPage(driver, 'https://www.wildberries.ru/')
        main_page.open()
        time.sleep(5)
        main_page.burger()
        assert main_page.result_burger_categories()[0] == 'Женщинам', 'последовательность категорий сломалась'

    def test_currency(self, driver):
        """ПРОВЕРКА ОТОБРАЖЕНИЯ КОРРЕКТНОЙ ВАЛЮТЫ"""
        main_page = MainPage(driver, 'https://www.wildberries.ru/')
        main_page.open()
        time.sleep(5)
        main_page.search_correct('Рубашка')
        assert len(main_page.correct_currency()) == 3,\
            'Проверка отображения корректной валюты сломалась'

    def test_incorrect_phone(self, driver):
        """ПРОВЕРКА НЕКОРРЕКТНОГО ТЕЛЕФОНА ЦИФРАМИ (p.s. ТАМ КАПЧА)"""
        main_page = MainPage(driver, 'https://www.wildberries.ru/')
        main_page.open()
        assert main_page.form_login_incorrect() == 'Введите код с картинки',\
            "Тест с проверкой телефона сломался"

    def test_incorrect_phone_with_words(self, driver):
        """ПРОВЕРКА НЕКОРРЕКТНОГО ТЕЛЕФОНА БУКВАМИ"""
        main_page = MainPage(driver, 'https://www.wildberries.ru/')
        main_page.open()
        assert main_page.form_login_with_words() == 'Введите номер, чтобы получить код',\
            'Проверка буквами входа в ЛК сломалась'

    # def test_test(self, driver):
    #     main_page = MainPage(driver, 'https://www.wildberries.ru/lk/basket')
    #     main_page.open()
    #     time.sleep(5)
    #     print(main_page.title_test())
