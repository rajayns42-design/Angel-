from pyrogram import Client, filters

# --- DATABASE (Using dictionary for speed as per your style) ---
user_coins = {} # Paisa
active_bounties = {} # Kispar kitni supari hai
line = "💀 ══════════════════ 💀"
owner_tag = "ᴢᴇxx 👑"

# --- 1. COMMAND: SET SUPARI (BOUNTY) ---
@Client.on_message(filters.command(["supari", "bounty"]) & filters.group)
async def set_bounty(client, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>❌ Kiske sar par supari rakhni hai? Reply karo!</b>")
    
    if len(message.command) < 2:
        return await message.reply_text("<b>Usage:</b> `/supari 5000` (Reply to victim)")

    try:
        amount = int(message.command[1])
    except:
        return await message.reply_text("<b>❌ Amount sahi se likho!</b>")

    attacker_id = message.from_user.id
    victim_id = message.reply_to_message.from_user.id
    victim_name = message.reply_to_message.from_user.first_name

    # Check if attacker has enough money
    if user_coins.get(attacker_id, 100) < amount:
        return await message.reply_text("<b>❌ Itni supari dene ki aukaat nahi hai! Coins kamao pehle.</b>")

    # Deduct money and add to bounty
    user_coins[attacker_id] -= amount
    active_bounties[victim_id] = active_bounties.get(victim_id, 0) + amount

    await message.reply_text(
        f"<b>📢 #sᴜᴘᴀʀɪ_ᴀɴɴᴏᴜɴᴄᴇᴅ</b>\n"
        f"{line}\n"
        f"🎯 <b>ᴛᴀʀɢᴇᴛ:</b> {message.reply_to_message.from_user.mention}\n"
        f"💰 <b>ɪɴᴀᴀᴍ:</b> <code>{active_bounties[victim_id]}</code> 🪙\n"
        f"👤 <b>ʙʏ:</b> Secret Don\n"
        f"{line}\n"
        f"<i>Jo bhi is victim ko harayega, use ye saara paisa milega!</i>\n"
        f"ʙʏ: {owner_tag}"
    )

# --- 2. COMMAND: CHECK ACTIVE BOUNTIES ---
@Client.on_message(filters.command("bounties") & filters.group)
async def list_bounties(client, message):
    if not active_bounties:
        return await message.reply_text("<b>🕊️ Shanti hai... Abhi kisi par supari nahi hai.</b>")
    
    text = f"<b>📝 ᴀᴄᴛɪᴠᴇ sᴜᴘᴀʀɪ ʟɪsᴛ</b>\n{line}\n"
    for v_id, amt in active_bounties.items():
        if amt > 0:
            text += f"👤 <code>{v_id}</code> — <code>{amt}</code> 🪙\n"
    
    text += f"{line}\n<i>Hunting mode: ON! 🔫</i>"
    await message.reply_text(text)
