# Bubblez.py - Api Module for [Bubblez.app](https://bubblez.app)
A Python Module for the [Bubblez.app](https://bubblez.app) api
- [Bubblez.app](https://bubblez.app/library#bubblez.py) has approved Bubblez.py

## Version's 
- Python: [Github Bubblez.py](https://github.com/ProjectBubblez/Bubblez.py)
- PyPi: [Bubblez.py](https://pypi.org/project/Bubblez.py/0.0.2.1/)
- Nodejs: [Bubblez.js](https://github.com/ProjectBubblez/bubblez.js)
- Nodejs Wiki/Documentation: [Wiki/Documentation](https://github.com/ProjectBubblez/bubblez.js/blob/master/DOCUMENTATION.md)
 ---- 
- Website: [Bubblez.app](https://bubblez.app)

## Setup

Pip install:
```bash
   pip install bubblez.py
```
 --- 

Required modules: requests
```bash 
   $ python3 -m pip install requests 
```


## Examples
Check the [examples.py](https://github.com/MeesMeijer/bubblez.py/blob/main/examples.py) file above!


# Docs
### Basic Client Setup:
If u do not have a token:
   Request your token at: https://bubblez.app/applications/api-token'

```python3
   from Bubblez import Bubblez 
   
   client = Bubblez("Your Username", "your token")  
```
### Basic Client Setup with websockets:
```python3
   from Bubblez import Bubblez 
   from Bubblez import Socket, Events
   
   client = Bubblez("Your Username", "your token")
   socket = Socket(client)
   
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
        
    socket.connect()
   
```
<br>

## User stuff: 
### checkUser()
```python3
   client.user.checkUser()
```
The response: 
```python3
{
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
```


### pingUser()
```python3
   client.user.pingUser()
```
The response: 
```python3
{
    "200": "Pong",
    "username": "DarkMatter",
    "online_status": "2021-07-30 13:03:18"
}
```
### getUser()
```python3
   client.user.getUser()
```
The response: 
```python3
{
    "200": "Found user",
    "uuid": null,
    "username": "embed",
    "displayname": "embed",
    "followers": 2,
    "pfp": "https://i.imgur.com/Md5C3uy.gif",
    "banner": null,
    "coins": "0",
    "rank": "founder",
    "eventr": "lgbt19",
    "patreon": "true",
    "booster": "true",
    "bio": "the best bubblez dev.",
    "nsfw": "false",
    "pronoun": "none",
    "ban": null,
    "created_at": "2019-10-22 12:04:01",
    "last_posted": null,
    "posts": [
        {
            "postid": "280",
            "username": "embed",
            "nsfw": "false",
            "content": "gamimg",
            "from": null,
            "locked": "false",
            "edited": null,
            "post_date": "2020-08-09 17:15:19"
        }
    ]
}
```

<br>

## Posts stuff:
### sendPost()
```python3
   client.post.sendPost(
        message="The best Website is:...",
        from_="This Beauti Python Program",
        locked=True or False,
        nsfw=True or False,
    )
```
The response: 
```python3
{
    "200": "message sent",
    "post": "API is cool",
    "from": "API testing",
    "locked": "false",
    "pnsfw": "false",
    "postid": 522
}
```

### editPost()
```python3
   client.post.editPost(
      new_message='The edited message',
      postid=1234
   )
```
The response:
```python3
{
    "200": "Post 522 has been updated"
}
```

### getPost()
```python3
   client.post.getPost(
      postid=...
   )
```
The response: 
```python3
{
    "200": "Found post",
    "postid": "522",
    "username": "DarkMatter",
    "pfp": "https://i.imgur.com/jAOd5gE.png",
    "nsfw": "false",
    "content": "API is cool",
    "from": "API testing",
    "locked": "false",
    "edited": null,
    "post_date": "2021-07-30 12:18:31",
    "replies": [
        {
            "replyid": "1473",
            "username": "DarkMatter",
            "pfp": "https://i.imgur.com/jAOd5gE.png",
            "content": "Cool reply with the API",
            "from": null,
            "deleted": null,
            "edit_date": null,
            "reply_date": "2021-07-30 12:49:12"
        }
    ]
}
```

### deletePost()
```python3
   client.post.deletePost(
      postid=...
   )
```
The response: 
```python3
{
    "200": "Post 522 has been deleted"
}
```

### lockPost()
```python3
   client.post.lockPost(
      postid=..., 
      locked=True or False
   )
```
The response: 
```python3
{
    "200": "Post 522 has been locked"
}
or 
{
    "200": "Post 522 has been unlocked"
}
```

### getLatestPost()   ``Global``
```python3
   client.post.getLatestPost(
      postid_only=True or False
   )
```
The response: 
```python3
{
    "200": "latest Post",
    "postid": "522"
}
```

<br>

## Reply's: 
### sendReply()
```python3
   client.reply.sendReply(
        postid=..., 
        message="The beauti reply on this beauti message..", 
        from_="from python", 
        nsfw=True or False
   )
```
The response: 
```python3
{
    "200": "reply sent",
    "reply": "Cool reply with the API",
    "postid": "522",
    "from": "API testing",
    "rnsfw": "false",
    "replyid": 1473
}
```

### deleteReply()
```python3
   client.reply.deleteReply(
        replyid=...
   )
```
The response: 
```python3
{
    "200": "reply 1473 has been deleted"
}
```

### editReply()
```python3
   client.reply.editReply(
        replyid=...,
        new_reply="edited reply"
   )
```
The response: 
```python3
{
    "200": "Reply 1473 has been updated"
}
```

<br>

## Blog:
### getLatest()
```python3
   client.blog.getLatest()
```
The response: 
```python3
{
    "200": "latest Blog Post",
    "blogid": "",
    "blogposter_username": "",
    "blogposter_displayname": "",
    "blogposter_pfp": "",
    "blogcontent": "",
    "blogdate": "1990-01-01 00:00:00"
}
```

<br>

## Websockets 
### A full websocket lisener: 
```python3

   client = Bubblez("username", "token",)
   socket = Socket(client)

   @socket.on(Socket.Events.NewPost)
   def new_post(post):
       print(post)

   @socket.on(Socket.Events.NewReply)
   def new_reply(post, reply):
       print(post, reply)
      
   @socket.on(Socket.Events.NewDevlog)
   def new_devlog(devlog):
       print(devlog)

   socket.connect()
```
### If you use windows and websockets give a SSL error: 
```python3
   socket.connect(verify=False)
```
### ``Note``: 
   This is vulnerable for man-in-middle attacks!! 

