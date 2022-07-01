import datetime

from ..components.Post import Post
from ..components.Reply import Reply
from ..components.User import User

from ..models.urls.Endpoints import Endpoints
from ..models.urls.Requester import Requester


class Replies:
    
    def __init__(self, client) -> None:
        self.client = client
        self.requester = Requester(self.client)

    def get():
        pass 

    def send():
        pass 

    def delete():
        pass 

    def edit():
        pass 

    def lock():
        pass 
