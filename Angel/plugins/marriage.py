from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import DIVORCE_COST, MARRIED_TAX_RATE, BOT_NAME
# Maan lete hain aapka database module 'db' hai
# from bot.database import db 

# --- 💔 DIVORCE COMMAND ---
@Client.on_message(filters.command("divorce") & filters.group)
async def divorce_cmd(client: Client, message: Message):
    user_id = message.from_user.id
    
    # Database check (Example logic)
    # partner = await db.get_partner(user_id)
    partner = None # Testing ke liye
    
    if not partner:
        return await message.reply_text("❌ **Aap pehle se hi single hain!**\nDivorce ke liye shaadi shuda hona zaroori hai.")

    text = (
        f"💔 **ᴅɪᴠᴏʀᴄᴇ ᴘᴀᴘᴇʀs**\n\n"
        f"Aap apne partner se alag hona chahte hain?\n"
        f"⚠️ **ᴄᴏsᴛ:** `{DIVORCE_COST}` coins\n\n"
        f"Kya aapko yakeen hai?"
    )
    
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✅ ʏᴇs, ɪ'ᴍ sᴜʀᴇ", callback_data=f"div_confirm_{user_id}"),
            InlineKeyboardButton("❌ ᴄᴀɴᴄᴇʟ", callback_data=f"div_cancel_{user_id}")
        ]
    ])
    
    await message.reply_text(text, reply_markup=buttons)

# --- 💍 PROPOSE COMMAND ---
@Client.on_message(filters.command("propose") & filters.group)
async def propose_cmd(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("❌ Kisi ko propose karne ke liye unke message par reply karein!")
    
    proposer = message.from_user
    target = message.reply_to_message.from_user

    if proposer.id == target.id:
        return await message.reply_text("🤨 Khud se shaadi nahi kar sakte, Capo!")

    text = (
        f"💍 **ᴍᴀʀʀɪᴀɢᴇ ᴘʀᴏᴘᴏsᴀʟ**\n\n"
        f"Hey {target.mention},\n"
        f"**{proposer.first_name}** ne aapko propose kiya hai!\n\n"
        f"✨ **ʙᴇɴᴇғɪᴛ:** Married couples ko tax mein `{int(MARRIED_TAX_RATE * 100)}%` ki chhoot milti hai!"
    )
    
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("❤️ ᴀᴄᴄᴇᴘᴛ", callback_data=f"mar_acc_{target.id}_{proposer.id}"),
            InlineKeyboardButton("💔 ʀᴇᴊᴇᴄᴛ", callback_data=f"mar_rej_{target.id}")
        ]
    ])
    
    await message.reply_photo(
        photo="https://graph.org/file/your_propose_image.jpg", # Config se image le sakte hain
        caption=text,
        reply_markup=buttons
    )

# --- CALLBACK HANDLERS ---
@Client.on_callback_query(filters.regex(r"div_confirm_"))
async def div_callback(client: Client, query: CallbackQuery):
    user_id = int(query.data.split("_")[2])
    if query.from_user.id != user_id:
        return await query.answer("Ye aapke liye nahi hai!", show_alert=True)
    
    # Logic: Database se partner remove karo aur coins deduct karo
    await query.message.edit_text(f"💔 **ᴅɪᴠᴏʀᴄᴇ sᴜᴄᴄᴇssғᴜʟ!**\n\nAap ab single hain. `{DIVORCE_COST}` coins kaat liye gaye hain.")

@Client.on_callback_query(filters.regex(r"mar_acc_"))
async def mar_callback(client: Client, query: CallbackQuery):
    data = query.data.split("_")
    target_id = int(data[2])
    proposer_id = int(data[3])
    
    if query.from_user.id != target_id:
        return await query.answer("Sirf wahi accept kar sakta hai jise propose kiya gaya hai!", show_alert=True)
    
    # Logic: Database mein dono ko marry kar do
    await query.message.edit_text(f"🎊 **ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs!**\n\nAb aap dono officially married hain! ❤️")
