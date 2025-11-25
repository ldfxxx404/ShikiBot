from api import ShikimoriApiClient
from messages.anime_message import AnimeMessage


class RandomAnimeMessage:
    client: ShikimoriApiClient

    def __init__(self, client: ShikimoriApiClient):
        self.client = client

    async def generate(self) -> str:
        try:
            data = await self.client.get_random_anime()
            message = AnimeMessage(data=data)
            return message.generate()
        except Exception:
            return "Что-то пошло не так..."
