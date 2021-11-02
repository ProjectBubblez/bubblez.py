from .models.user import User as user 
from .models.reply import Reply as reply
from .models.post import Post as post
from .models.blog import Blog as blog
from .sockets import Sockets as socket, Events

class Bubblez:
    stand_header = {"Content-Type": "application/x-www-form-urlencoded"}

    def __init__(self, username, token, verbose=False) -> None:
        self.user = self.User(self)
        self.post = self.Post(self)
        self.reply = self.Reply(self)
        self.blog = self.Blog(self)
        self.token = token 
        self.username = username
        self.verbose = verbose

    class User(user):
        pass 
    
    class Reply(reply):
        pass 

    class Post(post):
        pass 

    class Blog(blog):
        pass 

class Sockets(socket):
    class Events(Events):
        pass 
    pass