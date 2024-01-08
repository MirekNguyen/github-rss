"""Tools class for Github API"""
import requests


class Tools:
    """Tools class for Github API"""
    @staticmethod
    def get_limits(headers):
        """Get the rate limit of the Github API"""
        response = requests.get("https://api.github.com/rate_limit", headers=headers, timeout=5)
        return response.json()

    @staticmethod
    def sort_list_by(lst, key, reverse=True):
        """Sort a list of dictionaries by a key"""
        return sorted(lst, key=lambda x: x[key], reverse=reverse)
