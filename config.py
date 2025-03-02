from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials
TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")

# Edge browser configuration
EDGE_DRIVER_PATH = os.getenv("EDGE_DRIVER_PATH", "/usr/local/bin/msedgedriver")
EDGE_USER_DATA_DIR_PATH = os.getenv("EDGE_USER_DATA_DIR_PATH", "/home/runner/.config/microsoft-edge")
EDGE_PROFILE_DIR = os.getenv("EDGE_PROFILE_DIR", "Profile 3")

# Channel IDs # BestDealsInIndia=-1001493857075 # DailyDeals=-1001401654901 # My=-4618136976
CHANNEL_ID = [-1001493857075, -1001401654901, -4618136976]

# Time window for fetching messages (in seconds)
PAST_TIME = 60*60  # Default to 60 minutes

# Filter string for messages
FILTER_STRING = "https://amzn.to/"
