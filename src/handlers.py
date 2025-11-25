from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router
from messages.start_message import StartMessage
from messages.random_anime_message import RandomAnimeMessage
from messages.search_anime_message import SearchAnimeMessage
from api import ShikimoriApiClient

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    text = StartMessage().generate()
    await message.answer(text=text)


@router.message(Command("random"))
async def get_random_handler(message: Message) -> None:
    text = await RandomAnimeMessage(client=ShikimoriApiClient()).generate()
    await message.answer(text=text)


@router.message()
async def user_input_handler(message: Message) -> None:
    if not message.text:
        return
    title_name = message.text
    text = await SearchAnimeMessage(client=ShikimoriApiClient()).generate(name=title_name)
    await message.answer(text=text)
