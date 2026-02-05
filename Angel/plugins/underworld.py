import random
from pyrogram import Client, filters
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

db = AsyncIOMotorClient(MONGO_URL).MafiaBot.users
line = "✨ ━━━━━━━━━━━━━━━━━━━━ ✨"

# --- 1. SET SUPARI (BOUNTY) ---
@Client.on_message(filters.command(["supari", "bounty"]) & filters.group)
async def set_supari(client, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>❌ Kiske sar par supari rakhni hai? Reply karo!</b>")
    
    if len(message.command) < 2:
        return await message.reply_text("<b>Usage:</b> `/supari 10000`")

    try:
        amount = int(message.command[1])
    except: return await message.reply_text("<b>❌ Amount sahi dalo!</b>")

    attacker_id = message.from_user.id
    victim_id = message.reply_to_message.from_user.id

    a_data = await db.find_one({"user_id": attacker_id})
    if not a_data or a_data["cash"] < amount:
        return await message.reply_text("<b>❌ Itni supari dene ki aukaat nahi hai!</b>")

    # Supari database mein save karna
    await db.update_one({"user_id": victim_id}, {"$inc": {"bounty": amount}})
    await db.update_one({"user_id": attacker_id}, {"$inc": {"cash": -amount}})

    await message.reply_text(
        f"<b>💀 #sᴜᴘᴀʀɪ_ᴀɴɴᴏᴜɴᴄᴇᴅ</b>\n"
        f"{line}\n"
        f"🎯 <b>Target:</b> {message.reply_to_message.from_user.mention}\n"
        f"💰 <b>Inaam:</b> ₹{amount}\n"
        f"👤 <b>By:</b> Secret Don\n"
        f"{line}\n"
        f"<i>Jo isey marega, inaam usika!</i>"
    )

# --- 2. BLACK MARKET (SHOP) ---
@Client.on_message(filters.command(["shop", "blackmarket"]) & filters.group)
async def black_market(client, message):
    text = (
        f"<b>🖤 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʙʟᴀᴄᴋ ᴍᴀʀᴋᴇᴛ 🖤</b>\n"
        f"{line}\n"
        f"1️⃣ <b>ᴅᴏᴜʙʟᴇ ᴅᴀᴍᴀɢᴇ (2ʜ)</b> - ₹20,000\n"
        f"   ➥ Command: `/buy 1` \n\n"
        f"2️⃣ <b>ʟᴜᴄᴋʏ ᴄʜᴀʀᴍ (ʀᴏʙ ᴄʜᴀɴᴄᴇ ↑)</b> - ₹15,000\n"
        f"   ➥ Command: `/buy 2` \n\n"
        f"3️⃣ <b>ꜰᴀᴋᴇ ɪᴅ (ʜɪᴅᴇ ꜰʀᴏᴍ ʙᴏᴀʀᴅ)</b> - ₹50,000\n"
        f"   ➥ Command: `/buy 3` \n"
        f"{line}\n"
        f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>ᴢᴇxx 👑</b>"
    )
    await message.reply_text(text)
