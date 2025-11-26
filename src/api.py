import aiohttp
from aiocache import cached


class ShikimoriApiClient:
    api_url: str

    def __init__(self, api_url: str = "https://shikimori.one"):
        self.api_url = api_url

    async def get_random_anime(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    self._get_endpoint("/api/animes"), params={"order": "random"}
                ) as res:
                    return await res.json()
        except Exception:
            return None

    @cached(ttl=300)
    async def search_for_anime(self, name: str):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    self._get_endpoint("/api/animes"), params={"search": name}
                ) as res:
                    return await res.json()
        except Exception:
            return None

    async def get_similar_anime(self, anime_id: int):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    self._get_endpoint(f"/api/animes{anime_id}/similar"),
                    params={"similar": anime_id},
                ) as res:
                    return await res.json()
        except Exception:
            return None

    def _get_endpoint(self, path: str):
        return f"{self.api_url}{path}"
