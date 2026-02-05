import requests
from pyrogram import Client, filters

# --- CONFIGURATION ---
# Aap koi bhi free AI API use kar sakte hain (jaise Pollinations ya Lexica)
line = "✨ ══════════════════ ✨"

# --- 🎨 AI IMAGE GENERATION ---
@Client.on_message(filters.command("draw") & filters.group)
async def draw_image(client, message):
    if len(message.command) < 2:
        return await message.reply_text("<b>❌ Error:</b> Kya draw karna hai? \nUsage: `/draw a cute girl with angel wings`")
    
    prompt = message.text.split(None, 1)[1]
    waiting = await message.reply_text("<b>🎨 sᴋᴇᴛᴄʜɪɴɢ...</b>\n<i>ᴀɴɢᴇʟ ᴀɪ ɪs ᴅʀᴀᴡɪɴɢ ʏᴏᴜʀ ɪᴍᴀɢɪɴᴀᴛɪᴏɴ!</i>")
    
    # Pollinations AI (Free & Fast)
    img_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed=42"
    
    try:
        await message.reply_photo(img_url, caption=f"<b>✨ ʏᴏᴜʀ ᴀɪ ᴀʀᴛ ɪs ʀᴇᴀᴅʏ!</b>\n{line}\n<b>👤 ᴘʀᴏᴍᴘᴛ:</b> <code>{prompt}</code>\n{line}")
        await waiting.delete()
    except Exception as e:
        await waiting.edit(f"<b>❌ Error:</b> Kuch galat ho gaya! {e}")

# --- 👁️ IMAGE RECOGNITION (Vision) ---
@Client.on_message(filters.command("ask") & filters.reply)
async def ask_image(client, message):
    if not message.reply_to_message.photo:
        return await message.reply_text("<b>📸 Error:</b> Kisi photo par reply karke puchiye!")

    # Yahan hum Google Gemini ya Groq Vision use kar sakte hain
    # Abhi ke liye hum ek chota AI response set kar rahe hain
    await message.reply_text("<b>👀 ᴀɴɢᴇʟ ɪs ʟᴏᴏᴋɪɴɢ ᴀᴛ ᴛʜɪs ᴘʜᴏᴛᴏ...</b>\n<i>(Vision feature setup needed with API)</i>")
