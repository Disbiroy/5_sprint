import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.profile_page import ProfilePage
from utils.generators import generate_email, generate_password, generate_name


class TestLogout:
    def test_logout_from_profile(self, driver):
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
        main_page.click_personal_account_button()

        profile_page = ProfilePage(driver)
        profile_page.click_logout_button()

        login_page = LoginPage(driver)
        assert login_page.is_login_page_opened()