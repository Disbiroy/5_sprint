from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        super().open("/")

    def is_main_page_opened(self):
        self.wait_for_url_to_be("https://stellarburgers.nomoreparties.site/")
        return self.get_current_url() == "https://stellarburgers.nomoreparties.site/"

    def click_login_button(self):
        pass

    def click_personal_account_button(self):
        pass