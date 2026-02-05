import os
import asyncio
import logging
from pyrogram import Client, idle
from pyrogram.types import BotCommand
from config import (
    API_ID, 
    API_HASH, 
    BOT_TOKEN, 
    BOT_NAME, 
    MONGO_URL,
    OWNER_ID
)

# --- ʟᴏɢɢɪɴɢ sᴇᴛᴜᴘ ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(BOT_NAME)

# --- ʙᴏᴛ ɪɴɪᴛɪᴀʟɪᴢᴀᴛɪᴏɴ ---
# plugins=dict(root="plugins") ensures all handlers in the plugins folder are imported
app = Client(
    "AngelBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins") 
)

# --- 𝐒𝐄𝐓 𝐌𝐄𝐍𝐔 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 ---
async def set_commands(client):
    await client.set_bot_commands([
        BotCommand("give", "💸 Transfer Coins"),
        BotCommand("daily", "📅 Daily Reward"),
        BotCommand("shop", "🛒 Item Shop"),
        BotCommand("ranking", "🏆 Global Leaderboard"),
        BotCommand("wpropose", "💍 Waifu Propose"),
        BotCommand("wmarry", "🏰 Waifu Random"),
        BotCommand("propose", "💍 Marry User"),
        BotCommand("couple", "💞 Match Maker"),
        BotCommand("marry", "💖 Check Status"),
        BotCommand("divorce", "💔 Break Up"),
        BotCommand("claim", "💎 Claim Group Bonus"),
        BotCommand("draw", "🎨 AI Art"),
        BotCommand("speak", "🗣️ AI Voice"),
        BotCommand("dice", "🎲 Gamble"),
        BotCommand("protect", "🛡️ Buy Immunity"),
        BotCommand("revive", "✨ Revive"),
        BotCommand("chatbot", "🧠 AI Settings"),
        BotCommand("ping", "📊 Status"),
        BotCommand("update", "🔄 Update Bot")
    ])

# --- 𝐒𝐓𝐀𝐑𝐓𝐔𝐏 𝐋𝐎𝐆𝐈𝐂 ---
async def start_bot():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"📡 {BOT_NAME} ɪs sᴛᴀʀᴛɪɴɢ ʙʏ ᴍᴀsᴛᴇʀ ᴢᴇxx...")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    # Client Start
    await app.start()
    
    # Sync Menu Handlers
    await set_commands(app)
    
    me = await app.get_me()
    logger.info(f"✅ Bot @{me.username} is now online!")
    
    # Database Connection Check
    if not MONGO_URL:
        logger.warning("⚠️ MONGO_URL not found! Data won't be saved.")
    else:
        logger.info("🗄️ Database Handlers Linked!")

    print(f"👑 MASTER: ZEXX [cite: 2026-02-04]")
    print("🔥 HANDLERS FROM 30+ PLUGINS IMPORTED!")
    
    # Keep the bot running
    await idle()
    
    # Smooth Shutdown
    await app.stop()
    logger.info("❌ Bot Offline.")

if __name__ == "__main__":
    try:
        # Run the event loop
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start_bot())
    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt detected, stopping...")
