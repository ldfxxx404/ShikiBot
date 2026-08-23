from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from api import ShikimoriApiClient
from messages.random_anime_message import RandomAnimeMessage
from messages.search_anime_message import SearchAnimeMessage
from messages.similar_anime_message import SimilarAnimeMessage
from messages.start_message import StartMessage

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    text = StartMessage().generate()
    await message.answer(text=text)


@router.message(Command("random"))
async def get_random_handler(message: Message) -> None:
    text = await RandomAnimeMessage(client=ShikimoriApiClient()).generate()
    await message.answer(text=text)


@router.message(Command("similar"))
async def get_similar_anime(message: Message) -> None:
    if not message.text:
        return
    anime_id = message.text
    text = await SimilarAnimeMessage(client=ShikimoriApiClient()).generate(
        anime_id=anime_id
    )
    await message.answer(text=text)


@router.message()
async def user_input_handler(message: Message) -> None:
    if not message.text:
        return
    title_name = message.text
    text = await SearchAnimeMessage(client=ShikimoriApiClient()).generate(
        name=title_name
    )
    await message.answer(text=text)
