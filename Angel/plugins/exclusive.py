from pyrogram import Client, filters
import asyncio

# --- OWNER SETTINGS ---
# Note: ZEXX, apna user ID yahan likh dena
OWNER_ID = 123456789  # Replace with your Telegram ID
line = "👑 ══════════════════ 👑"

# --- HELPER: OWNER CHECK ---
def is_owner(_, __, message):
    return message.from_user and message.from_user.id == OWNER_ID

owner_filter = filters.create(is_owner)

# --- COMMAND: BROADCAST (Pure Groups mein Message) ---
@Client.on_message(filters.command("broadcast") & owner_filter)
async def broadcast(client, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>❌ Error:</b> Kisi message par reply karke `/broadcast` likho!")

    ex_msg = await message.reply_text("<b>📢 ʙʀᴏᴀᴅᴄᴀsᴛ sᴛᴀʀᴛᴇᴅ...</b>")
    chats = []
    async for dialog in client.get_dialogs():
        if dialog.chat.type in ["group", "supergroup"]:
            chats.append(dialog.chat.id)

    done = 0
    failed = 0
    for chat_id in chats:
        try:
            await message.reply_to_message.copy(chat_id)
            done += 1
            await asyncio.sleep(0.3) # Rate limit se bachne ke liye (Fast)
        except:
            failed += 1
    
    await ex_msg.edit(
        f"<b>✅ ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ</b>\n{line}\n"
        f"👤 <b>ᴏᴡɴᴇʀ:</b> ᴢᴇxx\n"
        f"📤 <b>sᴇɴᴛ ᴛᴏ:</b> {done} Chats\n"
        f"❌ <b>ғᴀɪʟᴇᴅ:</b> {failed}\n{line}"
    )

# --- COMMAND: STATS (Bot ki reach check karein) ---
@Client.on_message(filters.command("stats") & owner_filter)
async def bot_stats(client, message):
    groups = 0
    pms = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in ["group", "supergroup"]:
            groups += 1
        elif dialog.chat.type == "private":
            pms += 1
    
    await message.reply_text(
        f"<b>📊 ᴀɴɢᴇʟ ʙᴏᴛ sᴛᴀᴛs</b>\n{line}\n"
        f"👥 <b>ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs:</b> {groups}\n"
        f"👤 <b>ᴛᴏᴛᴀʟ ᴜsᴇʀs:</b> {pms}\n"
        f"👑 <b>ᴏᴡɴᴇʀ:</b> ᴢᴇxx\n{line}"
    )

# --- COMMAND: LEAVE GROUP (Kahin se bot nikalna ho) ---
@Client.on_message(filters.command("leave") & owner_filter)
async def leave_chat(client, message):
    chat_id = message.chat.id
    await message.reply_text("<b>👋 Bye! Owner ke order par main ye group chhod rahi hoon.</b>")
    await client.leave_chat(chat_id)
