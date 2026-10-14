import pytest
from selenium import webdriver
from page_object.pages.authorization_page import AuthorizationPage
from page_object.pages.account_creation_page import AccountCreationPage
from page_object.pages.creating_repo_page import CreatingRepoPage
from page_object.urls import URL_MAIN_PAGE
from selenium.webdriver import ChromeOptions
import os
from page_object.data import DATA_REG


@pytest.fixture(scope="function")
def driver():
    options = ChromeOptions()
    options.set_capability("acceptInsecureCerts", True)
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {"enableVideo": False})

    selenoid_url = os.getenv("SELENOID_URL", "http://localhost:4444/wd/hub")
    browser = webdriver.Remote(command_executor=selenoid_url, options=options)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def auth_user(driver, account_creation_page, authorization_page):
    account_creation_page.go_to_page(URL_MAIN_PAGE)
    account_creation_page.click_button_create_account()
    account_creation_page.set_fields_registration_form(DATA_REG)
    account_creation_page.click_button_create_account_form()

    authorization_page.go_to_page(URL_MAIN_PAGE)
    authorization_page.click_button_recipe()
    authorization_page.click_button_enter()
    authorization_page.set_fields_auth_form({
        'email': DATA_REG['username'],
        'password': DATA_REG['password'],
    })
    authorization_page.click_button_enter_form()

    return authorization_page

@pytest.fixture
def account_creation_page(driver):
    page = AccountCreationPage(driver)
    return page

@pytest.fixture
def authorization_page(driver):
    page = AuthorizationPage(driver)
    return page

@pytest.fixture
def creating_repo_page(driver):
    page = CreatingRepoPage(driver)
    return page