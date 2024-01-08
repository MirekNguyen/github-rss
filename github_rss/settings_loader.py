import os
from dotenv import load_dotenv
import argparse

class SettingsLoader:
    def load_env(self)-> dict:
        load_dotenv()
        parser = argparse.ArgumentParser(description="Github RSS")
        parser.add_argument("-o", "--output", action="store", help="Output (required)")
        args = parser.parse_args()

        return {
            "GITHUB_TOKEN": self.__env("GITHUB_TOKEN"),
            "USER": self.__env("USER"),
            "OUT_DIR": args.output
        }
    def __env(self, key: str):
        return os.environ.get(key, os.getenv(key))
