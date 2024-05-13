import os
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium_authenticated_proxy import SeleniumAuthenticatedProxy

# Initialize Chrome options



# Path to the GeckoDriver executable
# URL of the Facebook login page
login_url = 'https://mbasic.facebook.com'

# Your Facebook usernames and passwords
usernames = ['61559732393722', '61559686854533']  # Add your usernames here
passwords = ['Buyka89024', 'Bilguun1213']  # Add your passwords here
message = ['https://fb.watch/r__ja5RuUB/', 'https://rb.gy/7bamt1']

# Start

# Loop
for username, password, message in zip(usernames, passwords, message):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--ignore-certificate-errors')
    # Initialize SeleniumAuthenticatedProxy
    proxy_helper = SeleniumAuthenticatedProxy(
        proxy_url="https://brd-customer-hl_c2ad23d5-zone-residential_proxy1:9i9go44ljiyv@brd.superproxy.io:22225")
    # proxy_url = "https://brd-customer-hl_c2ad23d5-zone-residential_proxy1:9i9go44ljiyv@brd.superproxy.io:22225")
    # Enrich Chrome options with proxy authentication
    proxy_helper.enrich_chrome_options(chrome_options)
    # Start WebDriver with enriched options
    driver = webdriver.Chrome(options=chrome_options)

    stealth(driver,
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    # Your automation or scraping code here

    driver.get(login_url)
    # driver.save_screenshot('C:/Users/infnt/OneDrive/Desktop/pyBot/img.png')
    # <button type="submit" name="accept_only_essential" value="1" class="br">Decline optional cookies</button>


    try:
        driver.find_element(By.NAME, 'accept_only_essential').click()
    except:
        pass
    username_input = driver.find_element(By.NAME, 'email')
    password_input = driver.find_element(By.NAME, 'pass')
    login_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()
    #
    time.sleep(10)
    #
    # # Handle "Login with one tap" if it appears
    # try:
    #     ok_button = driver.find_element(By.CSS_SELECTOR, 'input[value="OK"]')
    #     ok_button.click()
    # except:
    #     pass
    #
    # try:
    #     driver.find_element(By.CSS_SELECTOR, ".bg:nth-child(8) > .bj").click()
    # except:
    #     driver.find_element(By.CSS_SELECTOR, ".bf:nth-child(8) >.bi").click()
    #
    # driver.find_element(By.LINK_TEXT, 'Сүхбаатар Аймаг Нэгдсэн Зар | Suhbaatar Zar').click()
    # time.sleep(3)
    # # Write and post a message
    # message_input = WebDriverWait(driver, timeout=30).until(
    #     EC.element_to_be_clickable((By.NAME, 'xc_message'))
    # )
    # message_input.send_keys(message)
    #
    # view_post_button = driver.find_element(By.NAME, 'view_post')
    # view_post_button.click()
    #
    # time.sleep(5)
    #
    # driver.quit()