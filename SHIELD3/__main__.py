import asyncio
import importlib
from pyrogram import idle
from SHIELD3 import SHIELD3
from SHIELD3.modules import ALL_MODULES

LOGGER_ID = -1001961907996

loop = asyncio.get_event_loop()

async def roy_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("SHIELD3.modules." + all_module)
    print("♥︎ B𝗈𝗍 Started Successfully.")
    await idle()
    print("♥︎ Don't edit baby, otherwise you get an error. @Boy_Girl_Dp")
    await SHIELD3.send_message(LOGGER_ID, "**✦ ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ.\n\n✦ ᴊᴏɪɴ - @Freinds_club**")

if __name__ == "__main__":
    loop.run_until_complete(roy_bot())




