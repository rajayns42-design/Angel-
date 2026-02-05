from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import START_IMG, BOT_OWNER

# Database ki jagah temporary status (Real DB ke liye MongoDB use karein)
welcome_status = {}

@Client.on_message(filters.new_chat_members)
async def welcome_bot(client: Client, message: Message):
    chat_id = message.chat.id
    
    # Check if welcome is ON or OFF (Default: ON)
    if not welcome_status.get(chat_id, True):
        return

    for user in message.new_chat_members:
        TEXT = (
            f"🩸 **𝐍𝐄𝐖 𝐁𝐋𝐎𝐎𝐃 𝐃𝐄𝐓𝐄𝐂𝐓𝐄𝐃** 🩸\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"👤 **𝐇𝐞𝐥𝐥𝐨**, {user.mention} !\n\n"
            f"ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ **{message.chat.title}**.\n"
            f"ʏᴏᴜ ᴀʀᴇ ɴᴏᴡ ᴜɴᴅᴇʀ ᴛʜᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ\n"
            f"ᴏғ ᴛʜᴇ **ᴀɴɢᴇʟ xʙ~** ᴍᴀғɪᴀ ғᴀᴍɪʟʏ.\n\n"
            f"🛡️ **𝐑𝐔𝐋𝐄 :** ᴅᴏɴ'ᴛ ɢᴇᴛ ᴋɪʟʟᴇᴅ.\n"
            f"👑 **𝐌𝐀𝐒𝐓𝐄𝐑 : {BOT_OWNER}** [cite: 2026-02-04]\n"
            f"━━━━━━━━━━━━━━━━━━━━"
        )
        
        if START_IMG:
            await message.reply_photo(photo=START_IMG, caption=TEXT)
        else:
            await message.reply_text(TEXT)

# --- 𝐎𝐍/𝐎𝐅𝐅 𝐂𝐎𝐍𝐓𝐑𝐎𝐋 (𝐀𝐝𝐦𝐢𝐧 𝐎𝐧𝐥𝐲) ---
@Client.on_message(filters.command("welcome") & filters.group)
async def toggle_welcome(client: Client, message: Message):
    # Only Admin or ZEXX can change settings
    if len(message.command) < 2:
        return await message.reply_text("🩸 **𝐔𝐬𝐚𝐠𝐞:** `/welcome on` **or** `/welcome off`")
    
    chat_id = message.chat.id
    state = message.command[1].lower()
    
    if state == "on":
        welcome_status[chat_id] = True
        await message.reply_text("✅ **𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐒𝐘𝐒𝐓𝐄𝐌 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐃**")
    elif state == "off":
        welcome_status[chat_id] = False
        await message.reply_text("❌ **𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐒𝐘𝐒𝐓𝐄𝐌 𝐃𝐄𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐃**")
    else:
        await message.reply_text("❗ **𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐒𝐭𝐚𝐭𝐞! 𝐔𝐬𝐞 on/off.**")
