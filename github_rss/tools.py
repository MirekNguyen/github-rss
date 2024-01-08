"""Tools class for Github API"""
import requests


class Tools:
    """Get the rate limit of the Github API"""
    @staticmethod
    def get_limits(headers):
        response = requests.get("https://api.github.com/rate_limit", headers=headers, timeout=5)
        return response.json()
    @staticmethod
    def sort_list_by(list, key, reverse=True):
        return sorted(list, key=lambda x: x[key], reverse=reverse)
