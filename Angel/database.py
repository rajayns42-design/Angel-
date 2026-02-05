from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

# --- CONNECTION ---
client = AsyncIOMotorClient(MONGO_URL)
db = client.MafiaBot.users  # Database ka naam 'MafiaBot' aur collection 'users'

# --- DATABASE FUNCTIONS ---

async def get_user(user_id):
    """User ka sara data fetch karne ke liye"""
    user = await db.find_one({"user_id": user_id})
    if not user:
        # Agar naya user hai toh default values ke saath register karo
        new_user = {
            "user_id": user_id,
            "cash": 5000,          # Starting bonus
            "bank": 0,
            "wins": 0,
            "losses": 0,
            "level": 1,
            "bounty": 0,           # Supari amount
            "is_premium": False,
            "premium_expiry": 0,
            "last_rob": 0          # Cooldown check ke liye
        }
        await db.insert_one(new_user)
        return new_user
    return user

async def update_money(user_id, amount, mode="cash"):
    """Paisa add ya minus karne ke liye (cash ya bank)"""
    await db.update_one(
        {"user_id": user_id},
        {"$inc": {mode: amount}}
    )

async def set_premium(user_id, expiry_time):
    """User ko premium banane ke liye"""
    await db.update_one(
        {"user_id": user_id},
        {"$set": {"is_premium": True, "premium_expiry": expiry_time}}
    )

async def check_bounty(user_id):
    """Supari check karne ke liye"""
    user = await get_user(user_id)
    return user.get("bounty", 0)

async def get_top_players(limit=10):
    """Leaderboard ke liye top players nikalna"""
    return db.find().sort("cash", -1).limit(limit)
