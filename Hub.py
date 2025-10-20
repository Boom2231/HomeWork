import asyncio
from aiogram import Bot, Dispatcher
import handlers.text_handlers

async def main():
    bot = Bot("token")
    dp = Dispatcher()

    dp.include_router(handlers.text_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
