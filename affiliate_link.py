from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import random
from config import EDGE_DRIVER_PATH, EDGE_USER_DATA_DIR_PATH, EDGE_PROFILE_DIR

def get_affiliate_url(product_url):
    # Create a unique temporary directory for this run
    unique_suffix = f"_{random.randint(1000, 9999)}"
    unique_user_data_dir = f"{EDGE_USER_DATA_DIR_PATH}{unique_suffix}"
    
    # Copy profile from the original location to the unique directory
    profile_source = os.path.join(EDGE_USER_DATA_DIR_PATH, EDGE_PROFILE_DIR)
    profile_dest = os.path.join(unique_user_data_dir, EDGE_PROFILE_DIR)
    
    # Create the destination directory
    os.makedirs(profile_dest, exist_ok=True)
    
    # Copy all files from source to destination (simple implementation)
    os.system(f"cp -r {profile_source}/* {profile_dest}/")
    
    # Setup WebDriver options
    options = webdriver.EdgeOptions()
    options.add_argument(f"--user-data-dir={unique_user_data_dir}")
    options.add_argument(f"--profile-directory={EDGE_PROFILE_DIR}")
    
    # Add headless mode options for GitHub Actions
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    
    service = Service(EDGE_DRIVER_PATH)
    driver = webdriver.Edge(service=service, options=options)
    
    try:
        print(f"Opening URL: {product_url}")
        driver.get(product_url)
        time.sleep(5)  # Allow page to load
        
        # Take screenshot for debugging
        driver.save_screenshot("amazon_page.png")
        
        # Print debug information
        print("Current URL:", driver.current_url)
        print("Page Title:", driver.title)
        
        # Check if logged in
        if "Hello, " in driver.page_source or "Your Account" in driver.page_source:
            print("Amazon is logged in!")
        else:
            print("Amazon is NOT logged in.")
            # Return early if not logged in
            return None
        
        try:
            # Use explicit wait for the affiliate button
            wait = WebDriverWait(driver, 10)
            button = wait.until(EC.element_to_be_clickable((By.ID, "amzn-ss-get-link-button")))
            button.click()
            
            # Wait for the affiliate link to be generated
            element = wait.until(EC.presence_of_element_located((By.ID, "amzn-ss-text-shortlink-textarea")))
            affiliate_url = element.get_attribute("value") or element.text
            
            if not affiliate_url or affiliate_url.strip() == "":
                print("Affiliate URL is empty")
                return None
                
            print(f"Successfully generated affiliate URL: {affiliate_url[:30]}...")
            return affiliate_url
            
        except Exception as e:
            print(f"Error finding or clicking affiliate elements: {e}")
            return None
            
    except Exception as e:
        print(f"Error getting affiliate URL for {product_url}: {e}")
        return None
    finally:
        # Clean up
        driver.quit()
        try:
            # Remove the temporary profile directory
            os.system(f"rm -rf {unique_user_data_dir}")
            print(f"Cleaned up temporary directory: {unique_user_data_dir}")
        except Exception as cleanup_error:
            print(f"Error during cleanup: {cleanup_error}")
