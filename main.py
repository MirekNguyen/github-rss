import sys

import requests
from dotenv import load_dotenv
import os

load_dotenv()
GITHUB_TOKEN=os.getenv("GITHUB_TOKEN")
DEFAULT_HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}
if GITHUB_TOKEN is None:
    print("GITHUB_TOKEN is not set.")
    sys.exit(1)
def latest_release(repository, headers = DEFAULT_HEADERS):
    response = requests.get(
        f"https://api.github.com/repos/{repository}/releases/latest",
        headers=headers
    )
    if response.status_code == 404:
        return {"error": True, "message": f"{response.status_code}: Repository release not found."}
    if response.status_code == 403:
        return {"error": True, "message": f"{response.status_code}: API rate limit exceeded."}
    if response.status_code != 200:
        return {"error": True, "message": f"{response.status_code}: Unknown error."}
    return response.json()

def get_limits(headers = DEFAULT_HEADERS):
    response = requests.get("https://api.github.com/rate_limit", headers=headers)
    return response.json()

def starred_repositories(username, headers = DEFAULT_HEADERS):
    starred = []
    page = 1
    per_page = 100
    while True:
        params = {
            'page': page,
            'per_page': per_page,
        }
        response = requests.get(
            f"https://api.github.com/users/{username}/starred",
            headers=headers,
            params=params,
        )
        if response.status_code != 200:
            return {"error": True, "message": f"{response.status_code}: Error getting starred repositories"}
        current_page = response.json()
        starred.extend(current_page)
        if len(current_page) < per_page:
            break
        page += 1

    details = []
    for release in starred:
        repository_release = latest_release(release['full_name'])
        if repository_release.get("error"):
            continue
        release_tag = repository_release['tag_name']
        details.extend(release_tag)
    return details


def print_latest_release(data):
    print(data["html_url"])
    print(data["published_at"])
    print(data["tag_name"])
    print(data["name"])
    print(data["prerelease"])
    print(data["body"])

print(starred_repositories("mireknguyen"))
limits = get_limits()
print(limits['rate'])
