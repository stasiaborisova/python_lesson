from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class InventoryPage:
    """
    PageObject для страницы товаров (Inventory).
    """

    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TSHIRT_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы товаров.

        :param driver: экземпляр WebDriver
        :type driver: WebDriver
        :return: None
        """
        self.driver = driver

    def add_backpack(self) -> None:
        """
        Добавить товар 'Sauce Labs Backpack' в корзину.

        :return: None
        """
        self.driver.find_element(*self.ADD_BACKPACK_BUTTON).click()

    def add_tshirt(self) -> None:
        """
        Добавить товар 'Sauce Labs Bolt T-Shirt' в корзину.

        :return: None
        """
        self.driver.find_element(*self.ADD_TSHIRT_BUTTON).click()

    def add_onesie(self) -> None:
        """
        Добавить товар 'Sauce Labs Onesie' в корзину.

        :return: None
        """
        self.driver.find_element(*self.ADD_ONESIE_BUTTON).click()

    def go_to_cart(self) -> None:
        """
        Перейти в корзину.

        :return: None
        """
        self.driver.find_element(*self.CART_BUTTON).click()
