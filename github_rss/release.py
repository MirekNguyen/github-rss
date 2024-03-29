"""Get the latest release of a repository or a list of repositories"""
from datetime import datetime

import pytz
import requests


class Release:
    """Get the latest release of a repository or a list of repositories"""

    def latest_release(self, repository, headers):
        """Get the latest release of a repository"""
        response = requests.get(
            f"https://api.github.com/repos/{repository}/releases/latest",
            headers=headers,
            timeout=5,
        )
        if response.status_code == 404:
            return {
                "error": True,
                "message": f"{response.status_code}: Repository release not found.",
            }
        if response.status_code == 403:
            return {
                "error": True,
                "message": f"{response.status_code}: API rate limit exceeded.",
            }
        if response.status_code != 200:
            return {"error": True, "message": f"{response.status_code}: Unknown error."}
        return response.json()

    def latest_release_list(self, repository_list, headers):
        """Get the latest release of a list of repositories"""
        details = []
        for release_name in repository_list:
            repository_release = self.latest_release(release_name, headers)
            if repository_release.get("error"):
                continue
            release = {
                "name": release_name,
                "tag_name": repository_release["tag_name"],
                "published_at": repository_release["published_at"],
                "html_url": repository_release["html_url"],
                "body": repository_release["body"],
            }
            details.append(release)
        return details

    def feedgen_format(self, releases):
        """Format the release details to feedgen format"""
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
            releases,
        )
        return fe_list
