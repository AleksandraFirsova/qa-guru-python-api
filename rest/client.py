import requests

from conf.config import get_base_url


class ClubClient:

    def __init__(self):
        self.base_url = get_base_url()

    def get_clubs(self, params=None):
        url = f"{self.base_url}/clubs/"
        return requests.get(url, params=params)
