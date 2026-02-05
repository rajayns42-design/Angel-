import random
import asyncio
from pyrogram import Client, filters
from Angel.plugins.mood import BREAKUP_MODE

line = "━━━━━━━━━━━━━━━━━━━━"

# List of Virtual Girlfriends
GF_NAMES = [
    "Simran", "Priya", "Sneha", "Anjali", "Muskan", 
    "Riya", "Kavya", "Zoya", "Ishani", "Sana"
]

@Client.on_message(filters.command(["gf", "girlfriend"]) & filters.group)
async def get_girlfriend(client, message):
    chat_id = message.chat.id
    user = message.from_user

    # Mood Check (Breakup mode mein GF nahi milegi)
    if BREAKUP_MODE.get(chat_id):
        return await message.reply_text("<b>💔 BREAKUP MODE ON HAI!</b>\nAbhi koi setting nahi hogi, sirf rona-dhona chalega.")

    status_msg = await message.reply_text("<b>🔍 Aapki kismat check kar raha hoon...</b>")
    await asyncio.sleep(2) # Suspense ke liye delay

    # 70% chance hai ki GF mil jaye, 30% chance ki "Naseeb Kharab"
    success = random.random() < 0.70

    if success:
        gf_name = random.choice(GF_NAMES)
        gift = random.choice(["Chocolate 🍫", "Rose 🌹", "Ring 💍", "Teddy 🧸"])
        
        text = (
            f"<b>🎉 ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs! 🎉</b>\n"
            f"{line}\n"
            f"👤 <b>ᴜsᴇʀ:</b> {user.mention}\n"
            f"👩‍❤️‍👨 <b>ᴀᴘᴋɪ ɴᴀʏɪ ɢꜰ:</b> <code>{gf_name}</code>\n"
            f"🎁 <b>ɢɪꜰᴛ:</b> {gift}\n"
            f"{line}\n"
            f"<i>Ab iska khayal rakhna, warna koi aur rob kar lega!</i>\n"
            f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>ᴢᴇxx 👑</b>"
        )
    else:
        text = (
            f"<b>🚫 ɴᴀsᴇᴇʙ ᴋʜᴀʀᴀʙ 🚫</b>\n"
            f"{line}\n"
            f"👤 <b>ᴜsᴇʀ:</b> {user.mention}\n"
            f"❌ <b>sᴛᴀᴛᴜs:</b> Aapka kat gaya! ✂️\n"
            f"📝 <b>ᴀᴅᴠɪᴄᴇ:</b> Thoda Mafia Cash kamao, ladki apne aap aayegi.\n"
            f"{line}"
        )

    await status_msg.edit(text)
