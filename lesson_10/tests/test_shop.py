import allure
from selenium import webdriver

from lesson_10.pages.login_page import LoginPage
from lesson_10.pages.inventory_page import InventoryPage
from lesson_10.pages.cart_page import CartPage
from lesson_10.pages.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Полный цикл покупки товара")
@allure.description(
    "Тест проверяет полный процесс покупки: логин, "
    "добавление товаров в корзину, "
    "оформление заказа и проверку итоговой суммы."
)
def test_shop_page_object():
    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step("Открыть страницу логина"):
            login_page.open()

        with allure.step("Авторизоваться под стандартным пользователем"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавить товары в корзину"):
            inventory_page.add_backpack()
            inventory_page.add_tshirt()
            inventory_page.add_onesie()

        with allure.step("Перейти в корзину"):
            inventory_page.go_to_cart()

        with allure.step("Перейти к оформлению заказа"):
            cart_page.checkout()

        with allure.step("Заполнить форму оформления заказа"):
            checkout_page.fill_form("Стася", "Борисова", "123456")

        with allure.step("Проверить итоговую сумму"):
            total = checkout_page.get_total()
            assert total == "Total: $58.29"

    finally:
        driver.quit()
