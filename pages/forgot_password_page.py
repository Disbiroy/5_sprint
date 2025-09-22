from .base_page import BasePage
from locators.locators import ForgotPasswordPageLocators
from selenium.webdriver.common.by import By


class ForgotPasswordPage(BasePage):
    def click_login_link(self):
        self.click_element((By.XPATH, ForgotPasswordPageLocators.LOGIN_LINK))

    def is_forgot_password_page(self):
        return self.find_element((By.XPATH, ForgotPasswordPageLocators.FORGOT_PASSWORD_TITLE)).is_displayed()