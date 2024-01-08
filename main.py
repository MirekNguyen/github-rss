import os
import sys
from datetime import datetime

import pytz
from dotenv import load_dotenv

from github_rss.feed_generator import Feed
from github_rss.release import Release
from github_rss.repository import Repository
from github_rss.tools import Tools

load_dotenv()
USER = "mireknguyen"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if GITHUB_TOKEN is None:
    print("GITHUB_TOKEN is not set.")
    sys.exit(1)

DEFAULT_HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

r = Release()
repository = Repository()
starred = repository.starred_repositories(USER, DEFAULT_HEADERS)

releases = r.latest_release_list(starred, DEFAULT_HEADERS)
sorted_releases = Tools.sort_list_by(list=releases, key="published_at", reverse=False)
feed = Feed()
fe_list = map(
    lambda release: {
        "id": release["html_url"],
        "title": release["name"],
        "link": release["html_url"],
        "description": release["body"],
        "pubDate": pytz.timezone("Etc/UTC").localize(
            datetime.strptime(release["published_at"], "%Y-%m-%dT%H:%M:%SZ")
        ),
    },
    sorted_releases,
)
feed.generate_fg(
    feed_id=f"https://api.github.com/users/{USER}",
    title="Github RSS",
    subtitle="Github RSS",
    link=f"https://api.github.com/users/{USER}",
)
if feed.generate_rss(fe_list, "out/rss.xml"):
    print("RSS feed generated.")
else:
    print("RSS feed generation failed.")
    sys.exit(1)
