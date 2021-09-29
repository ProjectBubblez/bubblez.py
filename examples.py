from bubblez import Bubblez

# The setup for the Python Bubblez API (Unofficial)!

client = Bubblez("foo","Your Api token")


def posts():
    # make a post: 
    client.post.send(
        message="The best Website is:...",
        from_="This Beauti Python Program",
        locked=True or False,
        nsfw=True or False,
    )

    # delete a post:
    client.post.delete(postid=...)

    # get a post:
    client.post.get(postid=...)

    # get the latest post or only the id of the post
    client.post.latest(postid_only=True or False)

    # and lock it with.. 
    client.post.lock(postid=..., locked=True or False)


def user():

    # ping / check the users token:
    client.user.check()
    client.user.ping()

    # more is in the making but still cooking.

def replys():

    # send a reply:
    client.reply.send(
        postid=..., 
        message="The beauti reply on this beauti message..", 
        from_="from Foo", 
        nsfw=True or False
    )

    # delete a reply:
    client.reply.delete(
        replyid=...
    )

def Future_Plans():

    '''
    highest prio's:
        Making a cache system to remember all the id's.



    last prio: making a UI

    '''

