import allure
from selenium import webdriver
from lesson_10.pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка сложения 7 + 8")
@allure.description(
    "Тест проверяет корректность сложения 7 и 8 "
    "на странице медленного калькулятора."
)
def test_slow_calculator_page_object():

    driver = webdriver.Chrome()

    try:
        calculator = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            calculator.open()

        with allure.step("Установить задержку 45 секунд"):
            calculator.set_delay("45")

        with allure.step("Нажать 7 + 8 ="):
            calculator.press_button("7")
            calculator.press_button("+")
            calculator.press_button("8")
            calculator.press_button("=")

        with allure.step("Дождаться результата 15"):
            calculator.wait_result("15")

        with allure.step("Проверить результат"):
            result = calculator.get_result()
            assert result == "15"

    finally:
        driver.quit()
