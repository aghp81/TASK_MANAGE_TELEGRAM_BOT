from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import asyncio

from config import BOT_TOKEN
from database.base import init_db
from handlers import start

async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    
    await init_db()
    
    dp.include_routers(start.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
