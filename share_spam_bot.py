import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to the GeckoDriver executable
driver_path = 'C:/Users/infnt/OneDrive/Desktop/pyBot/spamBot/geckodriver.exe'

# URL of the Facebook login page
login_url = 'https://mbasic.facebook.com'

# Your Facebook usernames and passwords
usernames = ['61559732393722', '61559686854533']  # Add your usernames here
passwords = ['Buyka89024', 'Bilguun1213']  # Add your passwords here
message = ['https://fb.watch/r__ja5RuUB/', 'https://rb.gy/7bamt1']

# Start


# Loop
for username, password in zip(usernames, passwords):
    driver = webdriver.Firefox()
    driver.get(login_url)
    # Log in to Facebook
    username_input = driver.find_element(By.NAME, 'email')
    password_input = driver.find_element(By.NAME, 'pass')
    login_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()

    time.sleep(3)

    # Handle "Login with one tap" if it appears
    try:
        ok_button = driver.find_element(By.CSS_SELECTOR, 'input[value="OK"]')
        ok_button.click()
    except:
        pass

    try:
        driver.find_element(By.CSS_SELECTOR, ".bg:nth-child(8) > .bj").click()
    except:
        driver.find_element(By.CSS_SELECTOR, ".bf:nth-child(8) >.bi").click()

    driver.find_element(By.LINK_TEXT, 'Мөнххаан зар').click()
    time.sleep(3)
    # Write and post a message
    message_input = WebDriverWait(driver, timeout=30).until(
        EC.element_to_be_clickable((By.NAME, 'xc_message'))
    )
    message_input.send_keys(message)

    view_post_button = driver.find_element(By.NAME, 'view_post')
    view_post_button.click()

    time.sleep(5)

    driver.quit()
