from Bubblez import Bubblez, Sockets, Events
from Bubblez.sockets import Events

# The setup for the Python Bubblez API (Unofficial)!

client = Bubblez("foo","Your Api token")
socket = Sockets(client, verbose=True or False)

def posts():
    # make a post: 
    client.post.sendPost(
        message="The best Website is:...",
        from_="This Beauti Python Program",
        locked=True or False,
        nsfw=True or False,
    )
    response = {
        "200": "message sent",
        "post": "API is cool",
        "from": "API testing",
        "locked": "false",
        "pnsfw": "false",
        "postid": 522
    }   

    # delete a post:
    client.post.deletePost(postid=...)
    response = {
            "200": "reply 1473 has been deleted"
        }

    # get a post:
    client.post.getPost(postid=...)
    response = {
            "200": "Found post",
            "postid": "522",
            "username": "DarkMatter",
            "pfp": "https://i.imgur.com/jAOd5gE.png",
            "nsfw": "false",
            "content": "API is cool",
            "from": "API testing",
            "locked": "false",
            "edited": None,
            "post_date": "2021-07-30 12:18:31",
            "replies": [
                {
                    "replyid": "1473",
                    "username": "DarkMatter",
                    "pfp": "https://i.imgur.com/jAOd5gE.png",
                    "content": "Cool reply with the API",
                    "from": None,
                    "deleted": None,
                    "edit_date": None,
                    "reply_date": "2021-07-30 12:49:12"
                }
            ]
        }

    # get the latest post or only the id of the post
    client.post.getLatestPost(postid_only=True or False)
    response = {
        "200": "latest Post",
        "postid": "522"
    }

    # and lock it with.. 
    client.post.lockPost(postid=..., locked=True or False)
    response = {
        "200": "Post 522 has been locked"
    }

def user():

    # ping / check the users token:
    client.user.checkUser()
    response = {
            "200": "Found user",
            "uuid": None,  
            "username": "DarkMatter",
            "displayname": "DarkMatter",
            "email": "zakygames701@gmail.com",
            "pfp": "https://i.imgur.com/jAOd5gE.png",
            "banner": "https://i.imgur.com/1bZdeBF.png",
            "coins": "85",
            "rank": "founder",
            "eventr": "darkmatter",
            "patreon": "true",
            "booster": "true",
            "bio": "We don't know much about them, but we're sure DarkMatter is great.",
            "nsfw": "false",
            "dob": None,
            "pronoun": "hehim",
            "ban": None,
            "created_at": "2019-10-21 07:40:23",
            "last_posted": "2021-07-30 01:19:36",
            "posts": [
                {
                    "postid": "522",
                    "username": "DarkMatter",
                    "nsfw": "false",
                    "content": "API is cool",
                    "from": "API testing",
                    "locked": "false",
                    "edited": None,
                    "post_date": "2021-07-30 12:18:31"
                }
            ],
            "replies": [
                {
                    "replyid": "1473",
                    "postid": "522",
                    "username": "DarkMatter",
                    "nsfw": "false",
                    "content": "Cool reply with the API",
                    "from": "API testing",
                    "edited": None,
                    "reply_date": "2021-07-30 12:49:12"
                }
            ]
        }
    
    client.user.pingUser()
    response = {
            "200": "Pong",
            "username": "DarkMatter",
            "online_status": "2021-07-30 13:03:18"
        }


    client.user.getUser()
    response = {
            "200": "Found user",
            "uuid": None,
            "username": "embed",
            "displayname": "embed",
            "followers": 2,
            "pfp": "https://i.imgur.com/Md5C3uy.gif",
            "banner": None,
            "coins": "0",
            "rank": "founder",
            "eventr": "lgbt19",
            "patreon": "true",
            "booster": "true",
            "bio": "the best bubblez dev.",
            "nsfw": "false",
            "pronoun": "none",
            "ban": None,
            "created_at": "2019-10-22 12:04:01",
            "last_posted": None,
            "posts": [
                {
                    "postid": "280",
                    "username": "embed",
                    "nsfw": "false",
                    "content": "gamimg",
                    "from": None,
                    "locked": "false",
                    "edited": None,
                    "post_date": "2020-08-09 17:15:19"
                }
            ]
        }


