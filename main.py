"""Main script to generate RSS feed from Github releases."""
import sys

from github_rss.feed_generator import Feed
from github_rss.release import Release
from github_rss.repository import Repository
from github_rss.tools import Tools
from github_rss.settings_loader import SettingsLoader

settings = SettingsLoader()
env = settings.load_env()
USER = env.get("USER")
GITHUB_TOKEN = env.get("GITHUB_TOKEN")
OUT_DIR = env.get("OUT_DIR")

if GITHUB_TOKEN is None:
    print("GITHUB_TOKEN is not set.")
    sys.exit(1)
if USER is None:
    print("USER is not set.")
    sys.exit(1)
if OUT_DIR is None:
    print("OUT_DIR is not set.")
    sys.exit(1)

DEFAULT_HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

r = Release()
repository = Repository()
feed = Feed()

starred = repository.starred_repositories(USER, DEFAULT_HEADERS)
releases = r.latest_release_list(starred, DEFAULT_HEADERS)
sorted_releases = Tools.sort_list_by(lst=releases, key="published_at", reverse=False)
fe_list = r.feedgen_format(sorted_releases)

feed.generate_fg(
    feed_id=f"https://api.github.com/users/{USER}",
    title="Github RSS",
    subtitle="Github RSS",
    link=f"https://api.github.com/users/{USER}",
)
if feed.generate_rss(fe_list, OUT_DIR):
    print("RSS feed generated.")
else:
    print("RSS feed generation failed.")
    sys.exit(1)
