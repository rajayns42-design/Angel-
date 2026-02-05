from pyrogram import Client, filters
import random

# --- DATABASE (Fast Dictionary) ---
# Tip: Global level par user_coins pehle se define hai plugins mein
user_coins = {} 
line = "✨ ══════════════════ ✨"

# --- 1. CHECK BALANCE (Bal) ---
@Client.on_message(filters.command(["bal", "balance", "coins"]) & (filters.group | filters.private))
async def get_balance(client, message):
    user_id = message.from_user.id
    coins = user_coins.get(user_id, 500) # Naye user ko free 500 coins
    
    await message.reply_text(
        f"<b>💰 ʏᴏᴜʀ ᴡᴀʟʟᴇᴛ</b>\n"
        f"{line}\n"
        f"👤 <b>ᴜsᴇʀ:</b> {message.from_user.first_name}\n"
        f"🪙 <b>ᴄᴏɪɴs:</b> <code>{coins}</code>\n"
        f"{line}\n"
        f"<i>ᴋᴇᴇᴘ ᴇᴀʀɴɪɴɢ, ᴋᴇᴇᴘ ɢᴀᴍɪɴɢ! 🚀</i>"
    )

# --- 2. DAILY REWARD (Fast Coins) ---
@Client.on_message(filters.command("daily") & (filters.group | filters.private))
async def daily_reward(client, message):
    user_id = message.from_user.id
    # Random reward 100 se 500 ke beech
    reward = random.randint(100, 500)
    
    current_bal = user_coins.get(user_id, 500)
    user_coins[user_id] = current_bal + reward
    
    await message.reply_text(
        f"<b>🎁 ᴅᴀɪʟʏ ʙᴏɴᴜs</b>\n"
        f"{line}\n"
        f"🎉 ᴄᴏɴɢʀᴀᴛs <b>{message.from_user.first_name}</b>!\n"
        f"Aapne aaj <code>{reward}</code> coins claim kiye.\n"
        f"💰 ɴᴇᴡ ʙᴀʟᴀɴᴄᴇ: <code>{user_coins[user_id]}</code>\n"
        f"{line}\n"
        f"<i>Kal phir aana! 😉</i>"
    )

# --- 3. PAY/GIVE COINS (Transfer) ---
@Client.on_message(filters.command("pay") & filters.group)
async def pay_coins(client, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>❌ Error:</b> Kise paise bhejne hain? Reply karo!")
    
    try:
        amount = int(message.command[1])
    except:
        return await message.reply_text("<b>❌ Amount batao!</b>\nUsage: `/pay 100`")

    sender_id = message.from_user.id
    receiver_id = message.reply_to_message.from_user.id
    
    if user_coins.get(sender_id, 500) < amount:
        return await message.reply_text("<b>⚠️ Gareeb!</b> Itne coins nahi hain tumhare paas.")

    # Transaction
    user_coins[sender_id] = user_coins.get(sender_id, 500) - amount
    user_coins[receiver_id] = user_coins.get(receiver_id, 500) + amount
    
    await message.reply_text(
        f"<b>💸 sᴜᴄᴄᴇssꜰᴜʟ ᴛʀᴀɴsꜰᴇʀ</b>\n"
        f"{line}\n"
        f"✅ <code>{amount}</code> coins bheje gaye <b>{message.reply_to_message.from_user.first_name}</b> ko!\n"
        f"{line}"
    )
