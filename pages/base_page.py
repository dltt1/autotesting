from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """ОТКРЫВАЕМ СТРАНИЦУ ПО URL"""
        self.driver.get(self.url)

    def open_js(self):
        """ОТКРЫТИЕ ПО URL JAVA SCRIPT"""
        self.driver.execute_script(f"window.open('{self.url}', '_self');")

    def element_is_visible(self, locator, timeout=5):
        """УСЛОВИЕ = ЕСЛИ ЭЛЕМЕНТ ВИДЕН НА СТРАНИЦЕ"""
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        """УСЛОВИЕ = ЕСЛИ ЭЛЕМЕНТЫ ВИДНЫ НА СТРАНИЦЕ"""
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def move_to_el(self, locator, timeout=5):
        """ПЕРЕДВИЖЕНИЕ КУРСОРА НА ЭЛЕМЕНТ"""
        element = Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return ActionChains(self.driver).move_to_element(element).perform()

    def move_in_page_by_pexels(self, pexels: int):
        """ПЕРЕДВИГАЕМ СТРАНИЦУ ПО ПИКСЕЛЯМ"""
        scroll_by = f'window.scrollBy(0, {pexels});'
        self.driver.execute_script(scroll_by)

    def get_attribute(self, locator, attribute,timeout=5):
        element = Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element.get_attribute(attribute)
