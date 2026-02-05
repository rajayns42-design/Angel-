import random
from pyrogram import Client, filters

# --- BREAKUP DATABASE ---
SHAYARI = [
    "Humne toh dil diya tha, unhone toh dushman samajh liya... 💔",
    "Mohabbat bhi unhi se hoti hai, jinhe milna naseeb mein nahi hota.",
    "Ab ke hum bichde toh shayad khwabon mein milein...",
    "Dil toota hai toh awaaz nahi aayi, par dard poori duniya ne suna.",
    "Yaad rakhenge hum bhi, ki koi tha zindagi mein jo bina kahe sab samajh leta tha."
]

QUOTES = [
    "Akele rehna seekh lo, yahan koi kisi ka nahi hota. 🕶️",
    "Don't cry because it's over, smile because he/she is someone else's problem now.",
    "My heart is currently under construction.",
    "Broken but still the King. 👑"
]

line = "🥀 ━━━━━━━━━━━━━━━━━━━━ 🥀"

@Client.on_message(filters.command("breakup"))
async def breakup_mode(client, message):
    # Randomly pick between Shayari or Quote
    mode = random.choice(["shayari", "quote"])
    
    if mode == "shayari":
        content = random.choice(SHAYARI)
        title = "💔 #ʙʀᴏᴋᴇɴ_ʜᴇᴀʀᴛ_ᴠɪʙᴇs"
    else:
        content = random.choice(QUOTES)
        title = "🕶️ #sᴀᴠᴀɢᴇ_ʙʀᴇᴀᴋᴜᴘ"

    text = (
        f"<b>{title}</b>\n"
        f"{line}\n\n"
        f"<i>\"{content}\"</i>\n\n"
        f"{line}\n"
        f"ᴏᴡɴᴇʀ: <b>ᴢᴇxx 👑</b>"
    )
    
    await message.reply_text(text)

# --- 💔 SAD STATUS FOR PROFILE ---
@Client.on_message(filters.command("sad_status"))
async def sad_status(client, message):
    status = random.choice(SHAYARI)
    await message.reply_text(f"<b>🥀 ʏᴏᴜʀ ɴᴇᴡ sᴛᴀᴛᴜs:</b>\n\n<code>{status}</code>")
