from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Televizor"), KeyboardButton(text="Telefon")],
            [KeyboardButton(text="Notebook"), KeyboardButton(text="Soat")],
            [KeyboardButton(text="Kansaner"), KeyboardButton(text="Kuler")],
            [KeyboardButton(text="Haladelnik"), KeyboardButton(text="Gaz pilita")],
            [KeyboardButton(text="Mikroto'lqinli pech"), KeyboardButton(text="Changyutgich")],
        ],
        resize_keyboard=True
    )

def info_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📍 Joylashuvni yuborish", request_location=True)],
            [KeyboardButton(text="📞 Kontaktni yuborish", request_contact=True)],
        ],
        resize_keyboard=True
    )

def inline_button(price, url):
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=f"{price}", url=url)]]
    )
