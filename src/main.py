from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
from handlers import router
from os import getenv
import asyncio
import logging
import sys


load_dotenv()

TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()
dp.include_router(router)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
