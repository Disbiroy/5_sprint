import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utils.generators import generate_email, generate_password, generate_name


class TestNavigation:
    def test_navigate_to_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        main_page = MainPage(driver)
        main_page.click_login_button()

        login_page = LoginPage(driver)
        login_page.click_register_link()

        from pages.registration_page import RegistrationPage
        registration_page = RegistrationPage(driver)
        name = generate_name()
        email = generate_email()
        password = generate_password()
        registration_page.register(name, email, password)

        login_page.login(email, password)

        main_page.click_personal_account_button()

        profile_page = ProfilePage(driver)
        assert profile_page.is_profile_page()

    def test_navigate_from_profile_to_constructor_via_button(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        main_page = MainPage(driver)
        main_page.click_login_button()

        login_page = LoginPage(driver)
        login_page.click_register_link()

        from pages.registration_page import RegistrationPage
        registration_page = RegistrationPage(driver)
        name = generate_name()
        email = generate_email()
        password = generate_password()
        registration_page.register(name, email, password)

        login_page.login(email, password)
        main_page.click_personal_account_button()

        profile_page = ProfilePage(driver)
        profile_page.click_constructor_link()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_navigate_from_profile_to_constructor_via_logo(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        main_page = MainPage(driver)
        main_page.click_login_button()

        login_page = LoginPage(driver)
        login_page.click_register_link()

        from pages.registration_page import RegistrationPage
        registration_page = RegistrationPage(driver)
        name = generate_name()
        email = generate_email()
        password = generate_password()
        registration_page.register(name, email, password)

        login_page.login(email, password)
        main_page.click_personal_account_button()

        main_page.click_logo()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"