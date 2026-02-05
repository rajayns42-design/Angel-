import random
import asyncio
import requests
from pyrogram import Client, filters

# --- CONFIG ---
line = "✨ ━━━━━━━━━━━━━━━━ ✨"
TRUTH_DARE_API = "https://api.truthordarebot.xyz/v1/"
QUIZ_API = "https://opentdb.com/api.php?amount=1&type=multiple"

# --- 1. UNLIMITED TRUTH (VIA API) ---
@Client.on_message(filters.command("truth") & filters.group)
async def truth_game(client, message):
    try:
        # API call for truth
        response = requests.get(f"{TRUTH_DARE_API}truth").json()
        question = response['question']
        
        target = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
        
        await message.reply_text(
            f"<b>✨ ᴛʀᴜᴛʜ ᴏʀ ᴅᴀʀᴇ: ᴛʀᴜᴛʜ</b>\n"
            f"{line}\n"
            f"👤 <b>ꜰᴏʀ:</b> {target}\n"
            f"❓ <b>ǫᴜᴇsᴛɪᴏɴ:</b> <i>{question}</i>\n"
            f"{line}\n"
            f"<b>ᴊᴀʟᴅɪ ʙᴀᴛᴀᴏ {target}! 😂</b>"
        )
    except Exception as e:
        await message.reply_text("<b>❌ API Error:</b> Truth nahi mil pa raha!")

# --- 2. UNLIMITED DARE (VIA API) ---
@Client.on_message(filters.command("dare") & filters.group)
async def dare_game(client, message):
    try:
        # API call for dare
        response = requests.get(f"{TRUTH_DARE_API}dare").json()
        task = response['question']
        
        target = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
        
        await message.reply_text(
            f"<b>🔥 ᴛʀᴜᴛʜ ᴏʀ ᴅᴀʀᴇ: ᴅᴀʀᴇ</b>\n"
            f"{line}\n"
            f"👤 <b>ꜰᴏʀ:</b> {target}\n"
            f"🎯 <b>ᴛᴀsᴋ:</b> <b>{task}</b>\n"
            f"{line}\n"
            f"<b>ᴅᴀʀᴇ ᴘᴏᴏʀᴀ ᴋᴀʀᴏ ᴠᴀʀɴᴀ ᴘᴜɴɪsʜᴍᴇɴᴛ ᴍɪʟᴇɢɪ! 😎</b>"
        )
    except Exception as e:
        await message.reply_text("<b>❌ API Error:</b> Dare load nahi ho raha!")

# --- 3. UNLIMITED QUIZ (VIA OPEN TRIVIA API) ---
@Client.on_message(filters.command("quiz") & filters.group)
async def quiz_game(client, message):
    try:
        # API call for random quiz
        response = requests.get(QUIZ_API).json()
        data = response['results'][0]
        
        question = data['question'].replace("&quot;", '"').replace("&#039;", "'")
        correct_answer = data['correct_answer']
        
        msg = await message.reply_text(
            f"<b>🧩 ᴀɴɢᴇʟ's ɢʟᴏʙᴀʟ ǫᴜɪᴢ</b>\n"
            f"{line}\n"
            f"❓ <b>ǫᴜᴇsᴛɪᴏɴ:</b> {question}\n"
            f"{line}\n"
            f"<i>𝟻 sᴇᴄᴏɴᴅs ᴍᴇɪɴ ᴀɴsᴡᴇʀ ᴀᴀʏᴇɢᴀ...</i>"
        )
        
        await asyncio.sleep(5)
        await msg.edit(
            f"<b>🧩 ᴀɴɢᴇʟ's ɢʟᴏʙᴀʟ ǫᴜɪᴢ</b>\n"
            f"{line}\n"
            f"❓ <b>ǫᴜᴇsᴛɪᴏɴ:</b> {question}\n"
            f"✅ <b>ᴄᴏʀʀᴇᴄᴛ ᴀɴsᴡᴇʀ:</b> <code>{correct_answer}</code>\n"
            f"{line}\n"
            f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>ᴢᴇxx</b> 👑"
        )
    except Exception as e:
        await message.reply_text("<b>❌ API Error:</b> Quiz load karne mein dikkat ho rahi hai!")
