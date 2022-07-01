
class Url:
    def __init__(self, url:str, method: str, params:dict, headers:dict, json:dict) -> None:
        self.url = url
        self.headers = headers
        self.json = json
        self.method = method
        self.params = params
        self.authenticated = False 

    def addToken(self, token:str):
        self.headers['token'] = token
        self.authenticated = True

        return self 
