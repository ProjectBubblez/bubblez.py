import requests

stand_header = {"Content-Type": "application/x-www-form-urlencoded"}

class Blog:
    def __init__(self, username, token) -> None:
        self.token = token
        self.username = username
    
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
                print("Something whent wrong with: blog/latest.. Status_code:", resp.status_code)
                print("Content: ", resp.content)
                return False 
        return False