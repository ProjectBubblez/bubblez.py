import requests

stand_header = {"Content-Type": "application/x-www-form-urlencoded"}

class Post:
    def __init__(self, token) -> None:
        self.token = token

    def delete(self, postid:int):
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
                print("Iets ging fout met post/delete.. Status_code:", resp.status_code)
                print("Content: ", resp.content)
                return False 
                
        return False 

    def get(self, postid:int):
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
                print("Iets ging fout met post/get.. Status_code:", resp.status_code)
                print("Content: ", resp.content)
                return False 

        return False

    def send(self,message:str, from_:str, locked:bool=False, nsfw:bool=False ):
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
                print("Iets ging fout met post/send.. Status_code:", resp.status_code)
                print("Content: ", resp.content)
                return False 
                
        return False
    
    def latest(self, postid_only:bool=False):
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
                    print("Iets ging fout met post/latest.. Status_code:", resp.status_code)
                    print("Content: ", resp.content)
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
                print("Iets ging fout met post/latest id_only.. Status_code:", resp.status_code)
                print("Content: ", resp.content)
                return False 
                
        return False

    def lock(self, postid:int, locked:bool=True):
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
                print("Iets ging fout met post/lock.. Status_code:", resp.status_code)
                print("Content: ", resp.content)
                return False 
                
        return False


    
