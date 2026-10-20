import allure
from page_object.locators.account_creation_page_locators import AccountCreationPageLocators
from page_object.pages.base_page import BasePage


class AccountCreationPage(BasePage):
    @allure.step('Нажать на кнопку "Создать аккаунт"')
    def click_button_create_account(self):
        self.click_to_element(AccountCreationPageLocators.LOCATOR_BUTTON_CREATE_ACCOUNT)

    @allure.step('Заполнить поля формы регистрации')
    def set_fields_registration_form(self, data):
        self.add_text_to_element(AccountCreationPageLocators.LOCATOR_INPUT_FIRST_NAME, data['first_name'])
        self.add_text_to_element(AccountCreationPageLocators.LOCATOR_INPUT_LAST_NAME, data['last_name'])
        self.add_text_to_element(AccountCreationPageLocators.LOCATOR_INPUT_USERNAME, data['username'])
        self.add_text_to_element(AccountCreationPageLocators.LOCATOR_INPUT_EMAIL, data['email'])
        self.add_text_to_element(AccountCreationPageLocators.LOCATOR_INPUT_PASSWORD, data['password'])

    @allure.step('Нажать на кнопку "Создать аккаунт" на форме регистрации')
    def click_button_create_account_form(self):
        self.click_to_element(AccountCreationPageLocators.LOCATOR_BUTTON_CREATE_ACCOUNT_FORM)