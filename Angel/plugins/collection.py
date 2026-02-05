from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- DECORATION ---
line = "✨ ══════════════════ ✨"
owner_name = "ᴢᴇxx"

@Client.on_message(filters.command("collection") & (filters.group | filters.private))
async def bot_collection(client, message):
    # Fast Response with Stylish Buttons
    text = (
        f"<b>📚 ᴀɴɢᴇʟ's ᴄᴏᴍᴍᴀɴᴅ ᴄᴏʟʟᴇᴄᴛɪᴏɴ</b>\n"
        f"{line}\n"
        f"👤 <b>ᴏᴡɴᴇʀ:</b> {owner_name}\n"
        f"🤖 <b>ᴠᴇʀsɪᴏɴ:</b> 𝟸.𝟶 (ꜰᴀsᴛ)\n"
        f"{line}\n"
        f"Niche diye gaye buttons se bot ke saare 'Fast Features' explore karein!"
    )

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🎮 ɢᴀᴍᴇs", callback_data="cb_games"),
            InlineKeyboardButton("🎭 ꜰᴜɴ", callback_data="cb_fun")
        ],
        [
            InlineKeyboardButton("💰 ᴇᴄᴏɴᴏᴍʏ", callback_data="cb_eco"),
            InlineKeyboardButton("📱 sᴏᴄɪᴀʟ", callback_data="cb_social")
        ],
        [
            InlineKeyboardButton("🧩 ʀɪᴅᴅʟᴇ", callback_data="cb_riddle"),
            InlineKeyboardButton("🌸 ᴡᴀɪғᴜ", callback_data="cb_waifu")
        ],
        [
            InlineKeyboardButton("👑 ᴏᴡɴᴇʀ ᴏɴʟʏ", callback_data="cb_owner")
        ]
    ])

    await message.reply_text(text, reply_markup=buttons)

# --- CALLBACK LOGIC (Fast Response) ---
@Client.on_callback_query()
async def cb_handler(client, query):
    data = query.data
    
    # Fast mapping for data
    pages = {
        "cb_games": "🎮 **Games:** /dice, /jumble, /fast, /guess, /slot",
        "cb_fun": "🎭 **Fun:** /kill, /slap, /kiss, /hug, /truth, /dare",
        "cb_eco": "💰 **Economy:** /wallet, /shop, /buy, /daily",
        "cb_social": "📱 **Social:** Just send Instagram/TikTok links!",
        "cb_riddle": "🧩 **Riddle:** Use /riddle to start quiz.",
        "cb_waifu": "🌸 **Waifu:** /waifu, /neko for anime pics.",
        "cb_owner": "👑 **Owner:** /broadcast, /stats, /leave (ZEXX Only)"
    }

    if data in pages:
        await query.answer("Fetching Details...", show_alert=False)
        await query.edit_message_text(
            f"<b>📍 ᴄᴀᴛᴇɢᴏʀʏ: {data.split('_')[1].upper()}</b>\n{line}\n{pages[data]}\n{line}",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="back_main")]])
        )
    
    elif data == "back_main":
        await bot_collection(client, query.message)
        await query.message.delete()
