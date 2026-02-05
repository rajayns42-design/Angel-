import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import BOT_OWNER

@Client.on_message(filters.command("ping"))
async def ping_handler(client: Client, message: Message):
    # ⚡ Start Time Check
    start_time = time.time()
    
    # Stylish Processing Message
    p_msg = await message.reply_text("⚡ **𝐀𝐍𝐆𝐄𝐋 𝐈𝐒 𝐂𝐀𝐋𝐂𝐔𝐋𝐀𝐓𝐈𝐍𝐆...**")
    
    # ⏱️ End Time & Calculation
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 2)
    
    # 🩸 Blood Style Ping Text
    TEXT = (
        f"🩸 **𝐀𝐍𝐆𝐄𝐋 x𝐁~ 𝐒𝐏𝐄𝐄𝐃 𝐒𝐓𝐀𝐓𝐒** 🩸\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🚀 **𝐏𝐈𝐍𝐆 :** `{ping_time} ᴍs`\n"
        f"📡 **𝐒𝐓𝐀𝐓𝐔𝐒 :** ᴜɴᴅᴇʀᴡᴏʀʟᴅ ᴏɴʟɪɴᴇ\n"
        f"💻 **𝐒𝐄𝐑𝐕𝐄𝐑 :** ʜᴇʀᴏᴋᴜ ᴄᴏɴᴛᴀɪɴᴇʀ\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"**𝐌𝐀𝐒𝐓𝐄𝐑 : {BOT_OWNER} ✦** [cite: 2026-02-04]"
    )
    
    await p_msg.edit_text(TEXT)
