from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop_page_object():
    driver = webdriver.Firefox()

    try:
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page.add_backpack()
        inventory_page.add_tshirt()
        inventory_page.add_onesie()

        inventory_page.go_to_cart()
        cart_page.checkout()

        checkout_page.fill_form("Стася", "Борисова", "123456")

        total = checkout_page.get_total()
        assert total == "Total: $58.29"

    finally:
        driver.quit()