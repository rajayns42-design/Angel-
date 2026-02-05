from pyrogram import Client, filters
from pyrogram.types import ChatPermissions

# --- CUSTOM DECORATIONS ---
line = "━━━━━━━━━━━━━━━━━━━━"

# --- BAN COMMAND ---
@Client.on_message(filters.command("ban") & filters.group)
async def ban_user(client, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>❌ Error:</b> Pehle kisi ke message par reply karein!")
    
    user = message.reply_to_message.from_user
    await message.chat.ban_member(user.id)
    await message.reply_text(
        f"<b>🚀 User Banned Successfully!</b>\n"
        f"{line}\n"
        f"<b>👤 Name:</b> <code>{user.first_name}</code>\n"
        f"<b>🆔 ID:</b> <code>{user.id}</code>\n"
        f"<b>👮 Action:</b> <u>Banned</u>\n"
        f"<b>✨ Status:</b> Kick Out From Paradise\n"
        f"{line}"
    )

# --- MUTE COMMAND ---
@Client.on_message(filters.command("mute") & filters.group)
async def mute_user(client, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>🔇 Error:</b> Kise chup karana hai?")
    
    user = message.reply_to_message.from_user
    await message.chat.restrict_member(user.id, ChatPermissions(can_send_messages=False))
    await message.reply_text(
        f"<b>🤐 User Has Been Muted!</b>\n"
        f"{line}\n"
        f"<b>👤 Name:</b> <code>{user.first_name}</code>\n"
        f"<b>👮 Action:</b> <u>Mute</u>\n"
        f"<b>🔇 Silence:</b> Enabled\n"
        f"{line}"
    )

# --- UNMUTE COMMAND ---
@Client.on_message(filters.command("unmute") & filters.group)
async def unmute_user(client, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>🔊 Error:</b> Reply kijiye!")
    
    user = message.reply_to_message.from_user
    await message.chat.restrict_member(user.id, ChatPermissions(can_send_messages=True))
    await message.reply_text(
        f"<b>🔔 User Is Now Unmuted!</b>\n"
        f"{line}\n"
        f"<b>👤 Name:</b> <code>{user.first_name}</code>\n"
        f"<b>👮 Action:</b> <u>Unmute</u>\n"
        f"<b>🎙️ Mic:</b> Turned On\n"
        f"{line}"
    )

# --- KICK COMMAND ---
@Client.on_message(filters.command("kick") & filters.group)
async def kick_user(client, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>👞 Error:</b> Reply karein!")
    
    user = message.reply_to_message.from_user
    await message.chat.ban_member(user.id)
    await message.chat.unban_member(user.id)
    await message.reply_text(
        f"<b>👞 User Kicked Out!</b>\n"
        f"{line}\n"
        f"<b>👤 Name:</b> <code>{user.first_name}</code>\n"
        f"<b>👮 Action:</b> <u>Kicked</u>\n"
        f"<b>⚠️ Note:</b> Don't come back soon!\n"
        f"{line}"
    )
