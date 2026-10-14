import allure
from page_object.locators.creating_repo_page_locators import CreatingRepoPageLocators
from page_object.pages.base_page import BasePage



class CreatingRepoPage(BasePage):
    @allure.step('Нажать на таб "Создать рецепт"')
    def click_tab_create_repo(self):
        self.click_to_element(CreatingRepoPageLocators.LOCATOR_TAB_CREATE_RECIPE)

    @allure.step('Нажать на кнопку "Создать рецепт"')
    def click_button_create_repo(self):
        self.click_to_element(CreatingRepoPageLocators.LOCATOR_BUTTON_CRAETE_RECIPE)

    @allure.step('Заполнить поля формы создания рецепта')
    def set_fields_recipe_creation_form(self, data, file_path):
        self.add_text_to_element(CreatingRepoPageLocators.LOCATOR_NAME_RECIPE_CREATE, data['recipe_title'])
        self.click_to_element(CreatingRepoPageLocators.LOCATOR_TEG_LUNCH)
        self.click_to_element(CreatingRepoPageLocators.LOCATOR_TEG_DINNER)
        self.add_text_to_element(CreatingRepoPageLocators.LOCATOR_INPUT_INGREDIENT, data['ingredient'])
        self.click_to_element(CreatingRepoPageLocators.LOCATOR_INGREDIENT)
        self.add_text_to_element(CreatingRepoPageLocators.LOCATOR_INPUT_WEIGHT, data['weight'])
        self.click_to_element(CreatingRepoPageLocators.LOCATOR_CREAT_INGREDIENT)
        self.add_text_to_element(CreatingRepoPageLocators.LOCATOR_INPUT_COOKING_TIME, data['time'])
        self.add_text_to_element(CreatingRepoPageLocators.LOCATOR_TEXTAREA_RECIPE_DESCRIPTION, data['description'])
        self.upload_file(file_path, CreatingRepoPageLocators.LOCATOR_FILE_DOWNLOADS)
