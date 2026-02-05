import requests
import asyncio
from pyrogram import Client, filters

# --- CONFIGURATION ---
line = "✨ ══════════════════ ✨"

@Client.on_message(filters.command("riddle") & (filters.group | filters.private))
async def fast_riddle(client, message):
    try:
        # Fast API fetch
        res = requests.get("https://riddles-api.vercel.app/random").json()
        question, answer = res['riddle'], res['answer']
    except:
        return await message.reply_text("<b>❌ Error:</b> API slow hai, phir try karo!")

    # Instant Post
    riddle_msg = await message.reply_text(
        f"<b>🧩 ʀɪᴅᴅʟᴇ ᴛɪᴍᴇ!</b>\n"
        f"{line}\n"
        f"<b>🤔 Q:</b> <i>{question}</i>\n"
        f"{line}\n"
        f"⏳ <i>ᴊᴀᴡᴀʙ ᴅᴏ (𝟹𝟶s)...</i>"
    )

    try:
        # Fast Timeout (30s) for quick groups
        user_answer = await client.wait_for_message(message.chat.id, timeout=30)
        
        if answer.lower() in user_answer.text.lower():
            await user_answer.reply_text(
                f"<b>🎉 ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs!</b>\n"
                f"{line}\n"
                f"👤 <b>ᴡɪɴɴᴇʀ:</b> {user_answer.from_user.first_name}\n"
                f"✅ <b>ᴀɴsᴡᴇʀ:</b> <code>{answer}</code>\n"
                f"{line}"
            )
        else:
            # Agar galat jawab de toh bhi game khatam (Fast)
            await message.reply_text(f"<b>❌ ᴡʀᴏɴɢ!</b>\nSahi jawab tha: <code>{answer}</code>")
            
    except asyncio.TimeoutError:
        await riddle_msg.edit(f"<b>⏰ ᴛɪᴍᴇ ᴜᴘ!</b>\nSahi jawab: <code>{answer}</code>")
