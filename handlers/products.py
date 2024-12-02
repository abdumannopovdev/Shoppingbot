from aiogram import Router, F
from aiogram.types import Message
from keyboards import inline_button

router = Router()

PRODUCTS = {
    "Televizor": [
        {"photo": "https://example.com/tv1.jpg", "caption": "Телевизор 1", "price": "1 000 000 so'm", "url": "https://example.com/tv1"},
        {"photo": "https://example.com/tv2.jpg", "caption": "Телевизор 2", "price": "2 000 000 so'm", "url": "https://example.com/tv2"},
    ],
    # Add other categories similarly
}

@router.message(F.text.in_(PRODUCTS.keys()))
async def show_products(message: Message):
    category = message.text
    for product in PRODUCTS[category]:
        await message.answer_photo(
            photo=product["photo"],
            caption=f"{product['caption']}\nNarxi: {product['price']}",
            reply_markup=inline_button(product["price"], product["url"])
        )
