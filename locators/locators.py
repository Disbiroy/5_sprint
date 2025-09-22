class MainPageLocators:
    PAGE_TITLE = ".//h1[contains(text(),'Соберите бургер')]"

    LOGIN_BUTTON = ".//button[contains(text(),'Войти в аккаунт')]"
    PERSONAL_ACCOUNT_BUTTON = ".//p[contains(text(),'Личный Кабинет')]"
    CONSTRUCTOR_BUTTON = ".//p[contains(text(),'Конструктор')]"

    BUNS_SECTION = ".//span[contains(text(),'Булки')]/.."
    SAUCES_SECTION = ".//span[contains(text(),'Соусы')]/.."
    FILLINGS_SECTION = ".//span[contains(text(),'Начинки')]/.."

    ACTIVE_SECTION = ".//div[contains(@class, 'tab_tab_type_current')]"

    LOGO = ".//div[contains(@class, 'AppHeader_header__logo')]"

class LoginPageLocators:

    LOGIN_TITLE = ".//h2[contains(text(),'Вход')]"

    EMAIL_INPUT = ".//input[@name='name']"
    PASSWORD_INPUT = ".//input[@name='Пароль']"

    LOGIN_BUTTON = ".//button[contains(text(),'Войти')]"
    REGISTER_LINK = ".//a[contains(text(),'Зарегистрироваться')]"
    FORGOT_PASSWORD_LINK = ".//a[contains(text(),'Восстановить пароль')]"


class RegistrationPageLocators:

    REGISTRATION_TITLE = ".//h2[contains(text(),'Регистрация')]"

    NAME_INPUT = ".//label[contains(text(),'Имя')]/following-sibling::input"
    EMAIL_INPUT = ".//label[contains(text(),'Email')]/following-sibling::input"
    PASSWORD_INPUT = ".//label[contains(text(),'Пароль')]/following-sibling::input"

    REGISTER_BUTTON = ".//button[contains(text(),'Зарегистрироваться')]"
    LOGIN_LINK = ".//a[contains(text(),'Войти')]"

    PASSWORD_ERROR = ".//p[contains(@class,'input__error')]"

class ProfilePageLocators:

    PROFILE_TITLE = ".//a[contains(text(),'Профиль')]"

    LOGOUT_BUTTON = ".//button[contains(text(),'Выход')]"
    CONSTRUCTOR_LINK = ".//p[contains(text(),'Конструктор')]"

    PROFILE_NAME_INPUT = ".//input[@name='name']"
    PROFILE_EMAIL_INPUT = ".//input[@name='email']"

class ForgotPasswordPageLocators:
    FORGOT_PASSWORD_TITLE = ".//h2[contains(text(),'Восстановление пароля')]"
    LOGIN_LINK = ".//a[contains(text(),'Войти')]"