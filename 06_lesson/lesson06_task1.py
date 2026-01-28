from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")

    button = driver.find_element(By.ID, "ajaxButton")
    button.click()

    wait = WebDriverWait(driver, 10)
    green_box = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )

    print(green_box.text)

finally:
    driver.quit()