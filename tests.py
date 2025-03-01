from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from helpers import close_edge
close_edge()
# Update with your actual Edge WebDriver path
EDGE_DRIVER_PATH = "D:/Installers/edgedriver_win64/msedgedriver.exe"

# Update with your actual Edge User Data and Profile paths
EDGE_USER_DATA_DIR_PATH = r"C:\Users\vinee\AppData\Local\Microsoft\Edge\User Data"
EDGE_PROFILE_DIR = "Default"  # Change if using another profile (e.g., "Default", "Profile 2")

# Set Edge options
options = webdriver.EdgeOptions()
options.add_argument(f"--user-data-dir={EDGE_USER_DATA_DIR_PATH}")  # Use existing user data
options.add_argument(f"--profile-directory={EDGE_PROFILE_DIR}")  # Use a specific profile
options.add_argument("--disable-gpu")  # Helps prevent some crashes
options.add_argument("--remote-debugging-port=9222")  # Enables debugging

# Start Edge WebDriver with service
service = Service(EDGE_DRIVER_PATH)
driver = webdriver.Edge(service=service, options=options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")

try:
    wait = WebDriverWait(driver, 30)
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, "canvas")))  # QR code should load
    print("WhatsApp Web Loaded with Profile!")
except Exception as e:
    print(f"Error: {e}")

time.sleep(10)  # Keep browser open for testing
driver.quit()


import os
tasklist = os.popen("tasklist").read()
print(tasklist)
