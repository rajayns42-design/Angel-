import time
from pyrogram import Client, filters
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

db = AsyncIOMotorClient(MONGO_URL).MafiaBot.users
line = "━━━━━━━━━━━━━━━━━━━━"

# --- 1. DEPOSIT MONEY ---
@Client.on_message(filters.command(["deposit", "d"]) & filters.group)
async def deposit_money(client, message):
    user_id = message.from_user.id
    if len(message.command) < 2:
        return await message.reply_text("<b>Usage:</b> `/deposit 5000`")

    try:
        amount = int(message.command[1])
    except: return await message.reply_text("<b>❌ Amount number mein dalo!</b>")

    user_data = await db.find_one({"user_id": user_id})
    if not user_data or user_data["cash"] < amount:
        return await message.reply_text("<b>❌ Itna paisa pocket mein nahi hai!</b>")

    # Bank mein paisa dalna aur timer set karna
    await db.update_one(
        {"user_id": user_id},
        {
            "$inc": {"cash": -amount, "bank": amount},
            "$set": {"last_interest_time": int(time.time())}
        }
    )

    await message.reply_text(
        f"<b>🏦 #ᴍᴀꜰɪᴀ_ʙᴀɴᴋ_ᴅᴇᴘᴏsɪᴛ</b>\n"
        f"{line}\n"
        f"💰 ᴀᴍᴏᴜɴᴛ: ₹{amount}\n"
        f"🔒 sᴛᴀᴛᴜs: Secure from Robbers\n"
        f"{line}\n"
        f"<i>Ab is par aapko 5% munafa milega!</i>"
    )

# --- 2. WITHDRAW FROM BANK ---
@Client.on_message(filters.command(["wdraw", "withdraw_bank"]) & filters.group)
async def withdraw_bank(client, message):
    user_id = message.from_user.id
    if len(message.command) < 2:
        return await message.reply_text("<b>Usage:</b> `/wdraw 5000`")

    try:
        amount = int(message.command[1])
    except: return await message.reply_text("<b>❌ Amount number mein dalo!</b>")

    user_data = await db.find_one({"user_id": user_id})
    bank_balance = user_data.get("bank", 0)

    if bank_balance < amount:
        return await message.reply_text("<b>❌ Bank mein itna paisa nahi hai!</b>")

    await db.update_one(
        {"user_id": user_id},
        {"$inc": {"cash": amount, "bank": -amount}}
    )
    await message.reply_text(f"<b>✅ Bank se ₹{amount} nikal liye gaye!</b>")

# --- 3. CLAIM INTEREST (DAILY REWARD) ---
@Client.on_message(filters.command(["claim", "interest"]) & filters.group)
async def claim_interest(client, message):
    user_id = message.from_user.id
    user_data = await db.find_one({"user_id": user_id})
    
    bank_bal = user_data.get("bank", 0)
    if bank_bal <= 0:
        return await message.reply_text("<b>❌ Bank khali hai, interest kahan se milega?</b>")

    last_time = user_data.get("last_interest_time", 0)
    current_time = int(time.time())

    # 24 Hours = 86400 Seconds
    if current_time - last_time < 86400:
        remaining = (86400 - (current_time - last_time)) // 3600
        return await message.reply_text(f"<b>⏳ Sabar karo! {remaining} ghante baad aana.</b>")

    interest = int(bank_bal * 0.05) # 5% Interest
    await db.update_one(
        {"user_id": user_id},
        {
            "$inc": {"bank": interest},
            "$set": {"last_interest_time": current_time}
        }
    )

    await message.reply_text(
        f"<b>📈 #ɪɴᴛᴇʀᴇsᴛ_ᴄʟᴀɪᴍᴇᴅ</b>\n"
        f"{line}\n"
        f"💰 ᴘʀᴏꜰɪᴛ: ₹{interest}\n"
        f"🏦 ɴᴇᴡ ʙᴀɴᴋ ʙᴀʟ: ₹{bank_bal + interest}\n"
        f"{line}\n"
        f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>ᴢᴇxx 👑</b>"
    )
