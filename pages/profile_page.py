from .base_page import BasePage
from locators.locators import ProfilePageLocators
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):
    def click_logout_button(self):
        self.click_element((By.XPATH, ProfilePageLocators.LOGOUT_BUTTON))

    def click_constructor_link(self):
        self.click_element((By.XPATH, ProfilePageLocators.CONSTRUCTOR_LINK))

    def is_profile_page(self):
        return self.find_element((By.XPATH, ProfilePageLocators.PROFILE_TITLE)).is_displayed()

    def get_profile_name(self):
        return self.find_element((By.XPATH, ProfilePageLocators.PROFILE_NAME_INPUT)).get_attribute("value")