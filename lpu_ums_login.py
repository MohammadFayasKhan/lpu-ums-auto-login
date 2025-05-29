"""
LPU UMS Auto Login Script
-------------------------

This script automates login to Lovely Professional University’s UMS portal using:
- Selenium WebDriver
- macOS Keychain for secure credential management

Ensure:
- Google Chrome is installed
- Compatible ChromeDriver is downloaded and executable
- Credentials are saved in macOS Keychain

Author: @Fayas
GitHub: https://github.com/yourusername/lpu-ums-auto-login
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import keyring
from time import sleep
import time

# 🔐 Secure credentials from macOS Keychain
username = keyring.get_password("lpu-ums", "username")
password = keyring.get_password("lpu-ums", "password")
url = "https://ums.lpu.in/lpuums/"

# ChromeDriver setup
chrome_driver_path = "/Users/fayaskhan/Downloads/chromedriver-mac-arm64/chromedriver"
service = Service(chrome_driver_path)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

wait = WebDriverWait(driver, 10)

# Enter username
wait.until(EC.presence_of_element_located((By.ID, "txtU"))).send_keys(username)

# Enter password with retry
for attempt in range(3):
    try:
        password_field = wait.until(EC.presence_of_element_located((By.ID, "TxtpwdAutoId_8767")))
        password_field.clear()
        password_field.send_keys(password)
        break
    except StaleElementReferenceException:
        print(f"Retrying password input (attempt {attempt + 1})")
        sleep(0.5)

# Click login
wait.until(EC.element_to_be_clickable((By.ID, "iBtnLogins150203125"))).click()

# Wait briefly for redirection
sleep(2)

# Handle new tab/window (if opened)
original_window = driver.current_window_handle
for window in driver.window_handles:
    if window != original_window:
        driver.switch_to.window(window)
        break

# Try detecting dashboard
try:
    wait.until(EC.presence_of_element_located((By.ID, "navbarsExample05")))
    print("✅ Logged in and dashboard detected.")
except:
    print("⚠️ Login done but dashboard may still be loading.")

# Keep browser open (for Automator/macOS)
time.sleep(99999)