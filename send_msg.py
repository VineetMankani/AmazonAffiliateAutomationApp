from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.webdriver.edge.service import Service # type: ignore
from datetime import datetime
import time
from config import EDGE_DRIVER_PATH, EDGE_USER_DATA_DIR_PATH, EDGE_PROFILE_DIR
from helpers import log

GROUP_NAMES = ["Amazon Affiliate", "Amazon Affiliate 2"]

def send_whatsapp_messages(messages):
    
    options = webdriver.EdgeOptions()
    options.add_argument(f"--user-data-dir={EDGE_USER_DATA_DIR_PATH}")
    options.add_argument(f"--profile-directory={EDGE_PROFILE_DIR}")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--headless")  # Optional: Run in headless mode

    service = Service(EDGE_DRIVER_PATH)
    driver = webdriver.Edge(service=service, options=options)   

    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 30)

    try:
        for group in GROUP_NAMES:
            # Always search for group in the search box first
            message_boxes = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@contenteditable='true' and @role='textbox']")))
            search_box = message_boxes[0]
            search_box.click()
            search_box.clear()  # Clear any previous search
            search_box.send_keys(group)
            time.sleep(2)

            try:
                # Try to find and click the group in search results
                contact = wait.until(EC.presence_of_element_located((By.XPATH, f"//span[@title='{group}']")))
                contact.click()
                time.sleep(2)

                # Now send messages using the chat message box
                for message in messages:
                    message = ''.join(c for c in message if ord(c) <= 0xFFFF)

                    # Get message boxes again - now we should have the chat message box
                    message_boxes = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@contenteditable='true' and @role='textbox']")))
                    chat_box = message_boxes[1]  # Use the second box for sending messages

                    chat_box.click()
                    for line in message.split('\n'):
                        chat_box.send_keys(line)
                        chat_box.send_keys(Keys.SHIFT, Keys.ENTER)
                    chat_box.send_keys(Keys.ENTER)

                    message = message.replace("\n", "\\n")
                    log(f"""Message sent successfuly to '{group}': "{message}" """)
                    time.sleep(2)

            except Exception as e:
                log(f"Error finding or sending to group '{group}': {e}")
                continue

        log("All messages sent on WhatsApp successfuly!")
    except Exception as e:
        log(f"ERROR in sending message on WhatsApp!")
        print(f"Error: {e}")

    driver.quit()

# send_whatsapp_messages(["Hello! IGNORE - This is an automated message test on 'WhatsApp-OldGroup'."])
