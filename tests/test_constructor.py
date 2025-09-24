import pytest
from pages.main_page import MainPage


class TestConstructor:
    def test_constructor_buns_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        main_page = MainPage(driver)
        main_page.click_sauces_section()
        main_page.click_buns_section()

        active_section = main_page.get_active_section_text()
        assert "Булки" in active_section

    def test_constructor_sauces_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        main_page = MainPage(driver)
        main_page.click_sauces_section()

        active_section = main_page.get_active_section_text()
        assert "Соусы" in active_section

    def test_constructor_fillings_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site")

        main_page = MainPage(driver)
        main_page.click_fillings_section()

        active_section = main_page.get_active_section_text()
        assert "Начинки" in active_section