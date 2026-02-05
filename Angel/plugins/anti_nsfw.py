import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message

# --- CONFIG ---
# ZEXX, sightengine.com par free account banao aur API details yahan dalo
SIGHTENGINE_API_USER = "YOUR_API_USER"
SIGHTENGINE_API_SECRET = "YOUR_API_SECRET"
line = "🛡️ 𝐀𝐍𝐓𝐈-𝟏𝟖+ 𝐒𝐄𝐂𝐔𝐑𝐈𝐓𝐘 🛡️"

async def is_nsfw(file_path):
    """Media scan karne ke liye function"""
    params = {
        'models': 'nudity-2.0,wad,offensive',
        'api_user': SIGHTENGINE_API_USER,
        'api_secret': SIGHTENGINE_API_SECRET
    }
    files = {'media': open(file_path, 'rb')}
    try:
        r = requests.post('https://api4.sightengine.com/1.0/check.json', files=files, data=params)
        output = r.json()
        if output['status'] == 'success':
            nudity = output['nudity']
            # Agar nudity score high hai (Sexual activity or display)
            if nudity['sexual_activity'] > 0.2 or nudity['sexual_display'] > 0.2 or nudity['erotica'] > 0.3:
                return True
    except Exception as e:
        print(f"Scanning Error: {e}")
    return False

# --- SCANNER FOR ALL MEDIA (PHOTO, VIDEO, STICKER, GIF) ---
@Client.on_message(filters.group & (filters.photo | filters.video | filters.sticker | filters.animation))
async def nsfw_guard(client, message: Message):
    # Admin check - Admins are safe
    try:
        user = await client.get_chat_member(message.chat.id, message.from_user.id)
        if user.status in ["administrator", "creator"]:
            return
    except:
        pass

    # Media download karna scan ke liye
    file_path = await client.download_media(message)
    
    if await is_nsfw(file_path):
        try:
            await message.delete() # Gandi media delete
            
            # User ko warn ya mute karna
            warn_text = (
                f"<b>🚫 ɴsꜰᴡ/𝟷𝟾+ ᴄᴏɴᴛᴇɴᴛ ᴅᴇᴛᴇᴄᴛᴇᴅ!</b>\n"
                f"{line}\n"
                f"👤 <b>ᴜsᴇʀ:</b> {message.from_user.mention}\n"
                f"📝 <b>ᴀᴄᴛɪᴏɴ:</b> Media Deleted\n"
                f"💡 <b>ʀᴇᴀsᴏɴ:</b> Adult content is strictly prohibited!\n"
                f"{line}\n"
                f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ: <b>ᴢᴇxx</b> 👑"
            )
            await client.send_message(message.chat.id, warn_text)
        except Exception as e:
            print(f"Delete Error: {e}")
    
    # Clean up local file
    if os.path.exists(file_path):
        os.remove(file_path)
