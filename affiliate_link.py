from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service # type: ignore
import time
from config import EDGE_DRIVER_PATH, EDGE_USER_DATA_DIR_PATH, EDGE_PROFILE_DIR

def get_affiliate_url(product_url):

    options = webdriver.EdgeOptions()
    options.add_argument(f"--user-data-dir={EDGE_USER_DATA_DIR_PATH}")
    options.add_argument(f"--profile-directory={EDGE_PROFILE_DIR}")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--headless")  # Optional: Run in headless mode

    service = Service(EDGE_DRIVER_PATH)
    driver = webdriver.Edge(service=service, options=options)   

    try:
        driver.get(product_url)

        button = driver.find_element(By.ID, "amzn-ss-get-link-button")
        button.click()

        time.sleep(3)

        element = driver.find_element(By.ID, "amzn-ss-text-shortlink-textarea")
        affiliate_url = element.text
        
        if not affiliate_url or affiliate_url.strip() == "":
            return None
            
        return affiliate_url
        
    except Exception as e:
        print(f"Error getting affiliate URL for {product_url}: {e}")
        return None
    finally:
        driver.quit()
