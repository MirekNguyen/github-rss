import os
from dotenv import load_dotenv

class SettingsLoader:
    def load_env(self)-> dict:
        load_dotenv()
        return {
            "GITHUB_TOKEN": self.__env("GITHUB_TOKEN"),
            "USER": self.__env("USER"),
        }
    def __env(self, key: str):
        return os.environ.get(key, os.getenv(key))
