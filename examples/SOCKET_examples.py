from Bubblez import Bubblez
from Bubblez.socket import Socket, Events, classes


client = Bubblez("Your token", True, True)
socket = Socket(client)


@socket.on(Events.NewLike)
def new_like(type, user: classes.User, post: classes.Post):
    print(type, user.username, post.message)
    "Do Your thing"
    
@socket.on(Events.NewPost)
def new_post(post: classes.Post):
    print(post.json())
    "Do Your thing"

@socket.on(Events.NewFollower)
def new_fol(user: classes.User):
    print(user.json())
    "Do Your thing"

@socket.on(Events.NewReply)
def new_fol(post: classes.Post, reply: classes.Reply):
    print(post.message, reply.message)
    "Do Your thing"

@socket.on(Events.UnFollowed)
def un_fol(user: classes.User):
    print(user.json())
    "Do Your thing"

socket.connect()