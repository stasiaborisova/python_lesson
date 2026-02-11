from selenium import webdriver
from pages.calculator_page import CalculatorPage


def test_slow_calculator_page_object():
    driver = webdriver.Chrome()

    try:
        calculator = CalculatorPage(driver)

        calculator.open()
        calculator.set_delay("45")

        calculator.press_button("7")
        calculator.press_button("+")
        calculator.press_button("8")
        calculator.press_button("=")

        calculator.wait_result("15")
        result = calculator.get_result()

        assert result == "15"

    finally:
        driver.quit()