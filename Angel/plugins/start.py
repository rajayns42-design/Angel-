from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from config import START_IMG, BOT_NAME, OWNER_USERNAME, SUPPORT_CHAT, UPDATE_CHANNEL, BOT_OWNER

# --- 𝐒𝐓𝐀𝐑𝐓 𝐇𝐀𝐍𝐃𝐋𝐄𝐑 ---
@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):
    TEXT = (
        f"👋 **𝐊𝐨𝐧'𝐧𝐢𝐜𝐡𝐢𝐰𝐚 ๛ [𝐙𝐄𝐗𝐗](https://t.me/{OWNER_USERNAME})...!!!** (≧▽≦)\n\n"
        f"『 🍥 **{BOT_NAME}** 』\n"
        f"*ᴛʜᴇ ᴀᴇsᴛʜᴇᴛɪᴄ ᴀɪ-ᴘᴏᴡᴇʀᴇᴅ ʀᴘɢ ʙᴏᴛ!* 🌸\n\n"
        f"🩸 **𝐌𝐀𝐅𝐈𝐀 𝐀𝐍𝐆𝐄𝐋 𝐄𝐃𝐈𝐓𝐈𝐎𝐍** 🩸\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"ɪ ᴀᴍ ᴛʜᴇ **ᴀɴɢᴇʟ ᴏғ ᴅᴇᴀᴛʜ** ɪɴ ᴛʜᴇ ᴜɴᴅᴇʀᴡᴏʀʟᴅ.\n"
        f"ᴄʟɪᴄᴋ ᴛʜᴇ **ʜᴇʟᴘ ᴍᴇɴᴜ** ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ\n"
        f"ʜᴏᴡ ᴛᴏ ʀᴜʟᴇ ᴛʜᴇ sᴛʀᴇᴇᴛs!\n\n"
        f"👑 **𝐌𝐀𝐒𝐓𝐄𝐑 : {BOT_OWNER}** [cite: 2026-02-04]\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━"
    )

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📢 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 ↗️", url=UPDATE_CHANNEL),
            InlineKeyboardButton("💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ↗️", url=SUPPORT_CHAT)
        ],
        [
            InlineKeyboardButton("✨ 𝐀𝐝𝐝 𝐌𝐞 𝐁𝐚𝐛𝐲 ✨", url=f"https://t.me/{client.me.username}?startgroup=true")
        ],
        [
            InlineKeyboardButton("📖 𝐇𝐞𝐥𝐩 𝐌𝐞𝐧𝐮", callback_data="h_back"),
            InlineKeyboardButton("👑 𝐎𝐰𝐧𝐞𝐫 ↗️", url=f"https://t.me/{OWNER_USERNAME}")
        ]
    ])

    await message.reply_photo(
        photo=START_IMG,
        caption=TEXT,
        reply_markup=buttons
    )

