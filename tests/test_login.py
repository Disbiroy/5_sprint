import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.forgot_password_page import ForgotPasswordPage
from utils.generators import generate_email, generate_password, generate_name


class TestLogin:
    def test_login_from_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_login_button()

        login_page = LoginPage(driver)
        login_page.click_register_link()

        registration_page = RegistrationPage(driver)
        name = generate_name()
        email = generate_email()
        password = generate_password()
        registration_page.register(name, email, password)

        login_page.login(email, password)

        main_page_after_login = MainPage(driver)
        assert main_page_after_login.is_main_page_opened()

    def test_login_from_personal_account(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_personal_account_button()

        login_page = LoginPage(driver)
        assert login_page.is_login_page_opened()

    def test_login_from_registration_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_login_button()

        login_page = LoginPage(driver)
        login_page.click_register_link()

        registration_page = RegistrationPage(driver)
        registration_page.click_login_link()

        assert login_page.is_login_page_opened()

    def test_login_from_forgot_password_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_login_button()

        login_page = LoginPage(driver)
        login_page.click_forgot_password_link()

        forgot_password_page = ForgotPasswordPage(driver)
        assert forgot_password_page.is_forgot_password_page_opened()

        forgot_password_page.click_login_link()

        assert login_page.is_login_page_opened()