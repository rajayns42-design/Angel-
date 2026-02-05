import requests
from pyrogram import Client, filters

# --- CONFIGURATION ---
GROQ_API_KEY = "YOUR_GROQ_API_KEY_HERE" 
API_URL = "https://api.groq.com/openai/v1/chat/completions"

# --- CHATBOT LOGIC (Hinglish + Unlimited + Fast) ---
@Client.on_message(filters.text & ~filters.bot & (filters.group | filters.private))
async def angel_ai_chat(client, message):
    user_name = message.from_user.first_name
    user_input = message.text.lower()

    # --- 1. SPECIAL TRIGGER: ANGEL ---
    if "angel" in user_input:
        return await message.reply_text("Ha❤️‍🩹, mai hu angel")

    # --- 2. SPECIAL TRIGGER: OWNER ---
    if "owner" in user_input:
        return await message.reply_text("ᴍʏ ᴏᴡɴᴇʀ ɪs <b>ᴢᴇxx</b> 👑")

    # --- 3. UNLIMITED FAST AUTO-REPLY (HINDI + ENGLISH) ---
    payload = {
        "model": "llama3-8b-8192", 
        "messages": [
            {
                "role": "system", 
                "content": (
                    f"Your name is Angel, a sweet and bubbly girl. User's name is {user_name}. "
                    f"STRICT RULE 1: Start the reply with {user_name} ONLY ONCE. "
                    f"STRICT RULE 2: Speak in natural Hinglish (Mix of Hindi and English) like: "
                    f"'Kaise ho aap?', 'Main thik hoon, tum batao', 'That's so sweet!', 'Bilkul nahi re'. "
                    f"STRICT RULE 3: Keep replies very small and fast (under 10 words). "
                    f"Vibe: Friendly, cute, and casual girl chatting style."
                )
            },
            {"role": "user", "content": message.text}
        ],
        "max_tokens": 30, 
        "temperature": 0.8
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            reply_text = result['choices'][0]['message']['content']
            await message.reply_text(reply_text)
    except Exception as e:
        print(f"Chatbot Error: {e}")
