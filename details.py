from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("22779671", 0))
API_HASH = getenv("125d8d88b77309dc3b154cbbfc2dacb2", None)
BOT_TOKEN = getenv("6152562853:AAGimPmtvHjqcE8em9iDMH-QAjkM8133P0c", None)
OWNER_ID = int(getenv("OWNER_ID", 1713924419))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1713924419").split()))
