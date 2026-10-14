from selenium.webdriver.common.by import By

class CreatingRepoPageLocators:
    LOCATOR_TAB_CREATE_RECIPE = By.XPATH, "//*[@class='style_link__1kPh8 style_nav__link__2rAY6' and text()='Создать рецепт']"

    LOCATOR_BUTTON_CRAETE_RECIPE = By.XPATH, "//button[contains(@class, 'style_button') and text()='Создать рецепт']"

    LOCATOR_NAME_RECIPE_CREATE = By.XPATH, "//label[.//div[text()='Название рецепта']]//input"

    LOCATOR_TEG_LUNCH = By.XPATH, "//span[text()='Обед']/preceding-sibling::button"

    LOCATOR_TEG_DINNER = By.XPATH, "//span[text()='Ужин']/preceding-sibling::button"

    LOCATOR_INPUT_INGREDIENT = By.XPATH, ".//input[@class='styles_inputField__3eqTj styles_ingredientsInput__1zzql']"
   
    LOCATOR_INGREDIENT = By.XPATH, "//div[text()='блины готовые']"
   
    LOCATOR_INPUT_WEIGHT = By.XPATH, ".//input[@class='styles_inputField__3eqTj styles_ingredientsAmountValue__2matT']"

    LOCATOR_INPUT_COOKING_TIME = By.XPATH, "//label[.//div[text()='Время приготовления']]//input"

    LOCATOR_TEXTAREA_RECIPE_DESCRIPTION = By.XPATH, ".//textarea[@class='styles_textareaField__1wfhC']"

    LOCATOR_FILE_DOWNLOADS = By.CSS_SELECTOR, "input[type='file']"
    
    LOCATOR_CARD_CREATE_RECIPE = By.XPATH, ".//div[@class='styles_single-card__info__2_cny']"
    
    LOCATOR_NAME_RECIPE = By.XPATH, "//*[@class='styles_single-card__title__2QMPq']"

    LOCATOR_CREAT_INGREDIENT = By.XPATH, "//div[@class='styles_ingredientAdd__3fc32' and text()='Добавить ингредиент']"



    