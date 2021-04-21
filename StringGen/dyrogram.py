from StringGen.config import ( BOT_TOKEN, APP_ID, API_HASH ) 

from pyrogram import Client
from pyromod import listen

devil = Client(
       "skem", 
    bot_token=BOT_TOKEN,
    api_id=APP_ID,
    api_hash=API_HASH
)

