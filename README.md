# Bubblez.py - Api Module for [Bubblez.app](https://bubblez.app)
A Python Module for the [Bubblez.app](https://bubblez.app) api
- [Bubblez.app](https://bubblez.app/library#bubblez.py) has approved Bubblez.py


# Bubblez live will shutdown from 07-01-2023 till ... 

## Version's 
- Python: [Github Bubblez.py](https://github.com/ProjectBubblez/bubblez.py)
- PyPi: [bubblez.py](https://pypi.org/project/bubblez.py/)
- Bubblez.js: [bubblez.js](https://github.com/ProjectBubblez/bubblez.js)
- Bubblez.js Wiki/Documentation: [Wiki/Documentation](https://github.com/ProjectBubblez/documentation)
 ---- 
- Live Website: [bubblez.app](https://bubblez.app)
- Canary Website [canary.bubblez.app](https://canary.bubblez.app/)

## Setup
##### For this Api Module you need to have your api token!
##### If you dont? Than request it [here.](https://bubblez.app/applications/api-token)

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
If you use Windows and can not connected to the websockets because a SSL problem with python: 
```python3
socket.connect(verify=False)
```
##### <b>This is vulnerable for man-in-middle attacks!!</b>
<br>

## Examples

Check the [examples](https://github.com/ProjectBubblez/bubblez.py/tree/main/examples) for api and websockets


# Docs 
### Basic Client Setup:

```python3
    from Bubblez import Bubblez 

    client = Bubblez("Live token") 

    'If you want to post to canary:'
    client = Bubblez("Canary token", use_canary=True)

```
### Client Setup with all the websocket-events:
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
    def new_follower(user: classes.User):
        print(user.json())
        "Do Your thing"

    @socket.on(Events.NewReply)
    def new_reply(postid: int, reply: classes.Reply):
        post = client.post.get(postid)
        print(post.message, reply.message)
        "Do Your thing"

    @socket.on(Events.UnFollowed)
    def un_follower(user: classes.User):
        print(user.json())
        "Do Your thing"

    @socket.on(Events.NewEdit)
    def new_edit(user: classes.User, type: str, post: classes.Post, reply: classes.Reply):        
        print(user.json(), type, post.json(), reply.json())
        "Do Your thing"

    @socket.on(Events.Unlike)
    def un_linke(user: classes.User, type: str, post: classes.Post, reply: classes.Reply):
        print(user.json(), type, post.json(), reply.json())
        "Do Your thing"

    socket.connect()
   
```
<br>

## User stuff: 
#### Check the user:
##### Command: ```user = client.user.check()```
This command checks the client's token 
##### The response: 
```user.json()```
```js
{
    "200": "Found user",
    "uuid": null,
    "username": "DarkMatter",
    "displayname": "DarkMatter",
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
##### Command: ```user = client.user.ping()```
##### The response: 
```user.json() ```
```js
{
    "200": "Pong",
    "username": "DarkMatter",
    "online_status": "2021-07-30 13:03:18"
}
```
#### Get the user:
##### Command: ```user = client.user.get(username=..)```
| Arguments | Type      | Value |
| :---      | :---      | :--- | 
| username  | ```str``` | The user you want to get | 
##### The response: 
```user.json() ```
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
#### Send a Post:
##### Command: ```post = client.post.send(message=.., from_=.., locked=.., nsfw=..)```
| Arguments | Type      | Value                           |
| :---      | :---      | :---
| message   | ```str``` | The message in the post.                   | 
| from_     | ```str``` | The little message next to the date.       | 
| locked    | ```bool``` | if True, no-one can reply.                    | 
| nsfw      | ```bool``` | if True, You need to set DOB (Date Of birth) to see this| 
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

#### Get a post
##### Command: ```post = client.post.get(postid=..)```
##### The response: 
| Arguments | Type      | Value                           |
| :---      | :---      | :--- | 
| postid    | ```int``` | The postid of the post you want to get. | 

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
##### Command: ```post = client.post.delete(postid=..)```
| Arguments | Type      | Value                           |
| :---      | :---      | :--- | 
| postid    | ```int``` | The id of the post you want to delete. | 

##### The response: 
```post.json()```
```js
{
    "200": "Post 522 has been deleted"
}
```

#### Lock a post
##### Command: ```post = client.post.lock(postid=.., togglelock=..)```
| Arguments | Type      | Value                           |
| :---      | :---      | :--- | 
| postid    | ```int``` | The post id|  
| togglelock| ```bool```| If True, no-one can reply on your post! |
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
##### Command: ```post = client.post.get_latest(id_only=..)```
| Arguments | Type      | Value                           |
| :---      | :---      | :--- | 
| id_only    | ```bool``` | If False, than it returns a Post object else only the ID | 
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
##### Command: ```reply = client.reply.send(message=.., postid=.., from_=.., nsfw=...)```
| Arguments | Type      | Value                           |
| :---      | :---      | :---
| message   | ```str``` | The message in the reply.                   | 
| postid    | ```int``` | The postid you want to reply on |  
| from_     | ```str``` | The little message next to the date.       | 
| nsfw      | ```bool``` | if True, You need to set DOB (Date Of birth) to see this| 
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
##### Command: ```reply = client.reply.delete(replyid=..)```
| Arguments | Type      | Value                           |
| :---      | :---      | :---
| replyid    | ```int``` | The postid you want to reply on |  

##### The response: 
```reply.json()```
```js
{
    "200": "reply 1473 has been deleted"
}
```

#### Edit a reply()
##### Command: ```reply = client.reply.edit(replyid=.., message=..)```
| Arguments | Type      | Value                           |
| :---      | :---      | :---                  | 
| replyid   | ```int``` | The postid you want to reply on |  
| message   | ```str``` | the message than will replace the old one | 
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
This command returns the latest Blog! 
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

### 
