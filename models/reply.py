import requests
from .classes import bcolors, Times

class Reply:
    stand_header = {"Content-Type": "application/x-www-form-urlencoded"}

    def __init__(self, client) -> None:
        self.token = client.token
        self.username = client.username

    def sendReply(self, postid:int, message:str, from_:str, nsfw:bool=False):
        resp = requests.post(
            "https://bubblez.app/api/v1/reply/send",
            data={
                "token": self.token,
                "reply": message,
                "postid": postid,
                "from": from_,
                "nsfw": nsfw
            }, 
            headers=self.stand_header
        )
        if resp.ok:
            try:
                return resp.json()
            except:
                print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Something whent wrong with: reply\'s/send.. Status_code:", resp.status_code, bcolors.ENDC)
                print(f"{bcolors.WARNING} Content: ", resp.content, bcolors.ENDC)
                return False 
        return False

    def deleteReply(self, replyid):
        resp = requests.post(
            "https://bubblez.app/api/v1/reply/delete",
            data={
                "token": self.token,
                "replyid": replyid,
                "confirm": "true"
            }, headers=self.stand_header
        )
        if resp.ok:
            try:
                return resp.json()
            except:
                print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Something whent wrong with: reply\'s/delete.. Status_code:", resp.status_code, bcolors.ENDC)
                print(f"{bcolors.WARNING} Content: ", resp.content, bcolors.ENDC)
                return False 
        return False
    
    def editReply(self, replyid:int, new_message:str):
        resp = requests.post(
            "https://bubblez.app/api/v1/reply/edit",
            data={
                "token": self.token,
                "replyid": replyid,
                "reply": new_message
            }, headers=self.stand_header
        )
        if resp.ok:
            try:
                return resp.json()
            except:
                print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Something whent wrong with: reply\'s/edit.. Status_code:", resp.status_code, bcolors.ENDC)
                print(f"{bcolors.WARNING} Content: ", resp.content, bcolors.ENDC)
                return False 
        return False
