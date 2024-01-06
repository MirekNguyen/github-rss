import sys

import requests


def latest_release(repository):
    response = requests.get(
        f"https://api.github.com/repos/{repository}/releases/latest"
    )
    if response.status_code != 200:
        print("Error: Could not find the repository.")
        sys.exit(1)
    return response.json()


def print_latest_release(data):
    print(data["html_url"])
    print(data["published_at"])
    print(data["tag_name"])
    print(data["name"])
    print(data["prerelease"])
    print(data["body"])
data = latest_release("neovim/neovim")
print_latest_release(data)
