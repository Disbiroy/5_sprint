from .base_page import BasePage
from locators.locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def input_email(self, email):
        self.input_text((By.XPATH, LoginPageLocators.EMAIL_INPUT), email)

    def input_password(self, password):
        self.input_text((By.XPATH, LoginPageLocators.PASSWORD_INPUT), password)

    def click_login_button(self):
        self.click_element((By.XPATH, LoginPageLocators.LOGIN_BUTTON))

    def click_register_link(self):
        self.click_element((By.XPATH, LoginPageLocators.REGISTER_LINK))

    def click_forgot_password_link(self):
        self.click_element((By.XPATH, LoginPageLocators.FORGOT_PASSWORD_LINK))

    def is_login_page(self):
        return self.find_element((By.XPATH, LoginPageLocators.LOGIN_TITLE)).is_displayed()

    def login(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.click_login_button()