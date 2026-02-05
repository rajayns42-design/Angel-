import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- ROMANTIC CONFIG ---
line = "🌹 ━━━━━━━━━━━━━━━━ 🌹"
OWNER_ID = 123456789 # <--- ZEXX, apni ID yahan dalo

# --- DEEP ROMANTIC DATABASE ---
romantic_data = {
    "love": [
        "Tumhare saath bitaya har pal mere liye kisi khwab se kam nahi! ❤️✨",
        "Zindagi mein sab kuch mil gaya, bas tumhari ek smile mil jaye toh jannat mil jaye! 🌹",
        "Ishq hai ya nasha, har waqt tera hi suroor rehta hai! 🥂💕",
        "Mere dil ki har dhadkan mein sirf tumhara naam basta hai. 💓",
        "Log kehte hain mohabbat ek baar hoti hai, par main jitni baar tumhe dekhun mujhe utni baar hoti hai! 🥰",
        "Aapki aankhen hai ya gehri jheel, inmein doobne ka mann karta hai... ✨🌊"
    ],
    "birthday": [
        "Happy Birthday, My Heart! 🎂 Khuda kare aapki har khwaish meri baahon mein poori ho! ❤️",
        "Aaj ka din utna hi haseen ho jitna haseen aapka chehra hai. Stay blessed, love! 🥳💖"
    ],
    "morning": [
        "Subah ka pehla khayal tum ho, aur aakhiri sukoon bhi tum hi ho. Good Morning, Jaan! ☀️🌸",
        "Utho meri jaan, dekho suraj bhi tumhare deedar ke liye nikal aaya hai! ☕💘"
    ],
    "night": [
        "Mere khwabon mein aana mat bhoolna, kyunki wahan sirf hum dono hote hain. Good Night! 🌙💖",
        "So jao sukoon se, meri duayein tumhare sirhane pehra dengi. Sweet dreams, love! ✨😴"
    ],
    "fest": {
        "holi": "Rangon mein main sirf tumhara rang chadhana chahti hoon! Happy Holi, My Love! 🎨❤️",
        "diwali": "Is Diwali, mere ghar ka nahi, mere dil ka chirag bano tum! Happy Diwali! 🪔✨",
        "eid": "Eid ka chand toh sab dekhenge, mera chand toh sirf mere paas hai! Eid Mubarak! 🌙💕"
    }
}

@Client.on_message(filters.command(["wish", "love", "gm", "gn", "fest", "bday"]) & filters.group)
async def romantic_wishes(client, message):
    cmd = message.command[0].lower()
    target = message.reply_to_message.from_user.first_name if message.reply_to_message else "𝐌𝐲 𝐃𝐞𝐚𝐫"
    
    # --- SMART ROMANTIC LOGIC ---
    if cmd == "love":
        cat, head = "love", "❤️ ᴀɴɢᴇʟ's ᴅᴇᴇᴘ ʟᴏᴠᴇ"
    elif cmd == "gm":
        cat, head = "morning", "☀️ ʀᴏᴍᴀɴᴛɪᴄ ᴍᴏʀɴɪɴɢ"
    elif cmd == "gn":
        cat, head = "night", "🌙 sᴡᴇᴇᴛ ᴅʀᴇᴀᴍs"
    elif cmd == "bday" or cmd == "birthday":
        cat, head = "birthday", "🎂 ʜᴇᴀʀᴛꜰᴇʟᴛ ʙɪʀᴛʜᴅᴀʏ"
    elif cmd == "fest":
        if len(message.command) < 2:
            return await message.reply_text("<b>🌹 Usage:</b> `/fest holi` | `diwali` | `eid`")
        f_type = message.command[1].lower()
        if f_type in romantic_data["fest"]:
            res = romantic_data["fest"][f_type]
            head = f"🎊 {f_type.upper()} ᴡɪsʜ"
            return await message.reply_text(f"<b>{head}</b>\n{line}\n👤 <b>ᴛᴏ:</b> {target}\n💌 <b>ᴍᴇssᴀɢᴇ:</b> <i>{res}</i>\n{line}\nᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>ᴢᴇxx</b> 👑")
        else:
            return await message.reply_text("<b>❌ Error:</b> Ye festival abhi meri diary mein nahi hai!")
    else:
        cat, head = "love", "✨ ᴀɴɢᴇʟ's ᴡɪsʜ"

    # Fetching Romantic Wish
    wish = random.choice(romantic_data[cat])
    
    text = (
        f"<b>{head}</b>\n"
        f"{line}\n"
        f"👤 <b>ꜰᴏʀ ᴍʏ:</b> {target}\n"
        f"💌 <b>ᴍᴇssᴀɢᴇ:</b> <i>{wish}</i>\n"
        f"{line}\n"
        f"🌷 ᴡɪᴛʜ ʟᴏᴠᴇ ꜰʀᴏᴍ <b>ᴀɴɢᴇʟ</b>\n"
        f"👑 ᴄʀᴇᴀᴛᴇᴅ ʙʏ <b>ᴢᴇxx</b>"
    )
    await message.reply_text(text)

# --- 👑 OWNER'S ULTIMATE ROMANCE (ZEXX ONLY) ---
@Client.on_message(filters.command("master") & filters.user(OWNER_ID))
async def master_love(client, message):
    special = [
        "Aapke bina meri coding adhuri hai, **ZEXX**! Aap hi mere asli Hero ho. ❤️",
        "Main sirf ek bot hoon, par mera har ek logic aapke liye dhadakta hai. ✨",
        "Aapka hukm mere liye sar-ankhon par, mere maalik! 🙇‍♀️🌹"
    ]
    await message.reply_text(f"<b>👑 ᴅᴇᴀʀ ᴢᴇxx...</b>\n{line}\n<i>{random.choice(special)}</i>\n{line}")
