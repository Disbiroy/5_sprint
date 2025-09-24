from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_login_page_opened(self):
        self.wait_for_url_to_contain("/login")
        return "/login" in self.get_current_url()

    def click_register_link(self):
        pass

    def click_forgot_password_link(self):
        pass

    def login(self, email, password):
        pass