from .base_page import BasePage
from locators.locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def click_login_button(self):
        self.click_element((By.XPATH, MainPageLocators.LOGIN_BUTTON))

    def click_personal_account_button(self):
        self.click_element((By.XPATH, MainPageLocators.PERSONAL_ACCOUNT_BUTTON))

    def click_constructor_button(self):
        self.click_element((By.XPATH, MainPageLocators.CONSTRUCTOR_BUTTON))

    def click_logo(self):
        self.click_element((By.XPATH, MainPageLocators.LOGO))

    def click_buns_section(self):
        self.click_element((By.XPATH, MainPageLocators.BUNS_SECTION))

    def click_sauces_section(self):
        self.click_element((By.XPATH, MainPageLocators.SAUCES_SECTION))

    def click_fillings_section(self):
        self.click_element((By.XPATH, MainPageLocators.FILLINGS_SECTION))

    def get_active_section_text(self):
        return self.get_text((By.XPATH, MainPageLocators.ACTIVE_SECTION))