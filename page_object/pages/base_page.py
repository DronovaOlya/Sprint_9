import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import os

class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    @allure.step('Открыть главную страницу')
    def go_to_page(self, url):
        self.driver.get(url)

    @allure.step('Найти элемент')
    def wait_and_find_element(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Нажать на элемент')
    def click_to_element(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def wait_text(self, locator, text):
        self.wait.until_not(expected_conditions.text_to_be_present_in_element_value(locator, text))
        return self.driver.find_element(*locator).text

    @allure.step('Заполнить поле ввода')
    def add_text_to_element(self, locator, text):
        self.wait_and_find_element(locator).send_keys(text)

    def get_text_to_element(self, locator):
        return self.wait_and_find_element(locator).text

    @allure.step('Загрузить файл на сервер')
    def upload_file(self, file_path, locator):
        assert os.path.exists(file_path), f"Файл не найден: {file_path}"
        absolute_path = os.path.abspath(file_path)
        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        element.send_keys(absolute_path)

