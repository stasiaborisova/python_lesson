from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    wait = WebDriverWait(driver, 15)

    wait.until(lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3)

    third_image = wait.until(
        lambda d: d.find_elements(By.TAG_NAME, "img")[2]
        if d.find_elements(By.TAG_NAME, "img")[2].get_attribute("src")
        else False
    )

    src_value = third_image.get_attribute("src")
    print(src_value)

finally:
    driver.quit()