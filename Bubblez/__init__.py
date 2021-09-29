from .models.user import User as user 
from .models.reply import Reply as reply
from .models.post import Post as post
from .models.blog import Blog as blog

class Bubblez:
    stand_header = {"Content-Type": "application/x-www-form-urlencoded"}

    def __init__(self, username, token) -> None:
        self.user = self.User(username, token)
        self.post = self.Post(token)
        self.reply = self.Reply(token, username)
        self.blog = self.Blog(username, token)
        self.token = token 
        self.username = username 

    class User(user):
        pass 
    
    class Reply(reply):
        pass 

    class Post(post):
        pass 

    class Blog(blog):
        pass 