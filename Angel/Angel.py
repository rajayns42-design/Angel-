import os
import asyncio
import importlib
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN

# =========================
# BOT INIT
# =========================

app = Client(
    "MyBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")  # 🔥 AUTO LOAD ALL PLUGINS
)

# =========================
# STARTUP
# =========================

async def main():
    await app.start()
    me = await app.get_me()
    print(f"✅ Bot Started -> @{me.username}")
    await idle()
    await app.stop()

# =========================
# RUN
# =========================

if __name__ == "__main__":
    asyncio.run(main())
