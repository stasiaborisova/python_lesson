from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPage:
    """
    PageObject для страницы авторизации.
    """

    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы логина.

        :param driver: экземпляр WebDriver
        :type driver: WebDriver
        :return: None
        """
        self.driver = driver

    def open(self) -> None:
        """
        Открыть страницу авторизации.

        :return: None
        """
        self.driver.get(self.URL)

    def login(self, username: str, password: str) -> None:
        """
        Выполнить вход в систему.

        :param username: имя пользователя
        :type username: str
        :param password: пароль пользователя
        :type password: str
        :return: None
        """
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()