from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
from os import getenv
import asyncio
import logging
import sys

from commands import BOT_COMMANDS
from handlers import router as main_router

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()


async def main() -> None:
    if not TOKEN:
        raise TypeError("BOT_TOKEN env variable must be provided")

    dp.include_router(main_router)

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
    await bot.set_my_commands(commands=BOT_COMMANDS)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
