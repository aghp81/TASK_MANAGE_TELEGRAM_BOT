import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.default import DefaultBotProperties
from database.db import init_db, SessionLocal
from database.models import Task, Phase
from database.db import init_db  #اجرای اولیه برای ساخت دیتابیس


# پراکسی (در صورت نیاز)
proxy_url = "http://51.81.245.3:17981"  # ← اینجا پراکسی خودت رو بذار
session = AiohttpSession(proxy=proxy_url)

# ثبت هندلرها
start.register_handlers(dp)
add_task.register_handlers(dp)
add_phase.register_handlers(dp)
auth.register_handlers(dp)

# راه‌اندازی بات و دیسپچر
bot = Bot(
    token="7972234523:AAEsQ18N_JsdBrhfFZ8xK3MZ5kHjy_Ox4iI",
    session=session,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# تعریف وضعیت‌ها
class TaskState(StatesGroup):
    awaiting_task_input = State()

# /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("سلام! از /addtask برای افزودن تسک استفاده کنید.")

# /addtask
@dp.message(Command("addtask"))
async def add_task(message: Message, state: FSMContext):
    await message.answer("لطفاً تسک را وارد کنید (مثلاً: طراحی صفحه لاگین برای محمد).")
    await state.set_state(TaskState.awaiting_task_input)

# دریافت تسک
@dp.message(TaskState.awaiting_task_input)
async def receive_task(message: Message, state: FSMContext):
    task_text = message.text
    await message.answer(f"✅ تسک ثبت شد:\n{task_text}")
    await state.clear()

# اجرای بات
async def main():
    print("بات در حال اجراست...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    init_db()#اجرای اولیه برای ساخت دیتابیس

    print("Database initialized.")
