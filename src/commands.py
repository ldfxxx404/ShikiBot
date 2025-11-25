from aiogram.types import BotCommand

BOT_COMMANDS: list[BotCommand] = [
    BotCommand(command="start", description="Start interact with bot"),
    BotCommand(command="random", description="Get random Shikimori anime"),
]
