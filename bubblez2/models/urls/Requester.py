from .Url import Url
import requests

class Requester:
    def __init__(self, client) -> None:
        self.client = client

    def request(self, url: Url):
        url = url.addToken(self.client.token)
        if not url.authenticated:
            raise Exception("Could not authenticated the request")

        return requests.request(url.method, url=url.url, params=url.params, json=url.json, headers=url.headers)
