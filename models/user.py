import requests
from .classes import bcolors, Times

stand_header = {"Content-Type": "application/x-www-form-urlencoded"}

class User:
    last_request = None 
    stand_header = {"Content-Type": "application/x-www-form-urlencoded"}

    def __init__(self, client) -> None:
        self.token = client.token
        self.username = client.username
    
    def json(self):
        return {
            "username": self.username,
            "token": self.token,
            "last_request": self.last_request
        }
    
    def getUser(self, username:str):
        resp = requests.post(
        "https://bubblez.app/api/v1/user/get",
        data={
            "token": self.token,
            "username": username
        },
        headers=self.stand_header
        )
        if resp.ok:
            try:
                return resp.json()
            except:
                print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Something whent wrong with: user\'s/get.. Status_code:", resp.status_code, bcolors.ENDC)
                print(f"{bcolors.WARNING} Content: ", resp.content, bcolors.ENDC)
                return False 
        return False
    
    def checkUser(self):
        resp = requests.post(
            "https://bubblez.app/api/v1/user/check",
            data={
                "token": self.token
            },
            headers=self.stand_header
        )
        if resp.ok:
            try:
                return resp.json()
            except:
                print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Something whent wrong with: user\'s/check.. Status_code:", resp.status_code, bcolors.ENDC)
                print(f"{bcolors.WARNING} Content: ", resp.content, bcolors.ENDC)
                return False 
        return False

    def pingUser(self):
        resp = requests.post(
            "https://bubblez.app/api/v1/user/ping", 
            data={
                "token": self.token
            }, 
            headers=self.stand_header
        )
        if resp.ok:
            self.username = resp.json()['username']
            print(f"{bcolors.OKGREEN}[Bubblez.py] {Times.log()} Setting username as: {self.username}", bcolors.ENDC)
            return resp.json()
        else:
            print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Something when\'t wrong! | status code:", resp.status_code)
            print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Raw content:", resp.content, bcolors.ENDC)
            return False  