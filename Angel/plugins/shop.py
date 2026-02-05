from pyrogram import Client, filters

# --- DATABASE (Memory based for now) ---
user_coins = {} 
line = "✨ ══════════════════ ✨"
owner_tag = "ᴢᴇxx 👑"

# --- SHOP ITEMS (Updated with 2 New Features) ---
items = {
    "1": {"name": "👑 VIP Role", "price": 5000},
    "2": {"name": "🛡️ Protection", "price": 2000},
    "3": {"name": "⚡ Fast Pass", "price": 1000},
    "4": {"name": "🔥 Double Damage", "price": 15000}, # Naya Item
    "5": {"name": "🕵️ Stealth Mode", "price": 10000}   # Naya Item
}

# --- COMMAND: CHECK COINS ---
@Client.on_message(filters.command("wallet") & (filters.group | filters.private))
async def check_wallet(client, message):
    user_id = message.from_user.id
    coins = user_coins.get(user_id, 100) 
    await message.reply_text(f"<b>💰 ʏᴏᴜʀ ᴡᴀʟʟᴇᴛ</b>\n{line}\n👤 <b>ᴜsᴇʀ:</b> {message.from_user.first_name}\n🪙 <b>ᴄᴏɪɴs:</b> <code>{coins}</code>\n{line}\nᴏᴡɴᴇʀ: {owner_tag}")

# --- COMMAND: SHOP MENU ---
@Client.on_message(filters.command("shop") & filters.group)
async def shop_menu(client, message):
    menu = f"<b>🛍️ ᴢᴇxx ᴜɴᴅᴇʀᴡᴏʀʟᴅ sʜᴏᴘ</b>\n{line}\n"
    for id, info in items.items():
        menu += f"<b>{id}. {info['name']}</b> — <code>{info['price']}</code> 🪙\n"
    menu += f"{line}\n<i>ᴜsᴇ `/buy [id]` ᴛᴏ ᴘᴜʀᴄʜᴀsᴇ!</i>\nᴘᴏᴡᴇʀᴇᴅ ʙʏ: {owner_tag}"
    await message.reply_text(menu)

# --- COMMAND: BUY ITEM ---
@Client.on_message(filters.command("buy") & filters.group)
async def buy_item(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<b>❌ ɪᴅ ᴅᴏ!</b> Example: `/buy 1`")
    
    user_id = message.from_user.id
    item_id = message.command[1]
    
    if item_id not in items:
        return await message.reply_text("<b>❌ Invalid Item ID!</b>")
    
    price = items[item_id]['price']
    current_coins = user_coins.get(user_id, 100)
    
    if current_coins < price:
        return await message.reply_text(f"<b>❌ ɢᴀʀᴇᴇʙ!</b> You need <code>{price - current_coins}</code> more coins.")
    
    # Deduct coins
    user_coins[user_id] = current_coins - price
    
    # Final Confirmation Message
    await message.reply_text(
        f"<b>✅ ᴘᴜʀᴄʜᴀsᴇ sᴜᴄᴄᴇss!</b>\n{line}\n"
        f"🎁 <b>ɪᴛᴇᴍ:</b> {items[item_id]['name']}\n"
        f"💰 <b>ʀᴇᴍᴀɪɴɪɴɢ:</b> {user_coins[user_id]} 🪙\n"
        f"{line}\n<i>ᴀɴɢᴇʟ ɪs ʜᴀᴘᴘʏ ᴡɪᴛʜ ʏᴏᴜʀ sʜᴏᴘᴘɪɴɢ! ✨</i>\nʙʏ: {owner_tag}"
    )
