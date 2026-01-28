from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, value: str):
        delay = self.driver.find_element(*self.DELAY_INPUT)
        delay.clear()
        delay.send_keys(value)

    def press_button(self, text: str):
        self.driver.find_element(
            By.XPATH, f"//span[text()='{text}']"
        ).click()

    def wait_result(self, expected: str):
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )

    def get_result(self) -> str:
        return self.driver.find_element(*self.SCREEN).text