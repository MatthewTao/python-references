from selenium import webdriver
from selenium.webdriver.common.by import By

import time


if __name__ == "__main__":
    driver = webdriver.Firefox()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # Wait up to 0.5 seconds for elements to become available
    # Look into explicit waits for more control
    driver.implicitly_wait(0.5)

    title = driver.title
    print(title)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    text = message.text
    print(text)

    # Just to be able to see the output before the browser closes
    time.sleep(2)

    driver.quit()
