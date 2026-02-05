import random
from pyrogram import Client, filters

# --- DATABASE (Temporary) ---
user_coins = {}
line = "✨ ══════════════════ ✨"
currency = "💎"

# --- DAILY COMMAND ---
@Client.on_message(filters.command("daily"))
async def daily_coins(client, message):
    user_id = message.from_user.id
    if user_id in user_coins and user_coins[user_id] > 5000: # Logic for limit
        return await message.reply_text(
            f"<b>⚠️ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ!</b>\n"
            f"{line}\n"
            f"ᴀᴀᴘ ᴀᴀᴊ ᴋᴀ ʀᴇᴡᴀʀᴅ ʟᴇ ᴄʜᴜᴋᴇ ʜᴀɪɴ.\n"
            f"ᴋᴀʟ ᴡᴀᴘᴀs ᴀᴀɪʏᴇ ɴᴀʏᴇ ᴛᴏᴋᴇɴs ᴋᴇ ʟɪʏᴇ!"
        )
    
    amount = random.randint(1000, 5000)
    user_coins[user_id] = user_coins.get(user_id, 0) + amount
    
    await message.reply_text(
        f"<b>🎁 ᴅᴀɪʟʏ ʙᴏɴᴜs ᴄʟᴀɪᴍᴇᴅ!</b>\n"
        f"{line}\n"
        f"<b>👤 ᴜsᴇʀ:</b> <code>{message.from_user.first_name}</code>\n"
        f"<b>💰 ᴀᴍᴏᴜɴᴛ:</b> <code>{amount} {currency}</code>\n"
        f"<b>🏦 sᴛᴀᴛᴜs:</b> ᴀᴅᴅᴇᴅ ᴛᴏ ᴡᴀʟʟᴇᴛ\n"
        f"{line}\n"
        f"<i>ᴋᴇᴇᴘ ᴘʟᴀʏɪɴɢ ᴛᴏ ᴇᴀʀɴ ᴍᴏʀᴇ!</i>"
    )

# --- BALANCE COMMAND ---
@Client.on_message(filters.command(["balance", "bal", "wallet"]))
async def check_balance(client, message):
    user_id = message.from_user.id
    balance = user_coins.get(user_id, 0)
    
    await message.reply_text(
        f"<b>🏦 ᴀɴɢᴇʟ ᴄᴇɴᴛʀᴀʟ ʙᴀɴᴋ</b>\n"
        f"{line}\n"
        f"<b>👤 ᴀᴄᴄᴏᴜɴᴛ:</b> <code>{message.from_user.first_name}</code>\n"
        f"<b>💎 ʙᴀʟᴀɴᴄᴇ:</b> <code>{balance} {currency}</code>\n"
        f"<b>🏆 sᴛᴀᴛᴜs:</b> ᴠɪᴘ ᴍᴇᴍʙᴇʀ\n"
        f"{line}"
    )

# --- GAMBLE COMMAND ---
@Client.on_message(filters.command("bet"))
async def bet_coins(client, message):
    user_id = message.from_user.id
    current_bal = user_coins.get(user_id, 0)
    
    if current_bal < 500:
        return await message.reply_text("<b>❌ ɪɴsᴜғғɪᴄɪᴇɴᴛ ғᴜɴᴅs!</b>\nʙᴇᴛ ʟᴀɢᴀɴᴇ ᴋᴇ ʟɪʏᴇ 𝟻𝟶𝟶 ᴅɪᴀᴍᴏɴᴅs ᴄʜᴀʜɪʏᴇ.")
    
    win = random.choice([True, False])
    amount = 500
    
    if win:
        user_coins[user_id] += amount
        status = f"<b>🎉 ʏᴏᴜ ᴡᴏɴ!</b>\n<b>📈 ᴘʀᴏғɪᴛ:</b> <code>+{amount}</code>"
    else:
        user_coins[user_id] -= amount
        status = f"<b>💔 ʏᴏᴜ ʟᴏsᴛ!</b>\n<b>📉 ʟᴏss:</b> <code>-{amount}</code>"
        
    await message.reply_text(
        f"<b>🎰 ʟᴜᴄᴋʏ ᴅɪᴄᴇ ʀᴏʟʟ</b>\n"
        f"{line}\n"
        f"{status}\n"
        f"<b>💰 ɴᴇᴡ ʙᴀʟᴀɴᴄᴇ:</b> <code>{user_coins[user_id]} {currency}</code>\n"
        f"{line}"
    )
