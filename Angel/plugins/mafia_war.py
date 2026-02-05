import random
import asyncio
from pyrogram import Client, filters
from motor.motor_asyncio import AsyncIOMotorClient
# Config se details lene ke liye (config.py file honi chahiye)
from config import MONGO_URL, LOG_GROUP_ID 

# --- DATABASE SETUP ---
db_client = AsyncIOMotorClient(MONGO_URL)
db = db_client.MafiaBot # Database Name
users_db = db.users      # Collection Name

line = "✨ ━━━━━━━━━━━━━━━━━━━━ ✨"
owner_tag = "ᴢᴇxx 👑"

# --- HELPER FUNCTIONS ---
async def get_user_data(user_id):
    user = await users_db.find_one({"user_id": user_id})
    if not user:
        new_user = {"user_id": user_id, "health": 100, "wins": 0, "cash": 1000, "level": 1}
        await users_db.insert_one(new_user)
        return new_user
    return user

async def update_user(user_id, update_data):
    await users_db.update_one({"user_id": user_id}, {"$set": update_data})

# --- WEAPONS CONFIG ---
WEAPONS = {
    "🔫 Glock-17": (15, 25), "🔪 Karambit": (10, 20),
    "💣 C4 Explosive": (40, 60), "🥊 Brass Knuckles": (5, 12)
}

# 1. FIGHT COMMAND
@Client.on_message(filters.command("mafia_fight") & filters.group)
async def mafia_fight(client, message):
    if not message.reply_to_message: return await message.reply_text("❌ Shikaar par reply karo!")
    
    attacker_id = message.from_user.id
    victim_id = message.reply_to_message.from_user.id
    if attacker_id == victim_id: return await message.reply_text("😂 Khud se mat lado!")

    a_data = await get_user_data(attacker_id)
    v_data = await get_user_data(victim_id)

    weapon, d_range = random.choice(list(WEAPONS.items()))
    damage = random.randint(*d_range) + (a_data["level"] * 2)
    
    v_data["health"] -= damage
    if v_data["health"] <= 0:
        loot = random.randint(500, 1500)
        a_data["wins"] += 1
        a_data["cash"] += loot
        a_data["level"] += 1
        v_data["health"] = 100
        res = f"<b>💀 {message.reply_to_message.from_user.mention} Finished!</b>\n🏆 <b>Winner:</b> {message.from_user.mention}\n💰 <b>Loot:</b> ₹{loot}\n🆙 <b>Level:</b> {a_data['level']}"
    else:
        res = f"⚔️ <b>{message.from_user.mention} attacked with {weapon}</b>\n💥 <b>Damage:</b> -{damage} HP\n❤️ <b>Victim HP:</b> {v_data['health']}%"
    
    await update_user(attacker_id, a_data)
    await update_user(victim_id, v_data)
    await message.reply_text(f"<b>🔥 #ᴍᴀꜰɪᴀ_ᴡᴀʀ</b>\n{line}\n{res}\n{line}")

# 2. BALANCE CHECK
@Client.on_message(filters.command(["balance", "cash"]))
async def check_balance(client, message):
    data = await get_user_data(message.from_user.id)
    await message.reply_text(
        f"<b>💰 ᴍᴀꜰɪᴀ ᴀᴄᴄᴏᴜɴᴛ: {message.from_user.first_name}</b>\n{line}\n"
        f"💵 ᴄᴀsʜ: <code>₹{data['cash']}</code>\n💀 ᴋɪʟʟs: <code>{data['wins']}</code>\n"
        f"⭐ ʟᴠʟ: <code>{data['level']}</code>\n{line}\nᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>{owner_tag}</b>"
    )

# 3. WITHDRAW SYSTEM
@Client.on_message(filters.command("withdraw") & filters.private)
async def withdraw_money(client, message):
    data = await get_user_data(message.from_user.id)
    try:
        amount = int(message.command[1])
    except: return await message.reply_text("<b>Usage:</b> `/withdraw 5000`")

    if amount < 5000: return await message.reply_text("⚠️ Min withdraw ₹5000 hai!")
    if data["cash"] < amount: return await message.reply_text("❌ Itna paisa nahi hai!")

    data["cash"] -= amount
    await update_user(message.from_user.id, data)
    
    await client.send_message(LOG_GROUP_ID, f"<b>🏧 #ᴡɪᴛʜᴅʀᴀᴡ_ʀᴇǫᴜᴇsᴛ</b>\n{line}\n👤 ᴜsᴇʀ: {message.from_user.mention}\n💰 ᴀᴍᴏᴜɴᴛ: ₹{amount}\n{line}")
    await message.reply_text("✅ Request ZEXX ko bhej di gayi hai!")
