from affiliate_link import get_affiliate_url
import re
import os
import logging
import subprocess
from datetime import datetime

def update_messages(message):
    """Modify the message (custom transformation logic)."""
    message = ''.join(c for c in message if ord(c) <= 0xFFFF)
    url_matches = re.findall(r"https://amzn\.to/\S+", message)
    if not url_matches:
        return message

    modified_message = message
    has_valid_urls = False

    for product_url in url_matches:
        affiliate_url = get_affiliate_url(product_url)
        if affiliate_url:
            modified_message = modified_message.replace(product_url, affiliate_url)
            has_valid_urls = True
        else:
            message = message.replace("\n", "\\n")
            log(f"""Message skipped: No affiliate URL for "{message}" """)
            return None

    return modified_message if has_valid_urls else None

def close_edge():
    """Close all Edge Windows."""
    ps_output = subprocess.check_output(['ps', '-A']).decode()
    if "microsoft-edge" in ps_output:
        subprocess.run(['killall', 'microsoft-edge'])
        log("Edge Linux processes running, closed now")
    else:
        log("No Edge Linux processes running")


def log(message):
    """Log and Print stuff"""
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(message)
    print(f"{time_now} | {message}")
