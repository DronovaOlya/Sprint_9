import allure
from page_object.data import DATA_RECIPE, FILE_FOR_UPLOAD
from page_object.locators.creating_repo_page_locators import CreatingRepoPageLocators

@allure.epic('Создание рецепта')
class TestCreatingRepoPage:
    @allure.title('Создание рецепта')
    def test_create_recipe(self, auth_user, creating_repo_page):
        creating_repo_page.click_tab_create_repo()
        creating_repo_page.set_fields_recipe_creation_form(DATA_RECIPE, FILE_FOR_UPLOAD)
        creating_repo_page.click_button_create_repo()


        check = creating_repo_page.wait_and_find_element(CreatingRepoPageLocators.LOCATOR_CARD_CREATE_RECIPE)
        assert check.is_displayed()

        assert DATA_RECIPE['recipe_title'] in creating_repo_page.get_text_to_element(CreatingRepoPageLocators.LOCATOR_NAME_RECIPE)