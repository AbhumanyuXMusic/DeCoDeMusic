from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Pubglovers_shayri_lovers")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "AlishaSupport")
BOT_USERNAME = getenv("BOT_USERNAME")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/a7adee6cf365d74734c5d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/a7adee6cf365d74734c5d.png")
BOT_IMG = getenv("BOT_IMG", "https://telegra.ph/file/de138de8fd880becb9cf1.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/de138de8fd880becb9cf1.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/a7adee6cf365d74734c5d.png")

admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

OWNER_ID = int(getenv("OWNER_ID"))

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
