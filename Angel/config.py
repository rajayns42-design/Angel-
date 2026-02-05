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
OWNER_USERNAME = "ZEXX" # [cite: 2026-02-04]
BOT_OWNER = "ZEXX" # [cite: 2026-02-04]
BOT_NAME = "📡 Angel xẞ~"

# --- ᴄʜᴀɴɴᴇʟs & ʟᴏɢɢᴇʀ ---
SUPPORT_CHAT = "https://t.me/your_support" # Apna link dalo
UPDATE_CHANNEL = "https://t.me/your_channel" # Apna link dalo
LOGGER_GROUP = -1001234567890 # Logs yahan aayenge

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
AUTO_REVIVE_HOURS = 6
AUTO_REVIVE_BONUS = 200
MIN_CLAIM_MEMBERS = 100

# --- 🛒 sʜᴏᴘ ɪᴛᴇᴍs (Full 60+ Items from Screenshot) ---
SHOP_ITEMS = [
    # --- WEAPONS (Damage Buff) ---
    {"id": "stick", "name": "🪵 Stick", "price": 500, "type": "weapon", "buff": 0.01},
    {"id": "brick", "name": "🧱 Brick", "price": 1000, "type": "weapon", "buff": 0.02},
    {"id": "slingshot", "name": "🏹 Slingshot", "price": 2000, "type": "weapon", "buff": 0.03},
    {"id": "knife", "name": "🔪 Knife", "price": 3500, "type": "weapon", "buff": 0.05},
    {"id": "bat", "name": "🏏 Bat", "price": 5000, "type": "weapon", "buff": 0.08},
    {"id": "axe", "name": "🪓 Axe", "price": 7500, "type": "weapon", "buff": 0.10},
    {"id": "hammer", "name": "🔨 Hammer", "price": 10000, "type": "weapon", "buff": 0.12},
    {"id": "chainsaw", "name": "🪚 Chainsaw", "price": 15000, "type": "weapon", "buff": 0.15},
    {"id": "pistol", "name": "🔫 Pistol", "price": 25000, "type": "weapon", "buff": 0.20},
    {"id": "shotgun", "name": "🔫 Shotgun", "price": 40000, "type": "weapon", "buff": 0.25},
    {"id": "uzi", "name": "🔫 Uzi", "price": 55000, "type": "weapon", "buff": 0.30},
    {"id": "katana", "name": "⚔️ Katana", "price": 75000, "type": "weapon", "buff": 0.35},
    {"id": "ak47", "name": "💥 AK-47", "price": 100000, "type": "weapon", "buff": 0.40},
    {"id": "minigun", "name": "🔥 Minigun", "price": 150000, "type": "weapon", "buff": 0.45},
    {"id": "sniper", "name": "🎯 Sniper", "price": 200000, "type": "weapon", "buff": 0.50},
    {"id": "rpg", "name": "🚀 RPG", "price": 300000, "type": "weapon", "buff": 0.55},
    {"id": "tank", "name": "🚜 Tank", "price": 500000, "type": "weapon", "buff": 0.58},
    {"id": "laser", "name": "⚡ Laser", "price": 800000, "type": "weapon", "buff": 0.59},
    {"id": "deathnote", "name": "📓 Death Note", "price": 5000000, "type": "weapon", "buff": 0.60},

    # --- ARMOR (Block Chance) ---
    {"id": "paper", "name": "📰 Newspaper", "price": 500, "type": "armor", "buff": 0.01},
    {"id": "cardboard", "name": "📦 Cardboard", "price": 1000, "type": "armor", "buff": 0.02},
    {"id": "cloth", "name": "👕 Cloth", "price": 2500, "type": "armor", "buff": 0.05},
    {"id": "leather", "name": "🧥 Leather", "price": 8000, "type": "armor", "buff": 0.08},
    {"id": "chain", "name": "⛓️ Chain", "price": 20000, "type": "armor", "buff": 0.10},
    {"id": "riot", "name": "🛡️ Riot Shield", "price": 40000, "type": "armor", "buff": 0.15},
    {"id": "swat", "name": "👮 SWAT", "price": 60000, "type": "armor", "buff": 0.20},
    {"id": "iron", "name": "🦾 Iron Suit", "price": 100000, "type": "armor", "buff": 0.25},
    {"id": "diamond", "name": "💎 Diamond", "price": 200000, "type": "armor", "buff": 0.30},
    {"id": "obsidian", "name": "🌑 Obsidian", "price": 400000, "type": "armor", "buff": 0.35},
    {"id": "nano", "name": "🦾 Nano Suit", "price": 700000, "type": "armor", "buff": 0.40},
    {"id": "vibranium", "name": "🛡️ Vibranium", "price": 1500000, "type": "armor", "buff": 0.50},
    {"id": "force", "name": "🔮 Forcefield", "price": 3000000, "type": "armor", "buff": 0.55},
    {"id": "plot", "name": "🎬 Plot Armor", "price": 10000000, "type": "armor", "buff": 0.60},

    # --- FLEX (Luxury Items) ---
    {"id": "cookie", "name": "🍪 Cookie", "price": 100, "type": "flex", "buff": 0},
    {"id": "coffee", "name": "☕ Starbucks", "price": 300, "type": "flex", "buff": 0},
    {"id": "rose", "name": "🌹 Rose", "price": 500, "type": "flex", "buff": 0},
    {"id": "sushi", "name": "🍣 Sushi Platter", "price": 2000, "type": "flex", "buff": 0},
    {"id": "vodka", "name": "🍾 Vodka", "price": 5000, "type": "flex", "buff": 0},
    {"id": "ring", "name": "💍 Gold Ring", "price": 10000, "type": "flex", "buff": 0},
    {"id": "ps5", "name": "🎮 PS5 Pro", "price": 15000, "type": "flex", "buff": 0},
    {"id": "iphone", "name": "📱 iPhone 16 Pro", "price": 25000, "type": "flex", "buff": 0},
    {"id": "macbook", "name": "💻 MacBook M3", "price": 50000, "type": "flex", "buff": 0},
    {"id": "gucci", "name": "👜 Gucci Bag", "price": 75000, "type": "flex", "buff": 0},
    {"id": "rolex", "name": "⌚ Rolex", "price": 100000, "type": "flex", "buff": 0},
    {"id": "diamond_ring", "name": "💎 Solitaire", "price": 250000, "type": "flex", "buff": 0},
    {"id": "tesla", "name": "🚗 Tesla", "price": 400000, "type": "flex", "buff": 0},
    {"id": "lambo", "name": "🏎️ Lambo", "price": 800000, "type": "flex", "buff": 0},
    {"id": "heli", "name": "🚁 Helicopter", "price": 1500000, "type": "flex", "buff": 0},
    {"id": "yacht", "name": "🛥️ Super Yacht", "price": 3000000, "type": "flex", "buff": 0},
    {"id": "mansion", "name": "🏰 Mansion", "price": 5000000, "type": "flex", "buff": 0},
    {"id": "jet", "name": "🛩️ Private Jet", "price": 10000000, "type": "flex", "buff": 0},
    {"id": "island", "name": "🏝️ Island", "price": 25000000, "type": "flex", "buff": 0},
    {"id": "moon", "name": "🌙 The Moon", "price": 100000000, "type": "flex", "buff": 0},
    {"id": "mars", "name": "🔴 Mars", "price": 500000000, "type": "flex", "buff": 0},
    {"id": "sun", "name": "☀️ The Sun", "price": 1000000000, "type": "flex", "buff": 0},
    {"id": "galaxy", "name": "🌌 Milky Way", "price": 5000000000, "type": "flex", "buff": 0},
    {"id": "blackhole", "name": "🕳️ Black Hole", "price": 9999999999, "type": "flex", "buff": 0},
]

# --- ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴs ---
PREMIUM_PLANS = {
    "month": 99,
    "year": 999,
    "lifetime": 1499
}
UPI_ID = "zexx@upi"
