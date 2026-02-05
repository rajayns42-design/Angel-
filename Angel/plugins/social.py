import requests
from pyrogram import Client, filters

# --- DECORATION ---
line = "✨ ══════════════════ ✨"
API_URL = "https://api.socialdownloader.xyz/all?url=" # Fast Public API

@Client.on_message(filters.regex(r"https?://(www\.)?(instagram\.com|tiktok\.com|youtube\.com|youtu\.be)/.+"))
async def social_downloader(client, message):
    url = message.matches[0].group(0)
    
    # Fast Processing Message
    status = await message.reply_text("<b>📥 ᴘʀᴏᴄᴇssɪɴɢ...</b>\n<i>ᴀɴɢᴇʟ ɪs ꜰᴇᴛᴄʜɪɴɢ ʏᴏᴜʀ ᴍᴇᴅɪᴀ!</i>")
    
    try:
        # Instant API Call
        response = requests.get(f"{API_URL}{url}").json()
        
        if response.get("status"):
            media_url = response['result']['url']
            caption = f"<b>✨ sᴏᴄɪᴀʟ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ</b>\n{line}\n👤 <b>ʙʏ:</b> {message.from_user.first_name}\n🖇️ <b>ʟɪɴᴋ:</b> <a href='{url}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n{line}"
            
            # Sending Video/Photo
            await message.reply_video(video=media_url, caption=caption)
            await status.delete()
        else:
            await status.edit("<b>❌ Error:</b> Link invalid hai ya video private hai!")
            
    except Exception as e:
        await status.edit(f"<b>❌ API Error:</b> Bot is busy, try again later!")

# --- SEARCH COMMAND ---
@Client.on_message(filters.command("social") & filters.group)
async def social_help(client, message):
    await message.reply_text(
        f"<b>📱 sᴏᴄɪᴀʟ ʜᴇʟᴘ</b>\n{line}\n"
        f"Bas Instagram ya TikTok ka link bhejo, Angel use auto-download kar degi!\n"
        f"Fast & Unlimited! 🚀\n{line}"
    )
