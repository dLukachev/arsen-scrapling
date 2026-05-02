import os
import logging
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from bot.handlers import user

logging.basicConfig(level=logging.INFO)
load_dotenv()

TOKEN = os.getenv("TOKEN")
dp = Dispatcher()
bot = Bot(TOKEN)  # type: ignore


async def start():
    dp.include_router(user)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start())
