from bubblez import Bubblez

# The setup for the Python Bubblez API (Unofficial)!

client = Bubblez("foo","Your Api token")

# All funcs for posts
def posts():
    # make a post: 
    client.post.send(
        message="The best Website is:...",
        from_="This Beauti Python Program",
        locked=True or False,
        nsfw=True or False,
    )

    # delete a post:
    client.post.delete("The best postid got!")

    # get a post:
    client.post.get("Again with a postid..")

    # get the latest post or only the id of the post
    client.post.latest(postid_only=True or False)

    # and lock it with.. 
    client.post.lock("postid..", locked=True or False)

# All funcs for User
def user():

    # ping / check the users token:
    client.user.check()
    client.user.ping()

    # more is in the making but still cooking.

# All funcs for reply's 
def replys():

    # send a reply:
    client.reply.send(
        postid="postid..", 
        message="The beauti reply on this beauti message..", 
        from_="from Foo", 
        nsfw=True or False
    )

    # delete a reply:
    client.reply.delete(
        replyid="U need some id?",
        confirm=True
    )

# Future plans:
def Future_Plans():

    '''
    highest prio's:
        Making a cache system to remember all the id's.



    last prio: making a UI

    '''






