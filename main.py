import os
import sys

from dotenv import load_dotenv

from github_rss.release import Release
from github_rss.repository import Repository
from github_rss.tools import Tools

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if GITHUB_TOKEN is None:
    print("GITHUB_TOKEN is not set.")
    sys.exit(1)

DEFAULT_HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

release = Release()
repository = Repository()
starred = repository.starred_repositories("mireknguyen", DEFAULT_HEADERS)

releases = release.latest_release_list(starred, DEFAULT_HEADERS)
sorted_releases = Tools.sort_list_by(releases, "published_at")
print(sorted_releases)
# print(Tools.get_limits(DEFAULT_HEADERS)["rate"])

# print(release.latest_release("mireknguyen/mirekng-homepage", DEFAULT_HEADERS))
# repository.starred_repositories("mireknguyen", DEFAULT_HEADERS)
# print(starred_repositories("mireknguyen"))
# print(latest_release("mireknguyen/mirekng-homepage"))

# fe = {
#     id: id,
#     title: title,
#     link: link,
#     description: description,
#     pubDate: pub_date,
# }
# fe_list = [ fe1, fe2, fe3]

