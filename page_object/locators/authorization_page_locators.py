from selenium.webdriver.common.by import By

class AuthorizationPageLocators:
    LOCATOR_BUTTON_ENTER = By. XPATH, "//*[@class='style_link__1kPh8 styles_menuLink__3a59I' and text()='Войти']"

    LOCATOR_BUTTON_ENTER_FORM = By.XPATH, ".//button[@class='style_button__1FFWl styles_button__1jD3X style_button_style_dark-blue__1cpq7' and text()='Войти']"

    LOCATOR_INPUT_EMAIL = By.XPATH, ".//input[@name='email']"

    LOCATOR_INPUT_PASSWORD = By.XPATH, ".//input[@name='password']"

    LOCATOR_MAIN_PAGE = By. XPATH, "//*[@class='styles_title__2fhty' and text()='Рецепты']"
    
    LOCATOR_BUTTON_EXIT = By. XPATH, "//*[@class='styles_menuLink__3a59I' and text()='Выход']"

    LOCATOR_PAGE_AUTH = By. XPATH, "//*[@class='styles_title__2fhty' and text()='Войти на сайт']"
   
    LOCATOR_FORM_AUTH = By. XPATH, "//*[@class='styles_form__2nwxz styles_form__2_42b']"

    LOCATOR_TAB_RECIPE = By. XPATH, "//*[@class='style_link__1kPh8 style_nav__link__2rAY6' and text()='Рецепты']"
    