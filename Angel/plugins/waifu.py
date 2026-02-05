import requests
from pyrogram import Client, filters

# --- DECORATION ---
line = "✨ ══════════════════ ✨"

@Client.on_message(filters.command("waifu") & (filters.group | filters.private))
async def get_waifu(client, message):
    # Chatting vibe ke liye pehle ek message
    waiting = await message.reply_text("<b>🌸 sᴇᴀʀᴄʜɪɴɢ...</b>\n<i>ᴀɴɢᴇʟ ɪs ғɪɴᴅɪɴɢ ᴀ ᴄᴜᴛᴇ ᴡᴀɪғᴜ ғᴏʀ ʏᴏᴜ!</i>")
    
    # Waifu API (Free & Fast)
    url = "https://api.waifu.pics/sfw/waifu"
    
    try:
        response = requests.get(url).json()
        img_url = response['url']
        
        # Photo bhejna stylish caption ke saath
        await message.reply_photo(
            photo=img_url,
            caption=(
                f"<b>✨ ʏᴏᴜʀ ᴡᴀɪғᴜ ɪs ʜᴇʀᴇ!</b>\n"
                f"{line}\n"
                f"<b>👤 ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:</b> {message.from_user.first_name}\n"
                f"<b>🎀 sᴛᴀᴛᴜs:</b> ᴏɴʟɪɴᴇ\n"
                f"{line}\n"
                f"<i>ᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ ᴀɴɢᴇʟ</i>"
            )
        )
        await waiting.delete()
        
    except Exception as e:
        await waiting.edit(f"<b>❌ Error:</b> Waifu nahi mil rahi! {e}")

# --- NEKO COMMAND (Optional Fun) ---
@Client.on_message(filters.command("neko") & (filters.group | filters.private))
async def get_neko(client, message):
    url = "https://api.waifu.pics/sfw/neko"
    response = requests.get(url).json()
    await message.reply_photo(response['url'], caption="<b>🐱 ɴʏᴀᴀᴀ~ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ɴᴇᴋᴏ!</b>")
