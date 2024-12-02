import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import start, info, products


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Register handlers
    dp.include_router(start.router)
    dp.include_router(info.router)
    dp.include_router(products.router)

    # Start polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
