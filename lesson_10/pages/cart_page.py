from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    PageObject для страницы корзины.
    """

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """
        Инициализация страницы корзины.

        :param driver: экземпляр WebDriver
        :param timeout: максимальное время ожидания элементов (сек)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def checkout(self) -> None:
        """
        Нажать кнопку оформления заказа после того,
        как она станет доступна.
        """
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_btn.click()
