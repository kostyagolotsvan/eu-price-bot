import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer("🚴 EU Bike Price Bot\nUse /search <product>")

@dp.message(Command("search"))
async def search(msg: types.Message):
    query = msg.text.replace("/search", "").strip()
    await msg.answer(f"✅ Bot is running.\nYou searched for: {query}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
