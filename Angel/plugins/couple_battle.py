import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- CONFIG ---
line = "⚔️ ━━━━━━━━━━━━━━━━ ⚔️"

@Client.on_message(filters.command(["multibattle", "mbattle"]) & filters.group)
async def multi_couple_battle(client, message):
    # --- FAST FIX: Fetching Active Members ---
    all_members = []
    async for m in client.get_chat_members(message.chat.id, limit=150):
        if not m.user.is_bot and not m.user.is_deleted:
            all_members.append(m.user.first_name)
    
    # --- FAST FIX: Minimum Members Check ---
    if len(all_members) < 6:
        return await message.reply_text("<b>⚠️ ᴇʀʀᴏʀ:</b> Multi-Battle ke liye kam se kam 6 log chahiye!")

    # Shuffling for randomness
    random.shuffle(all_members)

    # Creating 3 Random Couples
    c1 = f"{all_members[0]} + {all_members[1]}"
    c2 = f"{all_members[2]} + {all_members[3]}"
    c3 = f"{all_members[4]} + {all_members[5]}"

    start_text = (
        f"<b>🔥 ᴍᴜʟᴛɪ-ᴄᴏᴜᴘʟᴇ ʙᴀᴛᴛʟᴇ 🔥</b>\n"
        f"{line}\n"
        f"➊ <b>ᴛᴇᴀᴍ ʀᴇᴅ:</b> {c1}\n"
        f"➋ <b>ᴛᴇᴀᴍ ʙʟᴜᴇ:</b> {c2}\n"
        f"➌ <b>ᴛᴇᴀᴍ ɢᴏʟᴅ:</b> {c3}\n"
        f"{line}\n"
        f"<i>ᴀɴɢᴇʟ ɪs ᴄᴀʟᴄᴜʟᴀᴛɪɴɢ ᴛʜᴇ ʙᴇsᴛ ᴊᴏᴅɪ... ⚡</i>"
    )

    battle_msg = await message.reply_text(start_text)
    await asyncio.sleep(3) # Speed Fix: Dramatic delay

    # Score Calculation
    scores = {
        "ᴛᴇᴀᴍ ʀᴇᴅ": random.randint(40, 99),
        "ᴛᴇᴀᴍ ʙʟᴜᴇ": random.randint(40, 99),
        "ᴛᴇᴀᴍ ɢᴏʟᴅ": random.randint(40, 99)
    }

    # Sorting to find winner
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    winner_name, winner_score = sorted_scores[0]
    
    # Winner names mapping
    couples = {"ᴛᴇᴀᴍ ʀᴇᴅ": c1, "ᴛᴇᴀᴍ ʙʟᴜᴇ": c2, "ᴛᴇᴀᴍ ɢᴏʟᴅ": c3}
    winner_couple = couples[winner_name]

    result_text = (
        f"<b>🏆 ʙᴀᴛᴛʟᴇ ᴄʜᴀᴍᴘɪᴏɴs 🏆</b>\n"
        f"{line}\n"
        f"🥇 <b>{winner_name}:</b> {winner_couple}\n"
        f"📊 <b>sᴄᴏʀᴇ:</b> <code>{winner_score}%</code>\n"
        f"{line}\n"
        f"🥈 <b>𝟸ɴᴅ:</b> {sorted_scores[1][0]} (<code>{sorted_scores[1][1]}%</code>)\n"
        f"🥉 <b>𝟹ʀᴅ:</b> {sorted_scores[2][0]} (<code>{sorted_scores[2][1]}%</code>)\n"
        f"{line}\n"
        f"📝 <b>ᴠᴇʀᴅɪᴄᴛ:</b> <i>{winner_couple} ne baaki sabki chutti kar di! 👑</i>\n"
        f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>ᴢᴇxx</b>"
    )

    await battle_msg.edit(result_text)

# --- BONUS: QUICK SHIP (Fastest Fix for 2 users) ---
@Client.on_message(filters.command("ship") & filters.group)
async def quick_ship(client, message):
    try:
        members = []
        async for m in client.get_chat_members(message.chat.id, limit=50):
            if not m.user.is_bot: members.append(m.user.first_name)
        
        c = random.sample(members, 2)
        await message.reply_text(f"<b>💞 ɴᴇᴡ sʜɪᴘ ꜰᴏᴜɴᴅ!</b>\n{line}\n🚢 <b>ᴄᴏᴜᴘʟᴇ:</b> {c[0]} + {c[1]}\n📊 <b>ᴄʜᴀɴᴄᴇs:</b> {random.randint(10, 100)}%\n{line}")
    except Exception as e:
        await message.reply_text("<b>❌ Error:</b> Members load nahi ho paye!")
