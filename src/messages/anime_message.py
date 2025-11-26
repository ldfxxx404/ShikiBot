from aiogram.utils.markdown import bold
from random import choice


class AnimeMessage:
    data: list[dict]

    def __init__(self, data: list[dict]):
        self.data = data

    def generate(self):
        anime = self.data[0]
        random_anime_name = anime["russian"]
        random_anime_url = anime["url"]
        random_anime_score = anime["score"]
        random_anime_episodes = anime["episodes"]
        random_anime_id = anime["id"]
        return "\n".join(
            [
                f"{bold("Количество эпизодов:")} {random_anime_episodes}",
                f"{bold("Название аниме:")} {random_anime_name}",
                f"{bold("Оценка аниме:")} {random_anime_score}",
                f"{bold("ID аниме:")} {random_anime_id}",
                f"{bold("Ссылка:")} https://shikimori.one{random_anime_url}",
            ]
        )

    def generate_similar(self):
        anime = choice(self.data)
        similar_anime_name = anime["russian"]
        similar_anime_url = anime["url"]
        similar_anime_score = anime["score"]
        similar_anime_episodes = anime["episodes"]
        similar_anime_id = anime["id"]
        return "\n".join(
            [
                f"{bold("Название аниме:")} {similar_anime_name}",
                f"{bold("Количество эпизодов:")} {similar_anime_episodes}",
                f"{bold("Оценка аниме:")} {similar_anime_score}",
                f"{bold("ID аниме:")} {similar_anime_id})",
                f"{bold("Ссылка:")} https://shikimori.one{similar_anime_url}",
            ]
        )
