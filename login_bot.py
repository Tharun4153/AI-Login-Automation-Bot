from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


def login_test():

    # create screenshots folder
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.maximize_window()

        print("Opening website...")
        driver.get("https://www.saucedemo.com")

        wait = WebDriverWait(driver,10)

        username = wait.until(EC.presence_of_element_located((By.ID,"user-name")))
        password = driver.find_element(By.ID,"password")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")

        driver.find_element(By.ID,"login-button").click()

        time.sleep(3)

        if "inventory" in driver.current_url:
            print("Login Successful")

            driver.save_screenshot("screenshots/login_success.png")

        else:
            print("Login Failed")

            driver.save_screenshot("screenshots/login_failed.png")

    except Exception as e:
        print("Error occurred:",e)

    finally:
        time.sleep(3)
        driver.quit()


login_test()
