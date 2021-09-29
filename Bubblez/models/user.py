import requests
from requests.api import head
from .post import Post
from .reply import Reply

stand_header = {"Content-Type": "application/x-www-form-urlencoded"}

class User:
    last_request = None 
    stand_header = {"Content-Type": "application/x-www-form-urlencoded"}

    def __init__(self, username, token) -> None:
        self.username = username
        self.token = token
    
    def json(self):
        return {
            "username": self.username,
            "token": self.token,
            "last_request": self.last_request
        }
    
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
                print("Something whent wrong with: user/check.. Status_code:", resp.status_code)
                print("Content: ", resp.content)
                return False 
        return False

    def pingUser(self):
        if not self.token:
            raise ValueError("Missing token!")
        print("Ping!")
        resp = requests.post(
            "https://bubblez.app/api/v1/user/ping", 
            data={
                "token": self.token
            }, 
            headers=self.stand_header
        )
        if resp.ok:
            print("Pong!")
       
            self.username = resp.json()['username']
            print(f"username: {self.username}")
            print("everything is good! , status code: 200")
            return resp
            
        else:
            print("Something when\'t wrong! | status code:", resp.status_code)
            print("content:", resp.content)
            return False  