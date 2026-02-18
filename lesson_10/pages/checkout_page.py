from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    PageObject для страницы оформления заказа.
    """

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """
        Инициализация страницы оформления заказа.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def fill_form(self, first_name: str,
                last_name: str, zip_code: str) -> None:
        """
        Заполнить форму оформления заказа.
        """
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT)).send_keys(first_name)

        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.ZIP_CODE_INPUT).send_keys(zip_code)

        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    def get_total(self) -> str:
        """
        Получить итоговую сумму заказа.
        """
        total = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        )
        return total.text
