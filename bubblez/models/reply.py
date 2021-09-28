import requests

class Reply:
    stand_header = {"Content-Type": "application/x-www-form-urlencoded"}

    def __init__(self, token, username) -> None:
        self.token = token
        self.username = username

    def send(self, postid:int, message:str, from_:str, nsfw:bool=False):
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
                print("Iets ging fout met reply\'s/send.. Status_code:", resp.status_code)
                print("Content: ", resp.content)
                return False 
        return False

    def delete(self, replyid, confirm:bool=True):
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
                print("Iets ging fout met reply\'s/delete.. Status_code:", resp.status_code)
                print("Content: ", resp.content)
                return False 
        return False