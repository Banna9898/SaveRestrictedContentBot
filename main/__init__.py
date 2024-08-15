#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 29141829
API_HASH = "25020d00fbcfd406fc9979d24d761bff"
BOT_TOKEN = "7533852833:AAFbM51a-wGYT79C-HX8Cb1frUpyJBZ4O5E"
SESSION = "BQG8q0UAIKlcbtscn7AJSKedbTmLkgAGX5LiZgmsv9nQ9PROYFK6Cin920i8i0cct1zaMp1nbawNQ4-Q67MBMUqC1aZgVQBw4O-hRolSjb5Psfrs4WK7CN3kmb6hZG65CL7Wa-6vmDORq4mTWDiMzcNF6kXDJ1Z-9x9rrOKzRswL4y9WpsDxKGgPE1CzsWi615a0gQRBnwM2Ojtb_qQO5KcbZE8Jt-wO9L9CYmQ7Ck7WyQojn6yN9REAAOADm_rm1Y3jsaTnLUu13nojOZSSIk_vnuKLTvpIzdcN7AXzJxFcB6NaHcLGTAxX-zyLjf3nr8Sn-SHFwtc4ZScRO54AT1cnADUQAAAAE9TLQaAA"
FORCESUB = "jayhind_675"
AUTH = 5323404314

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
