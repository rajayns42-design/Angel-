import random
from pyrogram import Client, filters
from datetime import datetime

# --- DATABASE (Temporary) ---
user_data = {} # Coins aur Last Date ke liye
line = "✨ ɢᴏʟᴅᴇɴ ʀᴇᴡᴀʀᴅ ✨"
separator = "═" * 20

@Client.on_message(filters.command("daily"))
async def daily_handler(client, message):
    user_id = message.from_user.id
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Check agar user ne aaj claim kiya hai
    if user_id in user_data and user_data[user_id].get("last_claim") == today:
        return await message.reply_text(
            f"<b>🛑 ᴀʟʀᴇᴀᴅʏ ᴄʟᴀɪᴍᴇᴅ!</b>\n"
            f"<i>{separator}</i>\n"
            f"ᴀᴀᴘɴᴇ ᴀᴀᴊ ᴋᴀ ᴛᴏᴋᴇɴ ʟᴇ ʟɪʏᴀ ʜᴀɪ.\n"
            f"ᴀʙ ᴋᴀʟ ᴡᴀᴘᴀs ᴀᴀɪʏᴇ ɴᴀʏᴇ ɢɪғᴛs ᴋᴇ ʟɪʏᴇ! ⏳"
        )

    # Coins Logic
    bonus = random.randint(2000, 8000)
    
    # Data Update
    if user_id not in user_data:
        user_data[user_id] = {"coins": 0, "streak": 0}
    
    user_data[user_id]["coins"] += bonus
    user_data[user_id]["last_claim"] = today
    user_data[user_id]["streak"] += 1
    
    # Response UI
    await message.reply_text(
        f"<b>{line}</b>\n"
        f"<i>{separator}</i>\n"
        f"<b>👤 ᴘʟᴀʏᴇʀ:</b> <code>{message.from_user.first_name}</code>\n"
        f"<b>💰 ʀᴇᴡᴀʀᴅ:</b> <code>{bonus} ᴄᴏɪɴs</code>\n"
        f"<b>🔥 sᴛʀᴇᴀᴋ:</b> <code>{user_data[user_id]['streak']} ᴅᴀʏs</code>\n"
        f"<b>🏦 ʙᴀʟᴀɴᴄᴇ:</b> <code>{user_data[user_id]['coins']}</code>\n"
        f"<i>{separator}</i>\n"
        f"🎉 ᴀᴀᴘᴋᴀ ᴅᴀɪʟʏ ʙᴏɴᴜs sᴜᴄᴄᴇssғᴜʟʟʏ ᴀᴅᴅ ʜᴏ ɢᴀʏᴀ!"
    )
