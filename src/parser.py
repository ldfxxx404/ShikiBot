import requests


class Anime:

    def __init__(self, random_url, search_url, headers):
        self.random_url = random_url
        self.search_url = search_url
        self.headers = headers

    def _fetch_random_anime_data(self):
        try:
            response = requests.get(self.random_url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            return data
        except (requests.RequestException, ValueError):
            return None

    def _fetch_anime_info(self, title_name: str):
        try:
            response = requests.get(
                f"{self.search_url}/?search={title_name}", headers=self.headers
            )
            response.raise_for_status()
            data = response.json()
            return data
        except (requests.RequestException, ValueError):
            return None

    def get_random_anime(self):
        data = self._fetch_random_anime_data()
        if not data:
            return "Unable to get information about the anime. Please try again later."

        anime = data[0]
        random_anime_name = anime["russian"]
        random_anime_url = anime["url"]
        random_anime_score = anime["score"]
        random_anime_episodes = anime["episodes"]

        return (
            f"Название аниме: {random_anime_name}\n\n"
            f"Эпизоды: {random_anime_episodes}\n\n"
            f"Оценка аниме: {random_anime_score}\n\n"
            f"Ссылка: https://shikimori.one{random_anime_url}\n\n"
        )

    def get_anime_info(self, title_name):
        data = self._fetch_anime_info(title_name)
        if not data:
            return f"The anime '{title_name}' could not be found. Please check the title and try again."

        anime = data[0]
        anime_name = anime["russian"]
        anime_url = anime["url"]
        anime_score = anime["score"]
        anime_episodes = anime["episodes"]

        return (
            f"Название аниме: {anime_name}\n\n"
            f"Эпизоды: {anime_episodes}\n\n"
            f"Оценка аниме: {anime_score}\n\n"
            f"Ссылка: https://shikimori.one{anime_url}\n\n"
        )
