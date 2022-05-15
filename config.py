from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN","1917637742:AAF61TOx72pQEap0aHp56t9yQL5VUl-C7R0")
BOT_NAME = getenv("BOT_NAME","ᴍᴀʀʀᴋ ᴍᴜꜱɪᴄ")
BOT_USERNAME = getenv("BOT_USERNAME", "marrk_music_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "marrk85")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "marrkmusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/ea27626bc869d4dc452d8.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/31aada03a55ab31c447fc.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2030475041").split()))
