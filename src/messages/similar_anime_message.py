from api import ShikimoriApiClient
from messages.anime_message import AnimeMessage


class SimilarAnimeMessage:
    client = ShikimoriApiClient

    def __init__(self, client: ShikimoriApiClient):
        self.client = client

    async def generate(self, anime_id: int):
        try:
            data = await self.client.get_similar_anime(anime_id=anime_id)
            message = AnimeMessage(data=data)
            return message.generate_similar()
        except:
            return "Нет похожих аниме или неправильно использована команда"
