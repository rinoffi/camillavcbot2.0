from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("my_session", "session")
BOT_TOKEN = getenv("7965807385:AAFZiAyeZ4-tbWcw_bgDGwO-gx2Dr1A4x74")
BOT_NAME = getenv("𐅻⏤͟͟͞͞💗꯭꯭᪳𐙚𝆺꯭𝅥ᴋʜ꯭֟፝᷍ᴏ꯭ʟɪ꯭𔒜꯭ᴛⷡʜ꯭ɪʀ꯭ⷪᴜ꯭ᴅ꯭ⷮɪ𖫲ࠫ𝆹꯭𝅥𝄢")

API_ID = int(getenv("28015531"))
API_HASH = getenv("2ab4ba37fd5d9ebf1353328fc915ad28")

DURATION_LIMIT = int(getenv("60"))

COMMAND_PREFIXES = list(getenv("/start !play").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
