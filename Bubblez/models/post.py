import requests
from .classes import bcolors, Times

stand_header = {"Content-Type": "application/x-www-form-urlencoded"}

class Post:
    def __init__(self, client) -> None:
        self.token = client.token
        self.username = client.username

    def deletePost(self, postid:int):
        resp = requests.post(
            "https://bubblez.app/api/v1/post/delete", 
            data={
                "id":postid,
                "token": self.token,
                "confirm": True
            },
            headers=stand_header
        )
        if resp.ok:
            try:
                return resp.json()
            except:
                print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Something whent wrong with: post/delete.. Status_code:", resp.status_code, bcolors.ENDC)
                print(f"{bcolors.WARNING} Content: ", resp.content, bcolors.ENDC)
                return False 
                
        return False 

    def getPost(self, postid:int):
        resp = requests.post(
            "https://bubblez.app/api/v1/post/get",
            data={
                "token": self.token,
                "postid": postid
            },
            headers=stand_header
        )
        if resp.ok:
            try:
                return resp.json()
            except:
                print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Something whent wrong with: post/get.. Status_code:", resp.status_code, bcolors.ENDC)
                print(f"{bcolors.WARNING} Content: ", resp.content, bcolors.ENDC)
                return False 

        return False

    def sendPost(self,message:str, from_:str, locked:bool=False, nsfw:bool=False ):
        resp = requests.post(
            "https://bubblez.app/api/v1/post/send",
            data={
                "token": self.token,
                "post": message,
                "from": from_,
                'locked': locked ,
                "nsfw": nsfw 
            }
            ,headers=stand_header
        )
        if resp.ok:
            try:
                return resp.json()
            except:
                print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Something whent wrong with: post/send.. Status_code:", resp.status_code, bcolors.ENDC)
                print(f"{bcolors.WARNING} Content: ", resp.content, bcolors.ENDC)
                return False 
                
        return False
    
    def getLatestPost(self, postid_only:bool=False):
        if not postid_only:
            resp = requests.post(
                "https://bubblez.app/api/v1/post/latest",
                data={
                    "token": self.token
                },
                headers=stand_header
            )
            if resp.ok:
                try:
                    return resp.json()
                except:
                    print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Something whent wrong with: post/getlatest.. Status_code:", resp.status_code, bcolors.ENDC)
                    print(f"{bcolors.WARNING} Content: ", resp.content, bcolors.ENDC)
                    return False 
                    
            return False
        resp = requests.post(
            "https://bubblez.app/api/v1/post/latest",
            data={
                "token": self.token
            },
            headers=stand_header
        )
        if resp.ok:
            try:
                return resp.json()
            except:
                print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Something whent wrong with: post/getlatest.. Status_code:", resp.status_code, bcolors.ENDC)
                print(f"{bcolors.WARNING} Content: ", resp.content, bcolors.ENDC)
                return False 
                
        return False

    def lockPost(self, postid:int, locked:bool=True):
        resp = requests.post(
            "https://bubblez.app/api/v1/post/lock",
            data={
                "postid":postid,
                "token": self.token,
                "togglelock": locked
            },
            headers=stand_header
        )
        if resp.ok:
            try:
                return resp.json()
            except:
                print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Something whent wrong with: post/lock.. Status_code:", resp.status_code, bcolors.ENDC)
                print(f"{bcolors.WARNING} Content: ", resp.content, bcolors.ENDC)
                return False 
                
        return False
    
    def editPost(self, postid:int, new_message:str):
        resp = requests.post(
            "https://bubblez.app/api/v1/post/edit",
            data={
                "postid": postid,
                "token": self.token,
                "post": new_message
            }
        )
        if resp.ok:
            try:
                return resp.json()
            except:
                print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Something whent wrong with: post/edit.. Status_code:", resp.status_code, bcolors.ENDC)
                print(f"{bcolors.WARNING} Content: ", resp.content, bcolors.ENDC)
                return False 
        return False 
    


    

