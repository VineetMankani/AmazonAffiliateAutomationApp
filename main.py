from config import TELEGRAM_API_ID, TELEGRAM_API_HASH, CHANNEL_ID, PAST_TIME, FILTER_STRING
from telegram_app import initialize_telegram_client, read_and_update_telegram_messages
from helpers import update_messages, close_edge, log
from send_msg import send_whatsapp_messages
import logging
from datetime import datetime

time_start = datetime.now()
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s | %(message)s')
log("Starting the script...")
close_edge()

client = initialize_telegram_client(TELEGRAM_API_ID, TELEGRAM_API_HASH)
log("Initialized Telegram client")

if __name__ == "__main__":

    # READ TELEGRAM MESSAGES
    messages = read_and_update_telegram_messages(client, CHANNEL_ID, PAST_TIME, FILTER_STRING, update_messages)
    log(f"Read and Updated {len(messages)} Telegram messages: {messages}")

    # SEND MESSAGE ON WHATSAPP
    send_whatsapp_messages(messages) if messages else log("No messages to send")
    close_edge()

log("Script Terminated!")
time_end = datetime.now()
log(f"Time taken: {time_end - time_start}\n")
