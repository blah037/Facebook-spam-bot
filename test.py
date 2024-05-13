import os
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL of the Facebook login page
login_url = 'https://mbasic.facebook.com/login/save-password-interstitial/?ref_component=mbasic_footer&ref_page=%2Fwap%2Fhome.php&refid=7&ref=104&paipv=0&eav=AfYLVwsn78pLbkLoDFoD6JOcVBFsO4guJqYzrz-QcGrdHgzE3fWNSmggYFfZPlmao8A'

# Your Facebook usernames and passwords
usernames = ['61559732393722', '61559686854533']  # Add your usernames here
passwords = ['Buyka89024', 'Bilguun1213']  # Add your passwords here
messages = ['https://fb.watch/r__ja5RuUB/', 'https://rb.gy/7bamt1']

# List of group URLs
group_urls = [
    'https://mbasic.facebook.com/groups/1457232711308180/?refid=27&ref=104&paipv=0&eav=AfY2gvHLCvVPUTTq6ocMz4-Qi-j8lKwYdro41J5mqeiiZDej-3-2rnUuH8Y8kVzchpM',
    'https://mbasic.facebook.com/groups/sukhbaatar.aimgiin.zar/?refid=27&ref=104&paipv=0&eav=Afa5sKt1VxSDjfwntdy4eUVOx03paASJ8HxLNwqRDnguItkECzy__4jqEh8xdnIpJuk',
    'https://mbasic.facebook.com/groups/1080727898755526/?refid=27&ref=104&paipv=0&eav=AfbY-q5cWKCY98TFbv5wT-QXG2RtW3u8_2WljiqaWnFvXMgBq4MPhwnqhdbU7ofn7ME'
]

# File to store the index of the current group URL
index_file_path = 'group_url_index.txt'

# Read the index from the file or initialize it to 0 if the file doesn't exist
if os.path.exists(index_file_path):
    with open(index_file_path, 'r') as f:
        index = int(f.read())
else:
    index = 0

# Get the current group URL based on the index
current_group_url = group_urls[index]

# Increment the index and wrap around if it exceeds the length of group_urls
index = (index + 1) % len(group_urls)

# Write the updated index back to the file
with open(index_file_path, 'w') as f:
    f.write(str(index))

# Start

# Loop
for username, password, message in zip(usernames, passwords, messages):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    stealth(driver,
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    driver.get(login_url)
    # driver.save_screenshot('C:/Users/infnt/OneDrive/Desktop/pyBot/spamBot')
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

    driver.get(current_group_url)
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
