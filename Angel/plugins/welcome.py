import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- SETTINGS ---
WELCOME_IMG = "https://telegra.ph/file/your_image_url.jpg" # Apna mast wala image link dalo
SUPPORT = "https://t.me/ZEXX_SUPPORT" # Apna support link
line = "✨ ━━━━━━━━━━━━━━━ ✨"

@Client.on_message(filters.command("welcome") & filters.group)
async def welcome_toggle(client, message):
    # Admin Check
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if user.status not in ["administrator", "creator"]:
        return await message.reply_text("<b>❌ ᴀᴅᴍɪɴ ᴏɴʟʏ ᴀᴄᴄᴇss!</b>")

    if len(message.command) < 2:
        return await message.reply_text("<b>⚠️ ᴜsᴀɢᴇ:</b>\n`/welcome on` | `/welcome off`")

    state = message.command[1].lower()
    if state == "on":
        await message.reply_text(f"<b>✅ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇs:</b> <code>ᴇɴᴀʙʟᴇᴅ</code>")
    elif state == "off":
        await message.reply_text(f"<b>❌ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇs:</b> <code>ᴅɪsᴀʙʟᴇᴅ</code>")

@Client.on_message(filters.new_chat_members)
async def stylish_welcome(client, message):
    for member in message.new_chat_members:
        
        # --- 🤖 BOT ENTERS GROUP ---
        if member.id == (await client.get_me()).id:
            adder = message.from_user.first_name
            txt = (
                f"<b>🌸 ᴀʀɪɢᴀᴛᴏ, {adder}!</b>\n"
                f"{line}\n"
                f"ᴛʜᴀɴᴋs ꜰᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ɪɴ\n"
                f"<b>📍 ᴄʜᴀᴛ:</b> <code>{message.chat.title}</code>\n\n"
                f"🎁 <b>ꜰɪʀsᴛ ᴛɪᴍᴇ ʙᴏɴᴜs:</b>\n"
                f"ᴛʏᴘᴇ `/claim` ᴛᴏ ɢᴇᴛ <b>𝟸,𝟶𝟶𝟶</b> ᴄᴏɪɴs!\n"
                f"{line}\n"
                f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>ᴢᴇxx</b> 👑"
            )
            kb = InlineKeyboardMarkup([[InlineKeyboardButton("✨ sᴜᴘᴘᴏʀᴛ", url=SUPPORT)]])
            
            try: await message.reply_photo(photo=WELCOME_IMG, caption=txt, reply_markup=kb)
            except: await message.reply_text(txt, reply_markup=kb)

        # --- 👤 NEW USER JOINS ---
        else:
            greetings = ["ʜᴇʟʟᴏ", "ʜɪɪɪ", "ᴡᴇʟᴄᴏᴍᴇ", "ᴋᴏɴ'ɴɪᴄʜɪᴡᴀ", "ᴀᴅᴀʙ"]
            greet = random.choice(greetings)
            mention = f"<a href='tg://user?id={member.id}'>{member.first_name}</a>"
            
            txt = (
                f"<b>{greet}, {mention}! 👋</b>\n"
                f"{line}\n"
                f"ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ <b>{message.chat.title}</b>\n\n"
                f"✨ ʜᴀᴠᴇ ᴀ ɢʀᴇᴀᴛ ᴛɪᴍᴇ ʜᴇʀᴇ!\n"
                f"💡 ᴅᴏɴ'ᴛ ꜰᴏʀɢᴇᴛ ᴛᴏ `/register`!\n"
                f"{line}\n"
                f"🌷 <b>ᴇɴᴊᴏʏ ʏᴏᴜʀ sᴛᴀʏ!</b>"
            )
            
            try: await message.reply_photo(photo=WELCOME_IMG, caption=txt)
            except: await message.reply_text(txt)
