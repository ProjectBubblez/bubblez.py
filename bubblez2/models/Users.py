import datetime

from ..components.Post import Post
from ..components.Reply import Reply
from ..components.User import User

from ..models.urls.Endpoints import Endpoints
from ..models.urls.Requester import Requester


class Users:
    
    def __init__(self, client) -> None:
        self.client = client
        self.requester = Requester(self.client)

    def get():
        pass 

    def ping():
        pass 

    def check():
        pass 
