import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.database.models import async_main


async def main():
    await async_main()
    bot = Bot(token='7221166820:AAEKm8mLOfekc_NPILa6IJ8CYVd0158xmSM')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot off")
