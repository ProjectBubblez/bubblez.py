from Bubblez import Bubblez

# The setup for the Python Bubblez API (Unofficial)!

client = Bubblez("foo","Your Api token")


def posts():
    # make a post: 
    client.post.sendPost(
        message="The best Website is:...",
        from_="This Beauti Python Program",
        locked=True or False,
        nsfw=True or False,
    )

    # delete a post:
    client.post.deletePost(postid=...)

    # get a post:
    client.post.getPost(postid=...)

    # get the latest post or only the id of the post
    client.post.getLatestPost(postid_only=True or False)

    # and lock it with.. 
    client.post.lockPost(postid=..., locked=True or False)


def user():

    # ping / check the users token:
    client.user.checkUser()
    client.user.pingUser()
    client.user.getUser()

    # more is in the making but still cooking.

def replys():

    # send a reply:
    client.reply.sendReply(
        postid=..., 
        message="The beauti reply on this beauti message..", 
        from_="from Foo", 
        nsfw=True or False
    )

    # delete a reply:
    client.reply.deleteReply(
        replyid=...
    )

def blogs():

    # Get latest blog:
    client.blog.getlatest()


def Future_Plans():

    '''
    highest prio's:
        Making a cache system to remember all the id's.



    last prio: making a UI

    '''