# --- 𝐇𝐄𝐋𝐏 & 𝐔𝐒𝐀𝐆𝐄 𝐋𝐎𝐆𝐈𝐂 ---
@Client.on_callback_query(filters.regex(r"h_(.*)"))
async def help_callback(client: Client, cb: CallbackQuery):
    data = cb.data.split("_")[1]
    
    if data == "eco":
        text = (
            "💰 **𝐄𝐂𝐎𝐍𝐎𝐌𝐘 𝐒𝐘𝐒𝐓𝐄𝐌**\n\n"
            "• `/bal` - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴡᴀʟʟᴇᴛ\n"
            "• `/daily` - ᴄʟᴀɪᴍ ꜰʀᴇᴇ ᴄᴏɪɴs\n"
            "• `/shop` - ʙᴜʏ ᴡᴇᴀᴘᴏɴs & ᴀʀᴍᴏʀ\n"
            "• `/pay [user] [amt]` - sᴇɴᴅ ᴍᴏɴᴇʏ"
        )
    elif data == "bank":
        text = (
            "🏦 **𝐁𝐀𝐍𝐊𝐈𝐍𝐆 𝐕𝐀𝐔𝐋𝐓**\n\n"
            "• `/dep [amt]` - sᴀᴠᴇ ᴍᴏɴᴇʏ ɪɴ ʙᴀɴᴋ\n"
            "• `/with [amt]` - ᴛᴀᴋᴇ ᴍᴏɴᴇʏ ᴏᴜᴛ\n"
            "• `/bank` - ᴄʜᴇᴄᴋ ʙᴀɴᴋ sᴛᴀᴛᴜs"
        )
    elif data == "maf":
        text = (
            "🔪 **𝐌𝐀𝐅𝐈𝐀 𝐖𝐀𝐑𝐅𝐀𝐑𝐄**\n\n"
            "• `/kill [reply]` - ᴀssᴀssɪɴᴀᴛᴇ ᴇɴᴇᴍʏ\n"
            "• `/rob [reply]` - sᴛᴇᴀʟ ᴛʜᴇɪʀ ᴄᴀsʜ\n"
            "• `/bounty [amt]` - ᴘᴜᴛ ᴀ ʜɪᴛ ᴏɴ sᴏᴍᴇᴏɴᴇ"
        )
    elif data == "cas":
        text = (
            "🎲 **𝐂𝐀𝐒𝐈𝐍𝐎 & 𝐋𝐔𝐂𝐊**\n\n"
            "• `/bet [amt]` - ɢᴀᴍʙʟᴇ ʏᴏᴜʀ ʟᴜᴄᴋ\n"
            "• `/slots` - ᴘʟᴀʏ ᴍᴀғɪᴀ sʟᴏᴛs\n"
            "• `/dice` - ʀᴏʟʟ ᴛʜᴇ ᴅᴇᴀᴛʜ ᴅɪᴄᴇ"
        )
    elif data == "soc":
        text = (
            "💍 **𝐒𝐎𝐂𝐈𝐀𝐋 𝐄𝐌𝐏𝐈𝐑𝐄**\n\n"
            "• `/propose [reply]` - ᴀsᴋ ᴛᴏ ᴍᴀʀʀʏ\n"
            "• `/divorce` - ᴇɴᴅ ʀᴇʟᴀᴛɪᴏɴsʜɪᴘ\n"
            "• `/waifu` - ᴄʟᴀɪᴍ ʏᴏᴜʀ ᴀɴɪᴍᴇ ɢɪʀʟ"
        )
    elif data == "cou":
        text = (
            "💞 **𝐂𝐎𝐔𝐏𝐋𝐄 𝐙𝐎𝐍𝐄**\n\n"
            "• `/love [reply]` - ᴄʜᴇᴄᴋ ʟᴏᴠᴇ %\n"
            "• `/ship` - ᴍᴀᴋᴇ ᴀ ʀᴀɴᴅᴏᴍ ᴄᴏᴜᴘʟᴇ\n"
            "• `/wishes` - sᴇɴᴅ sᴘᴇᴄɪᴀʟ ɢɪғᴛs"
        )
    elif data == "fun":
        text = (
            "🧠 **𝐀𝐈 & 𝐅𝐔𝐍**\n\n"
            "• `/ask [msg]` - ᴄʜᴀᴛ ᴡɪᴛʜ sᴀssʏ ᴀɪ\n"
            "• `/riddle` - sᴏʟᴠᴇ ᴍᴀғɪᴀ ᴘᴜᴢᴢʟᴇs\n"
            "• `/game` - sᴛᴀʀᴛ ᴍɪɴɪ ɢᴀᴍᴇ"
        )
    elif data == "gua":
        text = (
            "🛡️ **𝐆𝐔𝐀𝐑𝐃𝐈𝐀𝐍 𝐒𝐇𝐈𝐄𝐋𝐃**\n\n"
            "• `/guard on` - ᴘʀᴏᴛᴇᴄᴛ ᴛʜᴇ ɢʀᴏᴜᴘ\n"
            "• `/anti_nsfw` - ʙʟᴏᴄᴋ ᴅɪʀᴛʏ ᴍᴇᴅɪᴀ\n"
            "• `/welcome on` - ɢʀᴇᴇᴛ ɴᴇᴡ ᴍᴇᴍʙᴇʀs"
        )
    elif data == "adm":
        text = (
            "🛠️ **𝐀𝐃𝐌𝐈𝐍 𝐂𝐎𝐍𝐓𝐑𝐎𝐋**\n\n"
            "• `/broadcast` - ᴍsɢ ᴛᴏ ᴀʟʟ ᴜsᴇʀs\n"
            "• `/add_prem` - ɢɪᴠᴇ ᴠɪᴘ sᴛᴀᴛᴜs\n"
            "• `/global_board` - sᴇᴇ ᴛᴏᴘ ʀɪᴄʜᴇsᴛ"
        )
    
    elif data == "back":
        text = "⚔️ **𝐀𝐍𝐆𝐄𝐋 x𝐁~ 𝐔𝐍𝐃𝐄𝐑𝐖𝐎𝐑𝐋𝐃 𝐌𝐄𝐍𝐔** ⚔️\n━━━━━━━━━━━━━━━━━━━━\nᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ᴛᴏ sᴇᴇ ᴄᴏᴍᴍᴀɴᴅs."
        buttons = [
            [InlineKeyboardButton("💰 𝐄𝐂𝐎𝐍𝐎𝐌𝐘", callback_data="h_eco"), InlineKeyboardButton("🏦 𝐁𝐀𝐍𝐊", callback_data="h_bank")],
            [InlineKeyboardButton("🔪 𝐌𝐀𝐅𝐈𝐀", callback_data="h_maf"), InlineKeyboardButton("🎲 𝐂𝐀𝐒𝐈𝐍𝐎", callback_data="h_cas")],
            [InlineKeyboardButton("💍 𝐒𝐎𝐂𝐈𝐀𝐋", callback_data="h_soc"), InlineKeyboardButton("💞 𝐂𝐎𝐔𝐏𝐋𝐄", callback_data="h_cou")],
            [InlineKeyboardButton("🧠 𝐀𝐈 & 𝐅𝐔𝐍", callback_data="h_fun"), InlineKeyboardButton("🛡️ 𝐆𝐔𝐀𝐑𝐃", callback_data="h_gua")],
            [InlineKeyboardButton("🛠️ 𝐀𝐃𝐌𝐈𝐍", callback_data="h_adm")]
        ]
        return await cb.edit_message_caption(
            caption=f"{text}\n\n━━━━━━━━━━━━━━━━━━━━\n**𝐎𝐖𝐍𝐄𝐑 : {BOT_OWNER} ✦** [cite: 2026-02-04]",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    await cb.edit_message_caption(
        caption=f"{text}\n\n━━━━━━━━━━━━━━━━━━━━\n**𝐎𝐖𝐍𝐄𝐑 : {BOT_OWNER} ✦** [cite: 2026-02-04]",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ 𝐁𝐀𝐂𝐊", callback_data="h_back")]])
    )
