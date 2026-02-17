from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    PageObject для страницы медленного калькулятора.
    """

    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CLASS_NAME, "screen")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        :param driver: экземпляр WebDriver
        :type driver: WebDriver
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> None:
        """
        Открыть страницу калькулятора.

        :return: None
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, value: str) -> None:
        """
        Установить задержку вычисления.

        :param value: значение задержки в секундах
        :type value: str
        :return: None
        """
        delay = self.driver.find_element(*self.DELAY_INPUT)
        delay.clear()
        delay.send_keys(value)

    def press_button(self, text: str) -> None:
        """
        Нажать кнопку калькулятора.

        :param text: текст кнопки
        :type text: str
        :return: None
        """
        self.driver.find_element(
            By.XPATH, f"//span[text()='{text}']"
        ).click()

    def wait_result(self, expected: str) -> None:
        """
        Дождаться появления результата.

        :param expected: ожидаемый результат
        :type expected: str
        :return: None
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )

    def get_result(self) -> str:
        """
        Получить результат вычисления.

        :return: результат вычисления
        :rtype: str
        """
        return self.driver.find_element(*self.SCREEN).text