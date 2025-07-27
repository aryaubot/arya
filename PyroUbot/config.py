import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "5654480935").split()))

API_ID = int(os.getenv("API_ID", "20227346"))

API_HASH = os.getenv("API_HASH", "0600f98a6c4721aeed6677480298ad88")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8165760784:AAFUXud7lQsmfLfqMt_SFgD3Zgw2SJx9bqY")

OWNER_ID = int(os.getenv("OWNER_ID", "5654480935"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002312835928").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://aortulsk:KxCX5EQdssavL4dm@cluster0.qsywpr2.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4912035642"))
