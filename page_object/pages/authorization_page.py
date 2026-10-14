import allure
from page_object.locators.authorization_page_locators import AuthorizationPageLocators
from page_object.pages.base_page import BasePage

class AuthorizationPage(BasePage):
    @allure.step('Нажать на кнопку "Войти"')
    def click_button_enter(self):
        self.click_to_element(AuthorizationPageLocators.LOCATOR_BUTTON_ENTER)

    @allure.step('Заполнить поля формы авторизации')
    def set_fields_auth_form(self, data):
        self.add_text_to_element(AuthorizationPageLocators.LOCATOR_INPUT_EMAIL, data['email'])
        self.add_text_to_element(AuthorizationPageLocators.LOCATOR_INPUT_PASSWORD, data['password'])


    @allure.step('Нажать на кнопку "Войти" на форме авторизации')
    def click_button_enter_form(self):
        self.click_to_element(AuthorizationPageLocators.LOCATOR_BUTTON_ENTER_FORM)

    @allure.step('Нажать на кнопку "Рецепты"')
    def click_button_recipe(self):
        self.click_to_element(AuthorizationPageLocators.LOCATOR_TAB_RECIPE)