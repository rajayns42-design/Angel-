from pyrogram import Client, filters

# --- FAST KILL CONFIG ---
line = "✨ ══════════════════ ✨"

@Client.on_message(filters.command("kill") & filters.group)
async def fast_kill(client, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>🔪 Kise marna hai? Reply toh karo!</b>")

    target = message.reply_to_message.from_user.first_name
    sender = message.from_user.first_name

    # Ekdum fast reply bina faltu processing ke
    await message.reply_text(
        f"<b>💀 ɪɴsᴛᴀɴᴛ ᴋɪʟʟ</b>\n"
        f"{line}\n"
        f"<b>{sender}</b> ne <b>{target}</b> ka game baja diya! 🔪\n\n"
        f"☠️ <b>sᴛᴀᴛᴜs: ᴅᴇᴀᴅ</b> ☠️\n"
        f"{line}\n"
        f"<i>ᴀɴɢᴇʟ sᴇ ᴘᴀɴɢᴀ ɴᴀʜɪ ʟᴇɴᴀ! 🔥</i>"
    )
