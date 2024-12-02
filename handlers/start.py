from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards import main_menu

router = Router()

@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        text=f"🄰🅂🅂🄰🄻🄾🄼🅄 🄰🄻🄰🅈🄺🅄🄼 {message.from_user.first_name}!\n"
             f"Uzum Market botiga xush kelibsiz.\n\n/info kiriting\n",
        reply_markup=main_menu()
    )
