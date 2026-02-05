import time
from pyrogram import Client, filters
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

db = AsyncIOMotorClient(MONGO_URL).MafiaBot.users
line = "✨ ━━━━━━━━━━━━━━━━━━━━ ✨"

# --- 1. HIRE BODYGUARD ---
@Client.on_message(filters.command(["hire", "bodyguard"]) & filters.group)
async def hire_guard(client, message):
    user_id = message.from_user.id
    cost = 15000  # 24 ghante ki fees
    
    user_data = await db.find_one({"user_id": user_id})
    if not user_data or user_data["cash"] < cost:
        return await message.reply_text(f"<b>❌ Bodyguard sasta nahi aata! ₹{cost} lekar aao.</b>")

    # Expiry time: Abhi se 24 ghante baad
    expiry = int(time.time()) + (24 * 3600)
    
    await db.update_one(
        {"user_id": user_id}, 
        {"$set": {"guard_expiry": expiry}, "$inc": {"cash": -cost}}
    )

    await message.reply_text(
        f"<b>🛡️ #ʙᴏᴅʏɢᴜᴀʀᴅ_ʜɪʀᴇᴅ</b>\n"
        f"{line}\n"
        f"👤 <b>Boss:</b> {message.from_user.mention}\n"
        f"💂‍♂️ <b>Status:</b> Protected for 24 Hours\n"
        f"💰 <b>Fees:</b> ₹{cost} Paid\n"
        f"{line}\n"
        f"<i>Ab koi aapka baal bhi bika nahi kar sakta!</i>"
    )

# --- 2. PROTECTION LOGIC (Middleware) ---
# Ye function baaki plugins (Fight/Rob) use karenge
async def is_protected(user_id):
    user = await db.find_one({"user_id": user_id})
    if user and "guard_expiry" in user:
        if int(time.time()) < user["guard_expiry"]:
            return True
    return False
