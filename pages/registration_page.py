from .base_page import BasePage
from locators.locators import RegistrationPageLocators
from selenium.webdriver.common.by import By


class RegistrationPage(BasePage):
    def input_name(self, name):
        self.input_text((By.XPATH, RegistrationPageLocators.NAME_INPUT), name)

    def input_email(self, email):
        self.input_text((By.XPATH, RegistrationPageLocators.EMAIL_INPUT), email)

    def input_password(self, password):
        self.input_text((By.XPATH, RegistrationPageLocators.PASSWORD_INPUT), password)

    def click_register_button(self):
        self.click_element((By.XPATH, RegistrationPageLocators.REGISTER_BUTTON))

    def click_login_link(self):
        self.click_element((By.XPATH, RegistrationPageLocators.LOGIN_LINK))

    def get_password_error(self):
        return self.get_text((By.XPATH, RegistrationPageLocators.PASSWORD_ERROR))

    def is_registration_page(self):
        return self.find_element((By.XPATH, RegistrationPageLocators.REGISTRATION_TITLE)).is_displayed()

    def register(self, name, email, password):
        self.input_name(name)
        self.input_email(email)
        self.input_password(password)
        self.click_register_button()