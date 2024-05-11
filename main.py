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

# Your Facebook credentials
username = '61559732393722'
password = 'Buyka89024'
61559686854533 Bilguun1213
# Your search query
search_query = 'SUKHBAATAR "Сүхбаатар аймгийн хамгийн том авто зарын групп"'

# Your message
message = 'https://fb.watch/r_RaaBcCgs/'

# Path to the photo you want to upload
# photo_path = 'C:/Users/infnt/OneDrive/Desktop/dd5z073-b6b2b967-d40c-41d2-b195-fbaad0ae0035.png'  # Update this with the path to your photo file

# Start the browser session
driver = webdriver.Firefox()
driver.get(login_url)

# Log in to Facebook
username_input = driver.find_element(By.NAME, 'email')
password_input = driver.find_element(By.NAME, 'pass')
login_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')

username_input.send_keys(username)
password_input.send_keys(password)
login_button.click()

time.sleep(5)  # Wait for the login process to complete

# Handle "Login with one tap" if it appears
try:
    ok_button = driver.find_element(By.CSS_SELECTOR, 'input[value="OK"]')
    ok_button.click()
except:
    pass  # If "Login with one tap" button is not found, continue

# Perform search
# search_input = driver.find_element(By.NAME, 'query')
# search_input.send_keys(search_query)
# search_input.send_keys(Keys.RETURN)

    # group_button = driver.find_element(By.CSS_SELECTOR, 'input[value="OK"]')

# time.sleep(3)  # Wait for the search results to load

# Click on the profile
driver.find_element(By.CSS_SELECTOR, ".bg:nth-child(8) > .bj").click()
driver.find_element(By.LINK_TEXT, "СҮХБААТАР АЙМГИЙН ХАМГИЙН ТОМ ЗАРЫН ГРУПП").click()

time.sleep(3)  # Wait for the profile page to load

# # Click on "View Photo"
# view_photo_button = driver.find_element(By.NAME, 'view_photo')
# view_photo_button.click()
#
# # Upload photo
# upload_file = os.path.abspath(photo_path)
# file_input = driver.find_element(By.NAME, 'file1')
# file_input.send_keys(upload_file)
#
# # Click "Add Photo Done"
# add_photo_done_button = driver.find_element(By.NAME, 'add_photo_done')
# add_photo_done_button.click()
# time.sleep(3)
# Write and post a message
message_input = WebDriverWait(driver, timeout=30).until(
    EC.element_to_be_clickable((By.NAME, 'xc_message'))
)

message_input.send_keys(message)

# Click "View Post"
view_post_button = driver.find_element(By.NAME, 'view_post')
view_post_button.click()
time.sleep(30)
# Close the browser
driver.quit()