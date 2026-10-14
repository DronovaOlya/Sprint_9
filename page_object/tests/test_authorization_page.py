import allure
from page_object.data import DATA_AUTH
from page_object.locators.authorization_page_locators import AuthorizationPageLocators
from page_object.urls import URL_MAIN_PAGE

@allure.epic('Авторизация пользователя')
class TestAuthorizationPage:
    @allure.title('Авторизация пользователя')
    def test_auth_user(self, authorization_page):
        authorization_page.go_to_page(URL_MAIN_PAGE)
        authorization_page.click_button_recipe()
        authorization_page.click_button_enter()
        authorization_page.set_fields_auth_form(DATA_AUTH)
        authorization_page.click_button_enter_form()


        check = authorization_page.wait_and_find_element(AuthorizationPageLocators.LOCATOR_MAIN_PAGE)
        assert check.is_displayed()

        check_exit = authorization_page.wait_and_find_element(AuthorizationPageLocators.LOCATOR_BUTTON_EXIT)
        assert check_exit.is_displayed()