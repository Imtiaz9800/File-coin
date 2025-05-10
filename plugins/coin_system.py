
from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from pymongo import MongoClient
import os

# Connect to MongoDB
mongo_url = os.environ.get("DATABASE_URL")
client = MongoClient(mongo_url)
db = client[os.environ.get("DATABASE_NAME", "Cluster0")]
users = db["users"]
shorteners = db["shorteners"]

def get_or_create_user(user_id):
    user = users.find_one({"user_id": user_id})
    if not user:
        user = {"user_id": user_id, "coins": 0, "shortner_index": 0}
        users.insert_one(user)
    return user

@Client.on_message(filters.command("balance"))
async def balance_command(client, message: Message):
    user = get_or_create_user(message.from_user.id)
    await message.reply(f"You have {user['coins']} coin(s).")

@Client.on_message(filters.command("earn"))
async def earn_command(client, message: Message):
    user = get_or_create_user(message.from_user.id)
    shortner_list = list(shorteners.find())
    if not shortner_list:
        await message.reply("No shorteners are available at the moment.")
        return

    index = user.get("shortner_index", 0) % len(shortner_list)
    link = shortner_list[index]["url"]
    users.update_one({"user_id": user["user_id"]}, {
        "$set": {"shortner_index": index + 1},
        "$inc": {"coins": 10}
    })
    await message.reply(f"Complete this shortlink to earn coins:
{link}
(+10 coins)")

@Client.on_message(filters.command("givecoins") & filters.user(OWNER_ID))
async def givecoins_command(client, message: Message):
    try:
        _, uid, amount = message.text.split()
        uid, amount = int(uid), int(amount)
        get_or_create_user(uid)
        users.update_one({"user_id": uid}, {"$inc": {"coins": amount}})
        await message.reply(f"Gave {amount} coins to user {uid}.")
    except Exception as e:
        await message.reply("Usage: /givecoins <user_id> <amount>")

@Client.on_message(filters.command("addshortner") & filters.user(OWNER_ID))
async def addshortner_command(client, message: Message):
    try:
        url = message.text.split(" ", 1)[1]
        shorteners.insert_one({"url": url})
        await message.reply("Shortener URL added.")
    except:
        await message.reply("Usage: /addshortner <shortner_url>")
