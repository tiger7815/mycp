from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("22609670", 0))
API_HASH = getenv("3506d8474ad1f4f5e79b7c52a5c3e88d", None)
BOT_TOKEN = getenv("6739442523:AAHHA5HZmU6sqI-elmhTs8dwHqfhTizWwnQ", None)
OWNER_ID = int(getenv("OWNER_ID", 5987970971))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5987970971").split()))
