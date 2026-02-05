import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

# --- OWNER ID (ZEXX ONLY) ---
OWNER_ID = 123456789 # Yahan apni ID daal dena
line = "✨ ══════════════════ ✨"

@Client.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def global_broadcast(client, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>❌ Error:</b> Kisi message par reply karke `/broadcast` likho!")

    ex_msg = await message.reply_text("<b>📢 ɢʟᴏʙᴀʟ ʙʀᴏᴀᴅᴄᴀsᴛ sᴛᴀʀᴛᴇᴅ...</b>\n<i>Sabhi users aur groups ko bhej rahi hoon!</i>")
    
    # Saare chats (Groups + Private Users) fetch karna
    all_chats = []
    async for dialog in client.get_dialogs():
        all_chats.append(dialog.chat.id)

    done = 0
    failed = 0
    
    # Fast Broadcasting Loop
    for chat_id in all_chats:
        try:
            await message.reply_to_message.copy(chat_id)
            done += 1
            # Rate limit se bachne ke liye chota delay (Super Fast)
            await asyncio.sleep(0.1) 
        except FloodWait as e:
            await asyncio.sleep(e.value) # Agar Telegram rok de toh wait karega
            await message.reply_to_message.copy(chat_id)
            done += 1
        except Exception:
            failed += 1
            continue

    await ex_msg.edit(
        f"<b>✅ ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ!</b>\n"
        f"{line}\n"
        f"👤 <b>ᴏᴡɴᴇʀ:</b> ᴢᴇxx\n"
        f"🚀 <b>ᴛᴏᴛᴀʟ sᴇɴᴛ:</b> {done}\n"
        f"❌ <b>ғᴀɪʟᴇᴅ:</b> {failed}\n"
        f"{line}\n"
        f"<i>Sab jagah message pahunch gaya! 😎</i>"
    )
