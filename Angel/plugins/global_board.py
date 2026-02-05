from pyrogram import Client, filters
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

# --- DATABASE SETUP ---
db_client = AsyncIOMotorClient(MONGO_URL)
db = db_client.MafiaBot
users_db = db.users

line = "━━━━━━━━━━━━━━━━━━━━"
owner_tag = "ᴢᴇxx 👑"

@Client.on_message(filters.command(["gboard", "globalboard"]))
async def global_leaderboard(client, message):
    # Sabse pehle bot ek "Processing" message dikhayega
    status_msg = await message.reply_text("🔍 ᴀɴᴀʟʏᴢɪɴɢ ᴜɴᴅᴇʀᴡᴏʀʟᴅ ᴅᴀᴛᴀ...")

    # MongoDB se Top 10 users nikalna (Kills/Wins ke basis par)
    cursor = users_db.find().sort("wins", -1).limit(10)
    top_users = await cursor.to_list(length=10)

    if not top_users:
        return await status_msg.edit("<b>❌ ᴀʙʜɪ ᴛᴀᴋ ᴋᴏɪ ᴅᴀᴛᴀ ɴᴀʜɪ ᴍɪʟᴀ!</b>")

    board_text = f"<b>🌍 ɢʟᴏʙᴀʟ ᴍᴀꜰɪᴀ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ</b>\n{line}\n\n"

    for i, user_data in enumerate(top_users, start=1):
        user_id = user_data["user_id"]
        kills = user_data.get("wins", 0)
        cash = user_data.get("cash", 0)
        level = user_data.get("level", 1)

        # User ka naam nikalne ki koshish
        try:
            user = await client.get_users(user_id)
            name = user.first_name
        except:
            name = f"Unknown Don [{user_id}]"

        # Rank design
        if i == 1: rank = "🥇"
        elif i == 2: rank = "🥈"
        elif i == 3: rank = "🥉"
        else: rank = f"<b>{i}.</b>"

        board_text += (
            f"{rank} <b>{name}</b>\n"
            f"   💀 ᴋɪʟʟs: <code>{kills}</code>\n"
            f"   💰 ᴄᴀsʜ: <code>₹{cash}</code>\n"
            f"   ⭐ ʀᴀɴᴋ ʟᴇᴠᴇʟ: <code>{level}</code>\n"
            f"────────────────────\n"
        )

    board_text += f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>{owner_tag}</b>"
    
    await status_msg.edit(board_text)
