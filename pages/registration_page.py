from .base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_login_link(self):
        pass

    def register(self, name, email, password):
        pass