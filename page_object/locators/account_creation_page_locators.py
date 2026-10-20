from selenium.webdriver.common.by import By

class AccountCreationPageLocators:

    LOCATOR_BUTTON_CREATE_ACCOUNT = By.XPATH, "//*[@class='style_link__1kPh8 styles_menuButton__1RUEF' and text()='Создать аккаунт']"

    LOCATOR_INPUT_FIRST_NAME = By.XPATH, ".//input[@name='first_name']"

    LOCATOR_INPUT_LAST_NAME = By.XPATH, ".//input[@name='last_name']"

    LOCATOR_INPUT_USERNAME = By.XPATH, ".//input[@name='username']"

    LOCATOR_INPUT_EMAIL = By.XPATH, ".//input[@name='email']"

    LOCATOR_INPUT_PASSWORD = By.XPATH, ".//input[@name='password']"

    LOCATOR_BUTTON_CREATE_ACCOUNT_FORM = By.XPATH, ".//button[@class='style_button__1FFWl styles_button__146Sy style_button_style_dark-blue__1cpq7' and text()='Создать аккаунт']"


