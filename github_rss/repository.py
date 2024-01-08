"""Get the latest release of a repository or a list of repositories"""
import requests

class Repository:
    """Get the latest release of a repository or a list of repositories"""
    def starred_repositories(self, username, headers):
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
            for item in current_page:
                starred.append(item['full_name'])
            if len(current_page) < per_page:
                break
            page += 1
        return starred
