import os
from dotenv import load_dotenv

load_dotenv()

# --- ʙᴏᴛ ᴛᴏᴋᴇɴ & ᴀᴘɪ ---
API_ID = int(os.environ.get("API_ID", "1234567"))
API_HASH = os.environ.get("API_HASH", "your_api_hash_here")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token_here")

# --- ᴅᴀᴛᴀʙᴀsᴇ ---
MONGO_URL = os.environ.get("MONGO_URL", "your_mongodb_url_here")

# --- ᴏᴡɴᴇʀ & ʙʀᴀɴᴅɪɴɢ ---
OWNER_ID = int(os.environ.get("OWNER_ID", "123456789"))
OWNER_USERNAME = "ZEXX"
BOT_OWNER = "ZEXX" # [cite: 2026-02-04]
BOT_NAME = "📡 Angel xẞ~"

# --- ᴄʜᴀɴɴᴇʟs & ʟᴏɢɢᴇʀ ---
SUPPORT_CHAT = "https://t.me/your_support"
UPDATE_CHANNEL = "https://t.me/your_channel"
LOGGER_GROUP = -1001234567890  # Logs yahan aayenge

# --- ᴍᴇᴅɪᴀ ᴜʀʟs ---
START_IMG = "https://graph.org/file/your_start_image.jpg"
QR_LINK = "https://graph.org/file/your_qr_link.jpg"

# --- ɢᴀᴍᴇ ᴄᴏɴsᴛᴀɴᴛs (As per your Screenshot) ---
REVIVE_COST = 500
PROTECT_1D_COST = 1000
PROTECT_2D_COST = 1800
REGISTER_BONUS = 5000
CLAIM_BONUS = 2000
RIDDLE_REWARD = 1000
DIVORCE_COST = 2000
WAIFU_PROPOSE_COST = 5000
TAX_RATE = 0.10
MARRIED_TAX_RATE = 0.05

# --- 🛒 sʜᴏᴘ ɪᴛᴇᴍs (Full 60+ Items List) ---
SHOP_ITEMS = [
    # WEAPONS (Damage Buff)
    {"id": "stick", "name": "🪵 Stick", "price": 500, "type": "weapon", "buff": 0.01},
    {"id": "brick", "name": "🧱 Brick", "price": 1000, "type": "weapon", "buff": 0.02},
    {"id": "slingshot", "name": "🏹 Slingshot", "price": 2000, "type": "weapon", "buff": 0.03},
    {"id": "knife", "name": "🔪 Knife", "price": 3500, "type": "weapon", "buff": 0.05},
    {"id": "bat", "name": "🏏 Bat", "price": 5000, "type": "weapon", "buff": 0.08},
    {"id": "axe", "name": "🪓 Axe", "price": 7500, "type": "weapon", "buff": 0.10},
    {"id": "chainsaw", "name": "🪚 Chainsaw", "price": 15000, "type": "weapon", "buff": 0.15},
    {"id": "pistol", "name": "🔫 Pistol", "price": 25000, "type": "weapon", "buff": 0.20},
    {"id": "ak47", "name": "💥 AK-47", "price": 100000, "type": "weapon", "buff": 0.40},
    {"id": "deathnote", "name": "📓 Death Note", "price": 5000000, "type": "weapon", "buff": 0.60},

    # ARMOR (Block Chance)
    {"id": "paper", "name": "📰 Newspaper", "price": 500, "type": "armor", "buff": 0.01},
    {"id": "cloth", "name": "👕 Cloth", "price": 2500, "type": "armor", "buff": 0.05},
    {"id": "iron", "name": "🦾 Iron Suit", "price": 100000, "type": "armor", "buff": 0.25},
    {"id": "vibranium", "name": "🛡️ Vibranium", "price": 1500000, "type": "armor", "buff": 0.50},

    # FLEX (No Buff, Just Swag)
    {"id": "cookie", "name": "🍪 Cookie", "price": 100, "type": "flex", "buff": 0},
    {"id": "iphone", "name": "📱 iPhone 16 Pro", "price": 25000, "type": "flex", "buff": 0},
    {"id": "lambo", "name": "🏎️ Lambo", "price": 800000, "type": "flex", "buff": 0},
    {"id": "island", "name": "🏝️ Island", "price": 50000000, "type": "flex", "buff": 0},
    {"id": "blackhole", "name": "🕳️ Black Hole", "price": 999999999, "type": "flex", "buff": 0},
]

# --- ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴs ---
PREMIUM_PLANS = {
    "month": 99,
    "year": 999,
    "lifetime": 1499
}
UPI_ID = "zexx@upi"

