from datetime import datetime, timedelta, timezone
from telethon import TelegramClient
from helpers import log


def initialize_telegram_client(API_ID, API_HASH):
    """Initialize and return the Telegram client."""
    client = TelegramClient("session_name", API_ID, API_HASH)
    client.start()
    return client


def read_and_update_telegram_messages(client, channel_ids, time_window, filter_string, update_messages):
    """Fetch messages from multiple Telegram channels, filter them by a keyword, and transform them."""
    cutoff_time = datetime.now(timezone.utc) - timedelta(seconds=time_window)
    updated_messages = []

    for channel_id in channel_ids:
        for message in client.iter_messages(channel_id):
            if message.date and message.date.replace(tzinfo=timezone.utc) > cutoff_time:
                if filter_string in message.text:  # Apply filtering
                    updated_messages.append(update_messages(message.text))  # Apply transformation
            else:
                break  # Stop fetching if messages are older than the cutoff time

    updated_messages = [msg for msg in updated_messages if msg]
    return updated_messages