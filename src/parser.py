import requests
from endpoints import GET_RANDOM_ANIME_URL, GET_ANIME_INFO_URL, SEARCH_ANIME_URL
from headers import HEADERS
# /?search={name}'

def fetch_random_anime_data():
    try:
        response = requests.get(GET_RANDOM_ANIME_URL, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data
    except (requests.RequestException, ValueError):
        return None


def fetch_anime_info(name: str):
    try:
        response = requests.get(f"{SEARCH_ANIME_URL}/?search={name}", headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data
    except (requests.RequestException, ValueError):
        return None


def get_random_anime():
    data = fetch_random_anime_data()
    anime = data[0]
    random_anime_name = anime.get("russian")
    random_anime_url = anime.get("url")
    random_anime_score = anime.get("score")
    random_anime_episodes = anime.get("episodes")
    return (
        f"Название аниме: {random_anime_name}\n\n"
        f"Эпизоды: {random_anime_episodes}\n\n"
        f"Оценка аниме: {random_anime_score}\n\n"
        f"Ссылка: https://shikimori.one{random_anime_url}\n\n"
    )


def get_anime_info(name):
    data = fetch_anime_info(name)
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
