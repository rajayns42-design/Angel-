from pyrogram import Client, filters
from pyrogram.types import Message

# --- CONFIG ---
# ZEXX, apne Log Group ki ID yahan dalo
LOG_GROUP_ID = -100123456789 
line = "✨ ━━━━━━━━━━━━━━━━━━━━ ✨"
top_border = "╔══════════════════════╗"
bottom_border = "╚══════════════════════╝"
owner_tag = "ᴢᴇxx 👑"

# 1. 📥 LOGGER: ADDED TO NEW GROUP (GRAND STYLE)
@Client.on_message(filters.new_chat_members)
async def group_added_log(client, message):
    if message.new_chat_members:
        for member in message.new_chat_members:
            if member.id == (await client.get_me()).id:
                chat = message.chat
                adder = message.from_user 
                
                adder_name = adder.first_name
                adder_id = adder.id
                adder_username = f"@{adder.username}" if adder.username else "ɴᴏ ᴜsᴇʀɴᴀᴍᴇ"
                adder_link = f"tg://user?id={adder_id}"
                
                log_text = (
                    f"<b>📥 #ɴᴇᴡ_ɢʀᴏᴜᴘ_ᴀᴅᴅᴇᴅ</b>\n"
                    f"<code>{top_border}</code>\n"
                    f"🏰 <b>ɢʀᴏᴜᴘ:</b> <code>{chat.title}</code>\n"
                    f"🆔 <b>ᴄʜᴀᴛ ɪᴅ:</b> <code>{chat.id}</code>\n"
                    f"{line}\n"
                    f"👤 <b>ᴀᴅᴅᴇᴅ ʙʏ:</b> <a href='{adder_link}'>{adder_name}</a>\n"
                    f"🆔 <b>ᴀᴅᴅᴇʀ ɪᴅ:</b> <code>{adder_id}</code>\n"
                    f"🔗 <b>ᴜsᴇʀɴᴀᴍᴇ:</b> {adder_username}\n"
                    f"{line}\n"
                    f"👥 <b>ᴍᴇᴍʙᴇʀs:</b> <code>{await client.get_chat_members_count(chat.id)}</code>\n"
                    f"<code>{bottom_border}</code>\n"
                    f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>{owner_tag}</b>"
                )
                await client.send_message(LOG_GROUP_ID, log_text, disable_web_page_preview=True)

# 2. 📤 LOGGER: REMOVED/LEFT FROM GROUP (SAD STYLE)
@Client.on_message(filters.left_chat_member)
async def group_left_log(client, message):
    if message.left_chat_member.id == (await client.get_me()).id:
        chat = message.chat
        
        log_text = (
            f"<b>📤 #ʙᴏᴛ_ʟᴇꜰᴛ_ᴄʜᴀᴛ</b>\n"
            f"<code>{top_border}</code>\n"
            f"🏰 <b>ɢʀᴏᴜᴘ:</b> <code>{chat.title}</code>\n"
            f"🆔 <b>ᴄʜᴀᴛ ɪᴅ:</b> <code>{chat.id}</code>\n"
            f"{line}\n"
            f"❌ <b>sᴛᴀᴛᴜs:</b> ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ\n"
            f"⚠️ <b>ᴀʟᴇʀᴛ:</b> ᴀɴɢᴇʟ ɪs ɴᴏᴡ ᴏꜰꜰʟɪɴᴇ ʜᴇʀᴇ.\n"
            f"<code>{bottom_border}</code>\n"
            f"ᴍᴀɴᴀɢᴇᴅ ʙʏ: <b>{owner_tag}</b>"
        )
        await client.send_message(LOG_GROUP_ID, log_text)

# 3. 🔔 LOGGER: PRIVATE START (CLEAN STYLE)
@Client.on_message(filters.command("start") & filters.private)
async def start_log(client, message):
    user = message.from_user
    profile_link = f"tg://user?id={user.id}"
    
    log_text = (
        f"<b>🚀 #ʙᴏᴛ_sᴛᴀʀᴛᴇᴅ</b>\n"
        f"<code>{top_border}</code>\n"
        f"👤 <b>ᴜsᴇʀ:</b> <a href='{profile_link}'>{user.first_name}</a>\n"
        f"🆔 <b>ɪᴅ:</b> <code>{user.id}</code>\n"
        f"🔗 <b>ᴜsᴇʀɴᴀᴍᴇ:</b> @{user.username if user.username else 'None'}\n"
        f"<code>{bottom_border}</code>\n"
        f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>{owner_tag}</b>"
    )
    await client.send_message(LOG_GROUP_ID, log_text, disable_web_page_preview=True)
