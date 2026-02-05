import random
import asyncio
from pyrogram import Client, filters
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

# Database Setup
db = AsyncIOMotorClient(MONGO_URL).MafiaBot.users
line = "━━━━━━━━━━━━━━━━━━━━"

@Client.on_message(filters.command(["bet", "casino", "jua"]) & filters.group)
async def underworld_casino(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    # Check input
    if len(message.command) < 2:
        return await message.reply_text("<b>⚠️ Use:</b> `/bet 500` (Reply to play)")

    try:
        amount = int(message.command[1])
    except:
        return await message.reply_text("<b>❌ Amount number mein dalo!</b>")

    if amount < 100:
        return await message.reply_text("<b>🤏 Minimum bet ₹100 hai!</b>")

    # User ka paisa check karna
    user_data = await db.find_one({"user_id": user_id})
    if not user_data or user_data["cash"] < amount:
        return await message.reply_text("<b>❌ Itna paisa nahi hai! Pehle robbery karo.</b>")

    # Casino Animation
    m = await message.reply_text(f"🎰 <b>{user_name}</b> ne ₹{amount} ki baazi lagayi hai...\n🎲 Dice ghoom raha hai...")
    await asyncio.sleep(2)

    # Logic: Dice 4, 5, 6 = WIN | 1, 2, 3 = LOSS
    dice_roll = random.randint(1, 6)
    
    if dice_roll >= 4:
        win_money = amount * 2
        await db.update_one({"user_id": user_id}, {"$inc": {"cash": amount}}) # Net profit = amount
        res_text = (
            f"<b>🎉 JACKPOT!!! 🎉</b>\n"
            f"{line}\n"
            f"🎲 ᴅɪᴄᴇ sᴄᴏʀᴇ: <code>{dice_roll}</code>\n"
            f"💰 ᴡɪɴ ᴀᴍᴏᴜɴᴛ: ₹{win_money}\n"
            f"✅ Account mein credit ho gaya!\n"
            f"{line}\n"
            f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>ᴢᴇxx 👑</b>"
        )
    else:
        await db.update_one({"user_id": user_id}, {"$inc": {"cash": -amount}})
        res_text = (
            f"<b>💀 LOSS... B बर्बादी 💀</b>\n"
            f"{line}\n"
            f"🎲 ᴅɪᴄᴇ sᴄᴏʀᴇ: <code>{dice_roll}</code>\n"
            f"💸 ʟᴏss ᴀᴍᴏᴜɴᴛ: ₹{amount}\n"
            f"📝 ᴛɪᴘ: Agli baar kismat chamkegi!\n"
            f"{line}"
        )

    await m.edit(res_text)
