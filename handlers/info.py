from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards import info_menu

router = Router()

@router.message(Command("info"))
async def info_command(message: Message):
    await message.answer("Iltimos, quyidagi variantlardan birini tanlang:", reply_markup=info_menu())
