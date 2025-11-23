from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router
from endpoints import GET_ANIME_INFO_URL
from headers import HEADERS
from parser import (
    # get_anime_preview,
    # get_anime_name,
    # get_anime_score,
    # get_anime_episodes,
    get_random_anime,
)

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        """
/random - рандомное аниме
/info - информация об аниме
"""
    )


# @router.message(Command("info"))
# async def handle_info(message: Message) -> None:
#     await message.answer(get_anime_preview())
#     await message.answer(get_anime_name())
#     await message.answer(get_anime_score())
#     await message.answer(get_anime_episodes())


@router.message(Command("random"))
async def get_random_handler(message: Message) -> None:
    await message.answer(get_random_anime())
