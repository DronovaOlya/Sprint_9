import allure
from page_object.data import DATA_REG, page_auth
from page_object.locators.authorization_page_locators import AuthorizationPageLocators
from page_object.urls import URL_MAIN_PAGE

@allure.epic('Создание пользователя')
class TestAccountCreationPage:
    @allure.title('Создание пользователя')
    def test_create_user(self, account_creation_page, authorization_page):
        account_creation_page.go_to_page(URL_MAIN_PAGE)
        account_creation_page.click_button_create_account()
        account_creation_page.set_fields_registration_form(DATA_REG)
        account_creation_page.click_button_create_account_form()


        assert page_auth in account_creation_page.get_text_to_element(AuthorizationPageLocators.LOCATOR_PAGE_AUTH)
        check = authorization_page.wait_and_find_element(AuthorizationPageLocators.LOCATOR_FORM_AUTH)
        assert check.is_displayed()