import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")

    # Самый простой способ
    driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()))

    driver.maximize_window()
    yield driver
    driver.quit()