from aiogram.utils.markdown import bold


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

        return "\n".join(
            [
                f"{bold("Название аниме:")} {random_anime_name}",
                f"{bold("Количество эпизодов:")} {random_anime_episodes}",
                f"{bold("Оценка аниме:")} {random_anime_score}",
                f"{bold("Ссылка:")} https://shikimori.one{random_anime_url}",
            ]
        )
