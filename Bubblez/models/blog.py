import requests
from .classes import bcolors, Times

stand_header = {"Content-Type": "application/x-www-form-urlencoded"}

class Blog:
    def __init__(self, client) -> None:
        self.token = client.token
        self.username = client.username
    
    def getlatest(self):
        resp = requests.post(
            "https://bubblez.app/api/v1/blog/latest",
            data={
                "token": self.token
            }, headers=stand_header
        )
        if resp.ok:
            try:
                return resp.json()
            except:
                print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Something whent wrong with: blog/latest.. Status_code:", resp.status_code, bcolors.ENDC)
                print(f"{bcolors.WARNING} Content: ", resp.content, bcolors.ENDC)
                return False 
        return False