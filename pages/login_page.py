from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_login_page_opened(self):  # Переименован для единообразия

        self.wait_for_url_to_contain("/login")
        return "/login" in self.get_current_url()