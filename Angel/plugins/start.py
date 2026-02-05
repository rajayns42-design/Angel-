from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import START_IMG, BOT_NAME, OWNER_USERNAME, SUPPORT_CHAT, UPDATE_CHANNEL, BOT_OWNER

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):
    # Stylish Caption based on your image style
    TEXT = (
        f"👋 **𝐊𝐨𝐧'𝐧𝐢𝐜𝐡𝐢𝐰𝐚 ๛ [𝐙𝐄𝐗𝐗](https://t.me/{OWNER_USERNAME})...!!!** (≧▽≦)\n\n"
        f"『 🍥 **{BOT_NAME}** 』\n"
        f"*ᴛʜᴇ ᴀᴇsᴛʜᴇᴛɪᴄ ᴀɪ-ᴘᴏᴡᴇʀᴇᴅ ʀᴘɢ ʙᴏᴛ!* 🌸\n\n"
        f"🎮 **𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬:**\n"
        f"▶ **𝐑𝐏𝐆:** ᴋɪʟʟ, ʀᴏʙ (𝟷𝟶𝟶%), ᴘʀᴏᴛᴇᴄᴛ\n"
        f"▶ **𝐒𝐨𝐜𝐢𝐚𝐥:** ᴍᴀʀʀʏ, ᴄᴏᴜᴘʟᴇ\n"
        f"▶ **𝐄𝐜𝐨𝐧𝐨𝐦𝐲:** ᴄʟᴀɪᴍ, ɢɪᴠᴇ\n"
        f"▶ **𝐀𝐈:** sᴀssʏ ᴄʜᴀᴛʙᴏᴛ\n\n"
        f"☁️ **𝐍𝐞𝐞𝐝 𝐇𝐞𝐥𝐩?**\n"
        f"ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ!\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👑 **𝐌𝐀𝐒𝐓𝐄𝐑 : {BOT_OWNER}** [cite: 2026-02-04]"
    )

    # Stylish Buttons (Exactly like the photo)
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📢 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 ↗️", url=UPDATE_CHANNEL),
            InlineKeyboardButton("💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ↗️", url=SUPPORT_CHAT)
        ],
        [
            InlineKeyboardButton("✨ 𝐀𝐝𝐝 𝐌𝐞 𝐁𝐚𝐛𝐲 ✨", url=f"https://t.me/{client.me.username}?startgroup=true")
        ],
        [
            InlineKeyboardButton("📖 𝐇𝐞𝐥𝐩 𝐌𝐞𝐧𝐮", callback_data="help_back_main"),
            InlineKeyboardButton("👑 𝐎𝐰𝐧𝐞𝐫 ↗️", url=f"https://t.me/{OWNER_USERNAME}")
        ]
    ])

    await message.reply_photo(
        photo=START_IMG,
        caption=TEXT,
        reply_markup=buttons
    )

