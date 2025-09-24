import pytest
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from utils.generators import generate_email, generate_password, generate_name


class TestRegistration:
    @pytest.mark.parametrize("password_length", [6, 10, 15])
    def test_successful_registration(self, driver, password_length):
        driver.get("https://stellarburgers.nomoreparties.site")

        main_page = MainPage(driver)
        main_page.click_login_button()

        login_page = LoginPage(driver)
        login_page.click_register_link()

        registration_page = RegistrationPage(driver)
        assert registration_page.is_registration_page()

        name = generate_name()
        email = generate_email()
        password = generate_password(password_length)

        registration_page.register(name, email, password)

        login_page = LoginPage(driver)
        assert login_page.is_login_page()

    def test_registration_with_short_password(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        main_page = MainPage(driver)
        main_page.click_login_button()

        login_page = LoginPage(driver)
        login_page.click_register_link()

        registration_page = RegistrationPage(driver)
        assert registration_page.is_registration_page()

        name = generate_name()
        email = generate_email()
        password = generate_password(5)  # Слишком короткий пароль

        registration_page.register(name, email, password)

        error_text = registration_page.get_password_error()
        assert "Некорректный пароль" in error_text