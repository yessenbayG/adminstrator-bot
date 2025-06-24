from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str # Токен для доступа к телеграм-боту


def load_config(path: str | None = None) -> TgBot:
    env = Env()
    env.read_env(path)
    return TgBot(token=env('BOT_TOKEN'))