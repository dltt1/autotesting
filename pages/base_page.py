from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import allure


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """ОТКРЫВАЕМ СТРАНИЦУ ПО URL"""
        with allure.step(f'Открываю страницу {self.url}'):
            self.driver.get(self.url)

    def open_js(self):
        """ОТКРЫТИЕ ПО URL JAVA SCRIPT"""
        with allure.step('Открываю страницу с работой JAVA SCRIPT'):
            self.driver.execute_script(f"window.open('{self.url}', '_self');")

    def element_is_visible(self, locator, timeout):
        """УСЛОВИЕ = ЕСЛИ ЭЛЕМЕНТ ВИДЕН НА СТРАНИЦЕ"""
        with allure.step('Проверяю на видимость элемента на странице'):
            return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout):
        """УСЛОВИЕ = ЕСЛИ ЭЛЕМЕНТЫ ВИДНЫ НА СТРАНИЦЕ"""
        with allure.step('Проверяю на видимость элементов на странице'):
            return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def move_to_el(self, locator, timeout):
        """ПЕРЕДВИЖЕНИЕ КУРСОРА НА ЭЛЕМЕНТ"""
        with allure.step(f'Навожу курсор на элемент {locator}'):
            element = self.element_is_visible(locator, timeout)
            return ActionChains(self.driver).move_to_element(element).perform()

    def move_in_page_by_pexels(self, pexels: int):
        """ПЕРЕДВИГАЕМ СТРАНИЦУ ПО ПИКСЕЛЯМ"""
        with allure.step(f'Передвинул страницу на {pexels} пикселей'):
            scroll_by = f'window.scrollBy(0, {pexels});'
            self.driver.execute_script(scroll_by)

    def get_attribute(self, locator, attribute, timeout):
        """ПОЛУЧЕНИЕ АТРИБУТА ЭЛЕМЕНТА HTML"""
        with allure.step(f'Получил текст атрибута элемента'):
            element = self.element_is_visible(locator, timeout)
            return element.get_attribute(attribute)

    def click(self, locator, timeout):
        """НАЖАТИЕ НА ВИДИМЫЙ ЭЛЕМЕНТ"""
        with allure.step(f'Нажал на элемент {locator}'):
            return self.element_is_visible(locator, timeout).click()
