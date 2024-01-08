"""Module for repository related functions"""
import requests


class Repository:
    """Class for repository related functions"""

    def starred_repositories(self, username, headers):
        """Get starred repositories from username"""
        starred = []
        page = 1
        per_page = 30
        while True:
            current_page = self.starred_repositories_by_page(
                username, headers, page=page, per_page=per_page
            )
            if current_page[0].get("error"):
                return current_page
            for item in current_page:
                starred.append(item["full_name"])
            if len(current_page) < per_page:
                break
            page += 1
        return starred

    def starred_repositories_by_page(
        self, username: str, headers, page: int = 1, per_page: int = 100
    ):
        """Get starred repositories from username by page"""
        params = {
            "page": page,
            "per_page": per_page,
        }
        response = requests.get(
            f"https://api.github.com/users/{username}/starred",
            headers=headers,
            params=params,
            timeout=5
        )
        if response.status_code != 200:
            return [{
                "error": True,
                "message": response.json()["message"],
            }]
        page_data = response.json()
        return page_data
