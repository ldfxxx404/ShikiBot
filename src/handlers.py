from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router
from parser import (
    get_random_anime,
    get_anime_info,
)

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        """
/random - radnom anime
"""
    )


@router.message(Command("random"))
async def get_random_handler(message: Message) -> None:
    await message.answer(get_random_anime())


@router.message()
async def get_anime(message: Message):
    title_name = message.text
    await message.answer(get_anime_info(title_name))
