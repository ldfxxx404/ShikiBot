from api import ShikimoriApiClient
from messages.anime_message import AnimeMessage


class SearchAnimeMessage:
    client: ShikimoriApiClient

    def __init__(self, client: ShikimoriApiClient):
        self.client = client

    async def generate(self, name: str) -> str:
        try:
            data = await self.client.search_for_anime(name=name)
            message = AnimeMessage(data=data)
            return message.generate()
        except:
            return "Не удалось найти аниме по вашему запросу"
