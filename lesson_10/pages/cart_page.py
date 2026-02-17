from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class CartPage:
    """
    PageObject для страницы корзины.
    """

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.

        :param driver: экземпляр WebDriver
        :type driver: WebDriver
        :return: None
        """
        self.driver = driver

    def checkout(self) -> None:
        """
        Нажать кнопку оформления заказа (Checkout).

        :return: None
        """
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()