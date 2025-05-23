import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = "7972234523:AAEsQ18N_JsdBrhfFZ8xK3MZ5kHjy_Ox4iI"
proxy_url = "http://51.81.245.3:17981"  # آدرس پراکسی خودت رو اینجا بگذار

async def start_handler(message: Message):
    await message.answer("سلام! ربات مدیریت پروژه آماده است.")

async def main():
    # ساخت session با پراکسی
    session = AiohttpSession(proxy=proxy_url)
    bot = Bot(token=BOT_TOKEN, session=session)
    dp = Dispatcher()


    # ثبت هندلر دستور /start
    dp.message.register(start_handler, Command(commands=["start"]))

    print("بات در حال اجراست...")
    await bot.delete_webhook()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

