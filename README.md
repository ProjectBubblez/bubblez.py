# Bubblez.py - Api Module for [Bubblez.app](https://bubblez.app)
A Python Module for the [Bubblez.app](https://bubblez.app) api
- [Bubblez.app](https://bubblez.app/library#bubblez.py) has approved Bubblez.py

## Version's 
- Python: [Github Bubblez.py](https://github.com/ProjectBubblez/Bubblez.py)
- PyPi: [Bubblez.py](https://pypi.org/project/Bubblez.py/0.0.2.1/)
- Bubblez.js: [Bubblez.js](https://github.com/ProjectBubblez/bubblez.js)
- Bubblez.js Wiki/Documentation: [Wiki/Documentation](https://github.com/ProjectBubblez/bubblez.js/blob/master/DOCUMENTATION.md)
 ---- 
- Live Website: [Bubblez.app](https://bubblez.app)
- Canary Website [Bubblez.app](https://canary.bubblez.app/)

## Setup
######For this Api Module you need to have your api token!
######If you dont? Than request it [here.](https://bubblez.app/applications/api-token)

Pip install:
```bash
   pip install bubblez.py
```
 --- 

If you dont use the Pypi, than you need to manuel install Requests
```bash 
   python -m pip install requests 
```

#### ```Note```: 
If you use Windows and can not connected to the websockets because a SSL problem with python: <b>This is vulnerable for man-in-middle attacks!!</b>
```python3
socket.connect(verify=False)
```


## Examples

Check the [examples](https://github.com/ProjectBubblez/Bubblez.py/tree/main/examples) for api and websockets


# Docs 
### Basic Client Setup:

```python3
    from Bubblez import Bubblez 

    client = Bubblez("Live token") 

    'If you want to post to canary:'
    client = Bubblez("Canary token", use_canary=True)

```
### Basic Client Setup with websockets:
```python3
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
   
```
<br>

## User stuff: 
#### Check the user:
##### Command: ```client.user.check()```
##### The response: 
```class User.json()```
```js
{
      "200": "Found user",
      "uuid": null,  
      "username": "DarkMatter",
      "displayname": "DarkMatter",
      "email": "zak@bubblez.app",
      "pfp": "https://i.imgur.com/jAOd5gE.png",
      "banner": "https://i.imgur.com/1bZdeBF.png",
      "coins": "85",
      "rank": "founder",
      "eventr": "darkmatter",
      "patreon": "true",
      "booster": "true",
      "bio": "We don't know much about them, but we're sure DarkMatter is great.",
      "nsfw": "false",
      "dob": null,
      "pronoun": "hehim",
      "ban": null,
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
              "edited": null,
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
              "edited": null,
              "reply_date": "2021-07-30 12:49:12"
          }
      ]
  }
```


#### Ping the user:
##### Command: ```client.user.ping()```
##### The response: 
```class User.json()```
```js
{
    "200": "Pong",
    "username": "DarkMatter",
    "online_status": "2021-07-30 13:03:18"
}
```
#### Get the user:
##### Command: ```client.user.get()```
##### The response: 
```class User.json()```
```js
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
    "pronoun": "null",
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
#### Send a Post:
##### Command: ```post = client.post.send()```
##### The response: 
```post.json()```
```js
{
    "200": "message sent",
    "post": "API is cool",
    "from": "API testing",
    "locked": "false",
    "pnsfw": "false",
    "postid": 522
}
```

#### Edit a post
##### Command: ```post = client.post.edit()```
##### The response: 
```post.json()```
```js
{
    "200": "Post 522 has been updated"
}
```

#### Get a post
##### Command: ```post = client.post.get()```
##### The response: 
```post.json()```
```js
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

#### Delete a Post
##### Command: ```post = client.post.delete()```
##### The response: 
```post.json()```
```js
{
    "200": "Post 522 has been deleted"
}
```

#### Lock a post
##### Command: ```post = client.post.lock()```
##### The response:  
```post.json()```
```js
{
    "200": "Post 522 has been locked"
}
```
or when unlocked
```js
{
    "200": "Post 522 has been unlocked"
}
```

#### Get the latest post ```Global```
##### Command: ```post = client.post.get_latest()```
##### The response: 
```post.json()```
```js
{
    "200": "latest Post",
    "postid": "522"
}
```

<br>

## Reply's: 
#### Send a reply
##### Command: ```reply = client.reply.send()```
##### The response: 
```reply.json()```
```js
{
    "200": "reply sent",
    "reply": "Cool reply with the API",
    "postid": "522",
    "from": "API testing",
    "rnsfw": "false",
    "replyid": 1473
}
```

#### Delete a reply
##### Command: ```reply = client.reply.delete()```
##### The response: 
```reply.json()```
```js
{
    "200": "reply 1473 has been deleted"
}
```

#### Edit a reply()
##### Command: ```reply = client.reply.edit()```
##### The response: 
```reply.json()```
```js
{
    "200": "Reply 1473 has been updated"
}
```

<br>

## Blog:
#### Get the latest Blog post!()
##### Command: ```devlog = client.devlog.get_latest()```
##### The response: 
```devlog.json()```
```js
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
