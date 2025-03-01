from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

# Edge browser configuration
EDGE_DRIVER_PATH = os.getenv("EDGE_DRIVER_PATH")
EDGE_USER_DATA_DIR_PATH = os.getenv("EDGE_USER_DATA_DIR_PATH")
EDGE_PROFILE_DIR = os.getenv("EDGE_PROFILE_DIR")

# Channel IDs # BestDealsInIndia=-1001493857075 # DailyDeals=-1001401654901 # My=-4618136976
CHANNEL_ID = [-1001493857075, -1001401654901, -4618136976]

# Time window for fetching messages (in seconds)
PAST_TIME = 60*15  # Default to 15 minutes

# Filter string for messages
FILTER_STRING = "https://amzn.to/"