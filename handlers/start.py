from aiogram import Router, F
from aiogram.types import Message
from database.base import AsyncSessionLocal
from database.models import User
from sqlalchemy.future import select

router = Router()

@router.message(F.text == "/start")
async def cmd_start(message: Message):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User).where(User.telegram_id == message.from_user.id))
        user = result.scalar_one_or_none()

        if user:
            await message.answer(f"👋 سلام {user.full_name}!\nشما قبلاً ثبت‌نام شده‌اید.\nنقش شما: {user.role}")
        else:
            new_user = User(
                telegram_id=message.from_user.id,
                full_name=message.from_user.full_name,
                role="member"
            )
            session.add(new_user)
            await session.commit()
            await message.answer(f"✅ ثبت‌نام انجام شد.\nسلام {new_user.full_name} عزیز! 👋")
