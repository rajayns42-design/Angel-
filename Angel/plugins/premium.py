import time
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID # Aapka ID config.py se

# --- DATABASE (Memory for now, MongoDB recommended) ---
premium_users = {} # {user_id: expiry_timestamp}
line = "━━━━━━━━━━━━━━━━━━━━"
QR_IMAGE = "https://graph.org/file/your-qr-link.jpg" # Apna QR link yahan dalo
UPI_ID = "zexx@upi" # Apna UPI ID

# --- 1. PREMIUM MENU ---
@Client.on_message(filters.command("premium"))
async def premium_menu(client, message):
    text = (
        f"<b>🌟 ᴀɴɢᴇʟ ᴘʀᴇᴍɪᴜᴍ sʏsᴛᴇᴍ 🌟</b>\n"
        f"{line}\n"
        f"💎 <b>ᴘʟᴀɴs ᴀᴠᴀɪʟᴀʙʟᴇ:</b>\n"
        f"🗓️ 1 ᴍᴏɴᴛʜ: ₹99\n"
        f"📅 1 ʏᴇᴀʀ: ₹999\n"
        f"♾️ ʟɪꜰᴇᴛɪᴍᴇ: ₹1499\n\n"
        f"🎁 <b>ʙᴇɴᴇꜰɪᴛs:</b>\n"
        f"✅ No Limit on Rob/Fight\n"
        f"✅ 2x Daily Rewards\n"
        f"✅ Exclusive VIP Badge\n"
        f"{line}\n"
        f"ᴘᴀʏ ᴏɴ ᴜᴘɪ: <code>{UPI_ID}</code>\n"
        f"<i>Payment ke baad Transaction ID bhejein!</i>"
    )
    buttons = InlineKeyboardMarkup([[InlineKeyboardButton("📤 sᴜʙᴍɪᴛ ᴘʀᴏᴏꜰ (ᴛʀɴ ɪᴅ)", callback_data="sub_proof")]])
    await message.reply_photo(photo=QR_IMAGE, caption=text, reply_markup=buttons)

# --- 2. SUBMIT TRANSACTION ID ---
@Client.on_message(filters.command("submit") & filters.private)
async def submit_id(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<b>❌ Trn ID dalo!</b> Example: `/submit TXN12345678` 1 Month")
    
    trn_id = message.text.split(None, 1)[1]
    user = message.from_user
    
    # Admin ko approval message bhejna
    await client.send_message(
        OWNER_ID,
        f"<b>📩 ɴᴇᴡ ᴘʀᴇᴍɪᴜᴍ ʀᴇǫᴜᴇsᴛ</b>\n{line}\n"
        f"👤 <b>ᴜsᴇʀ:</b> {user.mention} (<code>{user.id}</code>)\n"
        f"🆔 <b>ᴛʀɴ ɪᴅ:</b> <code>{trn_id}</code>\n{line}\n"
        f"Approve karne ke liye niche command use karein:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ ᴀᴘᴘʀᴏᴠᴇ", callback_data=f"approve_{user.id}")]
        ])
    )
    await message.reply_text("<b>✅ Request bhej di gayi hai! Admin approve karte hi aapko message mil jayega.</b>")

# --- 3. ADMIN APPROVAL & AUTO-EXPIRY ---
@Client.on_callback_query(filters.regex(r"approve_(\d+)"))
async def approve_user(client, callback_query):
    user_id = int(callback_query.data.split("_")[1])
    
    # Plans Logic (Modify as needed during approval)
    duration = 30 * 24 * 3600 # Default 1 Month
    expiry_time = int(time.time()) + duration
    
    premium_users[user_id] = expiry_time
    
    await client.send_message(user_id, "<b>🎊 Mubarak ho! Aapka Premium Approve ho gaya hai.</b>")
    await callback_query.answer("User Approved!", show_alert=True)
    await callback_query.edit_message_text(f"<b>✅ User {user_id} is now Premium!</b>")

# --- 4. CHECK PREMIUM STATUS (MIDDLEWARE) ---
def is_premium(user_id):
    if user_id in premium_users:
        if int(time.time()) < premium_users[user_id]:
            return True
        else:
            del premium_users[user_id] # Auto Expire
    return False
