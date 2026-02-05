from pyrogram import Client, filters
import random

# --- STORAGE (Fast Memory) ---
marriages = {} 
line = "✨ ══════════════════ ✨"

@Client.on_message(filters.command(["marry", "marriage"]) & filters.group)
async def marry_user(client, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>💍 Kise propose karna hai? Reply toh karo!</b>")

    proposer = message.from_user
    target = message.reply_to_message.from_user

    if proposer.id == target.id:
        return await message.reply_text("<b>😂 Khud se shadi? Itne bure din aa gaye?</b>")

    if target.is_bot:
        return await message.reply_text("<b>🤖 Main ek AI hoon, meri shadi ZEXX se fix ho chuki hai!</b>")

    # Shadi ka logic
    marriages[proposer.id] = target.first_name
    marriages[target.id] = proposer.first_name

    await message.reply_text(
        f"<b>🎊 ᴍᴀʀʀɪᴀɢᴇ sᴇᴛᴛʟᴇᴅ! 🎊</b>\n"
        f"{line}\n"
        f"🤵 <b>ɢʀᴏᴏᴍ:</b> {proposer.first_name}\n"
        f"👰 <b>ʙʀɪᴅᴇ:</b> {target.first_name}\n"
        f"{line}\n"
        f"<i>ᴀɴɢᴇʟ ɪs sᴏ ʜᴀᴘᴘʏ ꜰᴏʀ ʏᴏᴜ ʙᴏᴛʜ! ❤️‍🔥</i>\n"
        f"<b>sᴛᴀᴛᴜs:</b> ᴊᴜsᴛ ᴍᴀʀʀɪᴇᴅ! 💍"
    )

@Client.on_message(filters.command("divorce") & filters.group)
async def divorce_user(client, message):
    user_id = message.from_user.id
    if user_id not in marriages:
        return await message.reply_text("<b>🤔 Pehle shadi toh kar lo, phir divorce maangna!</b>")
    
    partner = marriages[user_id]
    del marriages[user_id]
    # Partner ka record bhi clear karna agar exists ho
    
    await message.reply_text(
        f"<b>💔 ᴅɪᴠᴏʀᴄᴇ ᴀʟᴇʀᴛ 💔</b>\n"
        f"{line}\n"
        f"<b>{message.from_user.first_name}</b> ne <b>{partner}</b> se talaq le liya!\n"
        f"<i>sɪɴɢʟᴇ ʟɪꜰᴇ ɪs ʙᴇsᴛ, ʜᴀɪ ɴᴀ? 😉</i>\n"
        f"{line}"
    )

@Client.on_message(filters.command("couple") & filters.group)
async def couple_of_day(client, message):
    # Group ke random users select karna (Fast logic)
    all_members = []
    async for member in client.get_chat_members(message.chat.id, limit=50):
        if not member.user.is_bot:
            all_members.append(member.user.first_name)
    
    if len(all_members) < 2:
        return await message.reply_text("<b>⚠️ Group mein log kam hain!</b>")

    c1, c2 = random.sample(all_members, 2)
    
    await message.reply_text(
        f"<b>💞 ᴄᴏᴜᴘʟᴇ ᴏꜰ ᴛʜᴇ ᴅᴀʏ 💞</b>\n"
        f"{line}\n"
        f"👩‍❤️‍👨 <b>{c1}</b>  +  <b>{c2}</b>\n\n"
        f"<i>Ye jodi toh Rab ne bana di! ✨</i>\n"
        f"{line}"
    )
