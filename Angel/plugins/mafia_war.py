import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

# --- MAFIA DATABASE (ZEXX UNDERWORLD) ---
stats = {} 
line = "✨ ━━━━━━━━━━━━━━━━━━━━ ✨"
owner_tag = "ᴢᴇxx 👑"

# --- WEAPONS CONFIG ---
WEAPONS = {
    "🔫 Glock-17": (15, 25),
    "🔪 Karambit": (10, 20),
    "💣 C4 Explosive": (40, 60),
    "🏹 Crossbow": (20, 30),
    "🥊 Brass Knuckles": (5, 12)
}

# --- 1. FIGHT COMMAND ---
@Client.on_message(filters.command("mafia_fight") & filters.group)
async def mafia_fight(client, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>❌ Shikaar par reply toh karo!</b>")
    
    attacker = message.from_user
    victim = message.reply_to_message.from_user
    if attacker.id == victim.id: return await message.reply_text("😂 Khud se mat lado!")

    for uid in [attacker.id, victim.id]:
        if uid not in stats: stats[uid] = {"health": 100, "wins": 0, "cash": 1000, "level": 1}

    weapon, d_range = random.choice(list(WEAPONS.items()))
    damage = random.randint(*d_range) + (stats[attacker.id]["level"] * 2)
    
    stats[victim.id]["health"] -= damage
    if stats[victim.id]["health"] <= 0:
        loot = random.randint(500, 1500)
        stats[attacker.id]["wins"] += 1
        stats[attacker.id]["cash"] += loot
        stats[attacker.id]["level"] += 1
        stats[victim.id]["health"] = 100
        res = (f"<b>💀 {victim.mention} Finished!</b>\n"
               f"🏆 <b>Winner:</b> {attacker.mention}\n"
               f"💰 <b>Loot:</b> ₹{loot}\n🆙 <b>Level:</b> {stats[attacker.id]['level']}")
    else:
        res = (f"⚔️ <b>{attacker.mention} attacked with {weapon}</b>\n"
               f"💥 <b>Damage:</b> -{damage} HP\n❤️ <b>Victim HP:</b> {stats[victim.id]['health']}%")
    
    await message.reply_text(f"<b>🔥 #ᴍᴀꜰɪᴀ_ᴡᴀʀ</b>\n{line}\n{res}\n{line}")

# --- 2. ROB COMMAND ---
@Client.on_message(filters.command("rob") & filters.group)
async def mafia_rob(client, message):
    if not message.reply_to_message: return await message.reply_text("❌ Kise lootna hai?")
    
    attacker = message.from_user
    victim = message.reply_to_message.from_user
    
    for uid in [attacker.id, victim.id]:
        if uid not in stats: stats[uid] = {"health": 100, "wins": 0, "cash": 1000, "level": 1}

    if stats[victim.id]["cash"] < 500:
        return await message.reply_text("<b>🤏 Victim bahut gareeb hai!</b>")

    if random.random() < 0.4: # 40% Success
        stolen = int(stats[victim.id]["cash"] * random.uniform(0.1, 0.3))
        stats[victim.id]["cash"] -= stolen
        stats[attacker.id]["cash"] += stolen
        res = f"<b>💰 Looted ₹{stolen} successfully!</b>"
    else:
        stats[attacker.id]["cash"] -= 300
        res = "<b>🚫 Pakde gaye! ₹300 fine bharna pada.</b>"
    
    await message.reply_text(f"<b>🕵️ #ᴍᴀꜰɪᴀ_ʀᴏʙʙᴇʀʏ</b>\n{line}\n👤 <b>Chor:</b> {attacker.mention}\n{res}\n{line}")

# --- 3. ULTIMATE LEADERBOARD ---
@Client.on_message(filters.command("mafia_board") & filters.group)
async def mafia_board(client, message):
    if not stats: return await message.reply_text("❌ Underworld khali hai!")
    
    sorted_stats = sorted(stats.items(), key=lambda x: x[1]['wins'], reverse=True)[:10]
    board = f"<b>🏆 ᴍᴀꜰɪᴀ ᴜɴᴅᴇʀᴡᴏʀʟᴅ: ᴛᴏᴘ ᴅᴏɴs</b>\n{line}\n\n"

    for i, (uid, data) in enumerate(sorted_stats, 1):
        try:
            u = await client.get_users(uid)
            name = u.first_name
        except: name = "Unknown"
        
        medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
        board += (f"{medal} <b>{name}</b>\n"
                  f"   💀 ᴋɪʟʟs: <code>{data['wins']}</code> | 💰 ᴄᴀsʜ: <code>₹{data['cash']}</code>\n"
                  f"   ⭐ ʟᴠʟ: <code>{data['level']}</code>\n"
                  f"────────────────────\n")

    board += f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>{owner_tag}</b>"
    await message.reply_text(board)
