import requests
from endpoints import GET_RANDOM_ANIME_URL
from headers import HEADERS


def fetch_random_anime_data():
    try:
        response = requests.get(GET_RANDOM_ANIME_URL, headers=HEADERS)
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

# def get_anime_preview():
#     anime_info = requests.get(GET_ANIME_INFO_URL, headers=HEADERS)
#     prewiev_data = anime_info.json()
#     image_path = prewiev_data["image"]["original"]
#     return f"https://shikimori.one{image_path}"


# def get_anime_name():
#     anime_info = requests.get(GET_ANIME_INFO_URL, headers=HEADERS)
#     anime_data = anime_info.json()
#     anime_data_name = anime_data.get("russian")
#     return f"Название аниме: {anime_data_name}"


# def get_anime_score():
#     anime_info = requests.get(GET_ANIME_INFO_URL, headers=HEADERS)
#     anime_data = anime_info.json()
#     anime_data_score = anime_data.get("score")
#     return f"Оценка: {anime_data_score}"


# def get_anime_episodes():
#     anime_info = requests.get(GET_ANIME_INFO_URL, headers=HEADERS)
#     anime_data = anime_info.json()
#     anime_data_episodes = anime_data.get("episodes")
#     return f"Эпизоды: {anime_data_episodes}"