def replys():

    # send a reply:
    client.reply.sendReply(
        postid=..., 
        message="The beauti reply on this beauti message..", 
        from_="from Foo", 
        nsfw=True or False
    )
    response = {
            "200": "reply sent",
            "reply": "Cool reply with the API",
            "postid": "522",
            "from": "API testing",
            "rnsfw": "false",
            "replyid": 1473
        }

    # delete a reply:
    client.reply.deleteReply(
        replyid=...
    )
    response = {
            "200": "reply ... has been deleted"
    }

def blogs():

    # Get latest blog:
    client.blog.getlatest()
    response = {
            "200": "latest Blog Post",
            "blogid": "",
            "blogposter_username": "",
            "blogposter_displayname": "",
            "blogposter_pfp": "",
            "blogcontent": "",
            "blogdate": "1990-01-01 00:00:00"
        }


def sockets():
    @socket.on(Events.NewDevlog)
    def new_devlog(devlog):
        devlog = {
            "200": "latest Blog Post",
            "blogid": "",
            "blogposter_username": "",
            "blogposter_displayname": "",
            "blogposter_pfp": "",
            "blogcontent": "",
            "blogdate": "1990-01-01 00:00:00"
        }

    @socket.on(Events.NewPost)
    def new_post(post):
        post = {
             
                "200": "Found post",
                "postid": "....",
                "username": "....",
                "pfp": "https://cds.bubblez.app/v2/get/bblz_606df57511f60/display/256",
                "content": "why is working not working? \r\n",
                "from": None,
                "locked": "false",
                "pnsfw": "false",
                "edited": None,
                "post_date": "2021-11-02 14:59:46",
                "replies": [
                    {
                        "replyid": "....",
                        "username": "MeeSoS",
                        "pfp": "https://cds.bubblez.app/v2/get/bblz_606df57511f60/display/256",
                        "content": "or is it?",
                        "from": None,
                        "rnsfw": None,
                        "deleted": None,
                        "edit_date": None,
                        "reply_date": "2021-11-02 15:01:00"
                    },
                    {
                        "replyid": "....",
                        "username": "MeeSoS",
                        "pfp": "https://cds.bubblez.app/v2/get/bblz_606df57511f60/display/256",
                        "content": "this is test\r\n",
                        "from": None,
                        "rnsfw": None,
                        "deleted": None,
                        "edit_date": None,
                        "reply_date": "2021-11-02 16:06:15"
                    }
                ]
            }

    @socket.on(Events.NewReply)
    def new_post(post, reply):
        post = {
             
                "200": "Found post",
                "postid": "....",
                "username": "....",
                "pfp": "https://cds.bubblez.app/v2/get/bblz_606df57511f60/display/256",
                "content": "why is working not working? \r\n",
                "from": None,
                "locked": "false",
                "pnsfw": "false",
                "edited": None,
                "post_date": "2021-11-02 14:59:46",
                "replies": [
                    {
                        "replyid": "....",
                        "username": "MeeSoS",
                        "pfp": "https://cds.bubblez.app/v2/get/bblz_606df57511f60/display/256",
                        "content": "or is it?",
                        "from": None,
                        "rnsfw": None,
                        "deleted": None,
                        "edit_date": None,
                        "reply_date": "2021-11-02 15:01:00"
                    },
                    {
                        "replyid": "....",
                        "username": "MeeSoS",
                        "pfp": "https://cds.bubblez.app/v2/get/bblz_606df57511f60/display/256",
                        "content": "this is test\r\n",
                        "from": None,
                        "rnsfw": None,
                        "deleted": None,
                        "edit_date": None,
                        "reply_date": "2021-11-02 16:06:15"
                    }
                ]
            }
        reply = {
            "replyid": "....",
            "username": "MeeSoS",
            "pfp": "https://cds.bubblez.app/v2/get/bblz_606df57511f60/display/256",
            "content": "this is test\r\n",
            "from": None,
            "rnsfw": None,
            "deleted": None,
            "edit_date": None,
            "reply_date": "2021-11-02 16:06:15"
        }
        
    socket.connect() or socket.connect(verify=False)

