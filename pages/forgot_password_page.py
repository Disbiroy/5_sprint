from .base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_forgot_password_page_opened(self):
        self.wait_for_url_to_contain("/forgot-password")
        return "/forgot-password" in self.get_current_url()

    def click_login_link(self):
        pass