from pyrogram import Client, filters
from pyrogram.types import Message

# --- DECORATION ---
line = "✨ ══════════════════ ✨"

# --- WELCOME EVENT ---
@Client.on_message(filters.new_chat_members)
async def welcome_event(client, message):
    for member in message.new_chat_members:
        await message.reply_text(
            f"<b>🌟 ɴᴇᴡ ᴍᴇᴍʙᴇʀ ᴅᴇᴛᴇᴄᴛᴇᴅ!</b>\n"
            f"{line}\n"
            f"ʜᴇʏ <a href='tg://user?id={member.id}'>{member.first_name}</a>,\n"
            f"ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ <b>{message.chat.title}</b>!\n\n"
            f"<b>🆔 ɪᴅ:</b> <code>{member.id}</code>\n"
            f"<b>👤 ᴜsᴇʀ:</b> @{member.username if member.username else 'No Username'}\n"
            f"{line}\n"
            f"<i>ᴍᴀᴋᴇ sᴜʀᴇ ᴛᴏ ʀᴇᴀᴅ ᴛʜᴇ ɢʀᴏᴜᴘ ʀᴜʟᴇs!</i>"
        )

# --- GOODBYE EVENT ---
@Client.on_message(filters.left_chat_member)
async def goodbye_event(client, message):
    user = message.left_chat_member
    await message.reply_text(
        f"<b>💔 sᴀᴅ ᴅᴇᴘᴀʀᴛᴜʀᴇ!</b>\n"
        f"{line}\n"
        f"<b>{user.first_name}</b> ᴊᴜsᴛ ʟᴇғᴛ ᴛʜᴇ ɢʀᴏᴜᴘ.\n\n"
        f"<b>✨ sᴛᴀᴛᴜs:</b> ʟᴇғᴛ ᴛʜᴇ ᴄʜᴀᴛ\n"
        f"<b>👋 ᴍᴇssᴀɢᴇ:</b> ᴡᴇ ᴡɪʟʟ ᴍɪss ʏᴏᴜ!\n"
        f"{line}"
    )

# --- PINNED MESSAGE EVENT (Optional) ---
@Client.on_message(filters.pinned_message)
async def pinned_event(client, message):
    await message.reply_text(
        f"<b>📌 ɴᴇᴡ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ!</b>\n"
        f"{line}\n"
        f"ᴀᴅᴍɪɴ ʜᴀs ᴘɪɴɴᴇᴅ ᴀ ɴᴇᴡ ᴍᴇssᴀɢᴇ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.\n"
        f"ᴋɪɴᴅʟʏ ᴄʜᴇᴄᴋ ɪᴛ ᴏᴜᴛ ᴛᴏ sᴛᴀʏ ᴜᴘᴅᴀᴛᴇᴅ!\n"
        f"{line}"
    )
