import random
import asyncio
from pyrogram import Client, filters

# --- DATABASE (Temporary) ---
stats = {} # {user_id: {"health": 100, "wins": 0}}
line = "⚔️ ━━━━━━━━━━━━━━━━━━━━ ⚔️"

# --- WEAPONS & DAMAGE ---
WEAPONS = {
    "🔫 Pistol": (10, 20),
    "🔪 Knife": (5, 15),
    "💣 Bomb": (30, 50),
    "🥊 Punch": (2, 8)
}

@Client.on_message(filters.command("mafia_fight") & filters.group)
async def start_war(client, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>❌ Arre Mafia! Kispe attack karna hai? Reply toh karo!</b>")
    
    attacker = message.from_user
    victim = message.reply_to_message.from_user
    
    if attacker.id == victim.id:
        return await message.reply_text("<b>😂 Apne aap ko goli maaroge kya?</b>")

    # Initializing Health
    for user_id in [attacker.id, victim.id]:
        if user_id not in stats:
            stats[user_id] = {"health": 100, "wins": 0}

    # Fight Logic
    weapon_name, damage_range = random.choice(list(WEAPONS.items()))
    damage = random.randint(*damage_range)
    
    stats[victim.id]["health"] -= damage
    if stats[victim.id]["health"] < 0: stats[victim.id]["health"] = 0
    
    current_health = stats[victim.id]["health"]
    
    # Stylish Fight UI
    text = (
        f"<b>🔥 #ᴍᴀꜰɪᴀ_ᴡᴀʀ_ɪɴ_ᴘʀᴏɢʀᴇss</b>\n"
        f"{line}\n"
        f"👤 <b>ᴀᴛᴛᴀᴄᴋᴇʀ:</b> {attacker.mention}\n"
        f"🎯 <b>ᴠɪᴄᴛɪᴍ:</b> {victim.mention}\n\n"
        f"⚔️ <b>ᴡᴇᴀᴘᴏɴ:</b> {weapon_name}\n"
        f"💥 <b>ᴅᴀᴍᴀɢᴇ:</b> -{damage} HP\n"
        f"❤️ <b>ᴠɪᴄᴛɪᴍ ʜᴇᴀʟᴛʜ:</b> {current_health}%\n"
        f"{line}\n"
    )

    if current_health <= 0:
        stats[victim.id]["health"] = 100 # Reset health for next time
        stats[attacker.id]["wins"] += 1
        text += f"<b>💀 {victim.first_name} ɪs ᴋɪʟʟᴇᴅ!</b>\n👑 <b>ᴡɪɴɴᴇʀ:</b> {attacker.mention}"
    else:
        text += f"<b>😈 {victim.first_name} abhi zinda hai, badla lo!</b>"

    await message.reply_text(text)

# --- CHECK MAFIA STATS ---
@Client.on_message(filters.command("mafia_stats") & filters.group)
async def mafia_rank(client, message):
    user_id = message.from_user.id
    if user_id not in stats:
        return await message.reply_text("<b>Abhi tak koi jung nahi ladi aapne!</b>")
    
    u_stats = stats[user_id]
    await message.reply_text(
        f"<b>🎖️ ᴍᴀꜰɪᴀ ʀᴇᴄᴏʀᴅ: {message.from_user.first_name}</b>\n"
        f"{line}\n"
        f"❤️ <b>ᴄᴜʀʀᴇɴᴛ ʜᴇᴀʟᴛʜ:</b> {u_stats['health']}%\n"
        f"🏆 <b>ᴛᴏᴛᴀʟ ᴋɪʟʟs:</b> {u_stats['wins']}\n"
        f"👑 <b>ᴏᴡɴᴇʀ:</b> ᴢᴇxx\n"
        f"{line}"
    )
