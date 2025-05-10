# (©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

# Bot Credentials
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7354651354:AAG2fCFJbHd5uxxoJCNCTFh7KPrz_F_Qkvk")
APP_ID = int(os.environ.get("APP_ID", "21489763"))
API_HASH = os.environ.get("API_HASH", "308f5362db7844a59272c33634e9e792")

# MongoDB Settings
DB_URI = os.environ.get(
    "DATABASE_URL",
    "mongodb+srv://fakemailcloud3:aZMCYB9Uh0xE7Gox@cluster0.pf4nmcc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# Telegram Channel and Admins
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002397291572"))
OWNER_ID = int(os.environ.get("OWNER_ID", "5100345229"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", None)
ADMINS = []

try:
    ADMINS = [int(x) for x in os.environ.get("ADMINS", "").split()]
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)  # You can remove or adjust this

# Bot Settings
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
PROTECT_CONTENT = os.environ.get("PROTECT_CONTENT", "False") == "True"
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "False") == "True"

# UI Messages
START_PIC = os.environ.get("START_PIC", "")
START_MSG = os.environ.get(
    "START_MESSAGE",
    "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link."
)
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>"
)
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"

# Auto-delete settings
AUTO_DELETE_TIME = int(os.environ.get("AUTO_DELETE_TIME", "300"))
AUTO_DELETE_MSG = os.environ.get(
    "AUTO_DELETE_MSG",
    "This file will be automatically deleted in {time} seconds. Please ensure you have saved any necessary content before this time."
)
AUTO_DEL_SUCCESS_MSG = os.environ.get(
    "AUTO_DEL_SUCCESS_MSG",
    "Your file has been successfully deleted. Thank you for using our service. ✅"
)

# Logging
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
