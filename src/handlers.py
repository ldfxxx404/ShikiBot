from endpoints import GET_RANDOM_ANIME_URL, SEARCH_ANIME_URL
from headers import HEADERS
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router
from parser import Anime

router = Router()

anime = Anime(GET_RANDOM_ANIME_URL, SEARCH_ANIME_URL, HEADERS)


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        """
/random - radnom anime
"""
    )


@router.message(Command("random"))
async def get_random_handler(message: Message) -> None:
    await message.answer(anime.get_random_anime())


@router.message()
async def get_anime(message: Message):
    title_name = message.text
    await message.answer(anime.get_anime_info(title_name))
