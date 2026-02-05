import random
import asyncio
from pyrogram import Client, filters

# --- DECORATION ---
line = "✨ ══════════════════ ✨"

# 1. --- FASTEST FINGER FIRST (Type the word) ---
@Client.on_message(filters.command("fast") & filters.group)
async def fast_type(client, message):
    words = ["ANGEL", "ZEXX", "PYTHON", "CHAMPION", "FASTEST", "KING", "MASTER", "OP"]
    target_word = random.choice(words)
    
    msg = await message.reply_text(f"<b>🚀 ꜰᴀsᴛᴇsᴛ ꜰɪɴɢᴇʀ ꜰɪʀsᴛ</b>\n{line}\nSabse pehle likho: <code>{target_word}</code>\n{line}")
    
    try:
        ans = await client.wait_for_message(message.chat.id, timeout=20)
        if ans.text.upper() == target_word:
            await ans.reply_text(f"<b>🏆 ᴡɪɴɴᴇʀ:</b> {ans.from_user.first_name}\n<i>Speed ekdum aag hai! 🔥</i>")
    except:
        await msg.edit("<b>⏰ ᴛɪᴍᴇ ᴏᴜᴛ!</b>\nKoi bhi fast nahi tha. 🤷‍♂️")

# 2. --- NUMBER GUESSING (1-10) ---
@Client.on_message(filters.command("guess") & filters.group)
async def guess_game(client, message):
    secret = random.randint(1, 10)
    await message.reply_text(f"<b>🤔 ɢᴜᴇss ᴛʜᴇ ɴᴜᴍʙᴇʀ</b>\n{line}\nMaine 1 se 10 ke beech ek number socha hai. Guess karo!\n{line}")
    
    try:
        ans = await client.wait_for_message(message.chat.id, timeout=30)
        if ans.text.isdigit() and int(ans.text) == secret:
            await ans.reply_text(f"<b>🎉 Sahi Pakda!</b>\nNumber tha: <code>{secret}</code>\nWinner: {ans.from_user.first_name}")
        else:
            await message.reply_text(f"<b>❌ Galat!</b> Number tha: <code>{secret}</code>")
    except:
        await message.reply_text(f"<b>⏰ Time Up!</b> Answer tha: <code>{secret}</code>")

# 3. --- SLOT MACHINE (Casino Style) ---
@Client.on_message(filters.command("slot") & filters.group)
async def slot_machine(client, message):
    # Telegram's animated slot machine
    slot_msg = await client.send_dice(message.chat.id, emoji="🎰")
    val = slot_msg.dice.value
    
    # 1, 22, 43, 64 are winning values in Telegram slots
    winners = [1, 22, 43, 64]
    await asyncio.sleep(4)
    
    if val in winners:
        await message.reply_text(f"<b>🎰 ᴊᴀᴄᴋᴘᴏᴛ!</b>\n{line}\n{message.from_user.first_name} ne kismat chamka di! 💰")
    else:
        await message.reply_text(f"<b>🎰 ɴᴏ ʟᴜᴄᴋ!</b>\n{line}\nTry again, {message.from_user.first_name}!")

# 4. --- TRUTH OR DARE (Instant) ---
@Client.on_message(filters.command(["truth", "dare"]) & filters.group)
async def t_or_d(client, message):
    cmd = message.command[0].lower()
    truths = ["Tera sabse bada secret kya hai?", "Bot owner ZEXX kaisa lagta hai?", "Last time kab roye the?"]
    dares = ["Apni crush ka naam likho group mein!", "Apni DP 5 min ke liye change karo.", "Owner ko 'I Love You' bolo!"]
    
    res = random.choice(truths if cmd == "truth" else dares)
    await message.reply_text(f"<b>🔥 {cmd.upper()} ᴛɪᴍᴇ</b>\n{line}\n<b>ᴛᴀsᴋ:</b> {res}\n{line}")
