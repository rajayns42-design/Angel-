import random
from pyrogram import Client, filters
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

db = AsyncIOMotorClient(MONGO_URL).MafiaBot.users
line = "━━━━━━━━━━━━━━━━━━━━"

@Client.on_message(filters.command("jealous
