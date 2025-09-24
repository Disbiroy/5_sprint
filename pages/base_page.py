from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.nomoreparties.site"

    def open(self, path=""):

        url = f"{self.base_url}{path}"
        self.driver.get(url)

    def get_current_url(self):

        return self.driver.current_url

    def wait_for_url_to_be(self, expected_url, timeout=10):

        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))
        return self.get_current_url()

    def wait_for_url_to_contain(self, text, timeout=10):

        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))
        return self.get_current_url()