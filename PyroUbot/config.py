import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7524271223").split()))

API_ID = int(os.getenv("API_ID", "29839059"))

API_HASH = os.getenv("API_HASH", "31611402902e312a81eec0587fd99206")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8165760784:AAFeeuavOwnXjmCf5UyyRqgKyi-_BC2dJIQ")

OWNER_ID = int(os.getenv("OWNER_ID", "7524271223"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002312835928").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://aortulsk:KxCX5EQdssavL4dm@cluster0.qsywpr2.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4753971361"))
