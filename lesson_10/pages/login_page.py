from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    PageObject для страницы авторизации.
    """

    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """
        Инициализация страницы логина.

        :param driver: экземпляр WebDriver
        :param timeout: максимальное время ожидания элементов (сек)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self) -> None:
        """Открыть страницу авторизации."""
        self.driver.get(self.URL)

    def login(self, username: str, password: str) -> None:
        """
        Выполнить вход в систему с ожиданием доступности полей.
        """

        self.wait.until(EC.visibility_of_element_located
                        (self.USERNAME_INPUT)).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
