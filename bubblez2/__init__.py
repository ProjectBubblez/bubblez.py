
from .models.urls.Endpoints import Endpoints
from .models.Users import Users
from .models.Posts import Posts
from .models.Replies import Replies

class Bubblez:    
    
    def __init__(self, token: str, useCanary:bool=False, verbose:bool=False) -> None:
        self.token = token
        self.useCanary = useCanary
        self.verbose = verbose

        self.users = Users(client=self)
        self.posts = Posts(client=self)
        self.replies = Replies(client=self)
    
