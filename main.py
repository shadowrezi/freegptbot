from os import getenv
import asyncio

from aiogram import Bot, Dispatcher

from dotenv import load_dotenv

from handlers.chat import form


load_dotenv()


async def main():
    TOKEN = getenv('TG_TOKEN')
    bot = Bot(TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    
    dp.include_router(form)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
