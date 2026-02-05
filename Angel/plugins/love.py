import random
from pyrogram import Client, filters
from Angel.plugins.mood import BREAKUP_MODE # Mood check karne ke liye

line = "━━━━━━━━━━━━━━━━━━━━"

@Client.on_message(filters.command(["love", "match"]) & filters.group)
async def love_match(client, message):
    chat_id = message.chat.id
    
    # Check if Breakup Mode is ON
    if BREAKUP_MODE.get(chat_id):
        return await message.reply_text(
            "<b>💔 ʙʀᴇᴀᴋᴜᴘ ᴍᴏᴅᴇ ɪs ᴏɴ!</b>\n"
            "ZEXX ne pyaar par ban lagaya hai. Abhi sirf dushmani chalegi! 🔫"
        )

    if not message.reply_to_message:
        return await message.reply_text("<b>❌ Arre Majnu! Kiske saath match karna hai? Reply karo!</b>")

    user1 = message.from_user
    user2 = message.reply_to_message.from_user

    if user1.id == user2.id:
        return await message.reply_text("<b>😂 Khud se itna pyaar? Thoda dusron ke liye bhi bacha lo!</b>")

    # Love Percentage Logic
    percentage = random.randint(1, 100)
    
    # Status message based on %
    if percentage > 90:
        status = "Made for Each Other! 😍"
    elif percentage > 70:
        status = "Hot Relationship! 🔥"
    elif percentage > 50:
        status = "Good Friends! ✨"
    elif percentage > 30:
        status = "Thoda struggle hai... 🚧"
    else:
        status = "Sirf dushmani hi thik hai! 💀"

    text = (
        f"<b>❤️ ʟᴏᴠᴇ ᴍᴀᴛᴄʜ ᴅᴇᴛᴇᴄᴛᴇᴅ ❤️</b>\n"
        f"{line}\n"
        f"👤 <b>ꜰʀᴏᴍ:</b> {user1.mention}\n"
        f"👤 <b>ᴡɪᴛʜ:</b> {user2.mention}\n\n"
        f"📊 <b>ᴘᴇʀᴄᴇɴᴛᴀɢᴇ:</b> <code>{percentage}%</code>\n"
        f"📝 <b>ᴠᴇʀᴅɪᴄᴛ:</b> {status}\n"
        f"{line}\n"
        f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>ᴢᴇxx 👑</b>"
    )

    await message.reply_text(text)
