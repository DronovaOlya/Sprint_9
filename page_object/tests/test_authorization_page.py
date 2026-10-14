import allure
from page_object.data import DATA_AUTH
from page_object.locators.authorization_page_locators import AuthorizationPageLocators
from page_object.urls import URL_MAIN_PAGE

@allure.epic('Авторизация пользователя')
class TestAuthorizationPage:
    @allure.title('Авторизация пользователя')
    def test_auth_user(self, auth_user):

        check = auth_user.wait_and_find_element(AuthorizationPageLocators.LOCATOR_MAIN_PAGE)
        assert check.is_displayed()

        check_exit = auth_user.wait_and_find_element(AuthorizationPageLocators.LOCATOR_BUTTON_EXIT)
        assert check_exit.is_displayed()