
from .Methods import Methods
from .Url import Url

ENDPOINT = "http://192.168.2.7:8080/api/v2"
STAND_HEADER = {"Content-Type": "application/json"}

class Endpoints:
    class Posts:
        def get(postid:str, replies:bool=True) -> Url:
            return Url(
                url = ENDPOINT + "/posts/get",
                method = Methods.GET(),
                params = {
                    "postid": postid,
                    "replies": replies
                },
                headers=STAND_HEADER,
                json={},
                )
        
        def getAll(replies:bool=False) -> Url:
                return Url(
                    url = ENDPOINT + "/posts/get/all",
                    method = Methods.GET(),
                    params = {
                        "replies": replies
                    },
                    headers=STAND_HEADER,
                    json={},
                )

        def send(content:str, locked:bool=False, nsfw:bool=False) -> Url:
            return Url(
                url = ENDPOINT + "/posts/send",
                headers=STAND_HEADER,
                params={},
                method=Methods.POST(),
                json={
                    "content": content,
                    "locked": locked, 
                    "nsfw": nsfw
                }
            )

        def delete(postid:str) -> Url:
            return Url(
                url = ENDPOINT + "/posts/delete",
                headers=STAND_HEADER,
                params={"postid": postid},
                method=Methods.POST(),
                json={}
            )

        def edit(postid:str, locked: bool = None, nsfw: bool = None, content: str = None) -> Url:
            json = {}
            if locked != None: json["locked"] = locked
            if nsfw != None: json["nsfw"] = nsfw
            if content != None: json["content"] = content

            if json == {}:
                return False

            return Url(
                url = ENDPOINT + "/posts/edit",
                headers = STAND_HEADER,
                json = json,
                method = Methods.POST(),
                params = {
                    "postid": postid
                }
            )
    
        def lock(postid:str, locked:bool=True) -> Url:
            if locked == None: 
                raise Exception("locked can not be None")

            return Url(
                url = ENDPOINT + "/posts/edit",
                headers=STAND_HEADER,
                json={"postid": postid, "locked": locked},
                method=Methods.POST(),
                params={}
            )

    class Blogs:
        def getLatest() -> Url:
            return Url(
                url= ENDPOINT + "/blogs/getLatest",
                method= Methods.GET(),
                json={},
                params={},
                headers=STAND_HEADER
            )
        
        def get(blogid:int) -> Url:
            return Url(
                url = ENDPOINT + "/blogs/get",
                method = Methods.GET(),
                json = {},
                params = {
                    "blogid": blogid
                },
                headers = STAND_HEADER
            )

        def getAll(limit:int=10) -> Url:
            return Url(
                url = ENDPOINT + "/blogs/get/all",
                method = Methods.GET(),
                json = {},
                params = {
                    "limit": limit
                },
                headers = STAND_HEADER
            )
            

    class Replies:
        def get(replyid: int) -> Url:
            return Url(
                url = ENDPOINT + "/replies/get",
                method = Methods.GET(),
                json = {},
                params = {
                    "replyid": replyid
                },
                headers = STAND_HEADER
            )
            
        def send(postid:str, content: str, locked : bool = False, nsfw: bool = False) -> Url:
            json = {}
            if locked != None: json["locked"] = locked
            if nsfw != None: json["nsfw"] = nsfw
            if content != None: json["content"] = content

            if json == {}: return False

            return Url(
                url = ENDPOINT + "/replies/send",
                method = Methods.POST(),
                json = json,
                params = {
                    "postid": postid
                },
                headers = STAND_HEADER
            )

        def delete(replyid:int) -> Url:
            return Url(
                url = ENDPOINT + "/replies/delete",
                method = Methods.POST(),
                json = {},
                params = {
                    "replyid": replyid
                },
                headers = STAND_HEADER
            )

        def edit(replyid:int, content: str, locked: bool = None, nsfw: bool = None) -> Url:
            json = {}
            if locked != None: json["locked"] = locked
            if nsfw != None: json["nsfw"] = nsfw
            if content != None: json["content"] = content
            
            if json == {}: return False

            return Url(
                url = ENDPOINT + "/replies/edit",
                method = Methods.POST(),
                json = json,
                params = {
                    "replyid": replyid
                },
                headers = STAND_HEADER
            )


    
    class Users:
        def get(username: str = None, displayname: str = None) -> Url:
            if username == None and displayname == None:
                raise BaseException("username or displayname is required")

            params = {}
            
            if username != None: params["username"] = username
            if displayname != None: params["displayname"] = displayname

            return Url(
                url = ENDPOINT + "/users/get",
                method = Methods.GET(),
                json = {},
                params = params,
                headers = STAND_HEADER
            )
        
        def ping() -> Url:
            return Url(
                url = ENDPOINT + "/users/ping",
                method = Methods.GET(),
                json = {},
                params = {},
                headers = STAND_HEADER
            )
