# Bubblez.py - Api Module for [bubblez](https://bubblez.app)
A Python Module for the [bubblez](https://bubblez.app) api

## Version's 
- Python: This one..
- Nodejs: [HERE](https://github.com/ProjectBubblez/bubblez.js)
 ---- 
- Official Wiki/Documentation: [Wiki/Documentation](https://github.com/ProjectBubblez/bubblez.js/blob/master/DOCUMENTATION.md)
- Website: [Bubblez.app](https://bubblez.app)

## Setup
To use this python module, you need to install ```$ python3 -m pip install requests ```


## Examples
Check the [example.py](examples.py) file above!


# Docs
### Basic Client Setup:
```python3
   from bubblez import Bubblez 
   
   client = Bubblez("Your Username", "your token")  # Request your token at: 'https://bubblez.app/applications/api-token'
```

<br>

## User: 
#### checkUser()
```python3
   client.user.checkUser()
```


#### pingUser()
```python3
   client.user.pingUser()
```

### getUser()
```python3
   client.user.getUser()
```

<br>

## Posts:
#### sendPost()
```python3
   client.post.sendPost(
        message="The best Website is:...",
        from_="This Beauti Python Program",
        locked=True or False,
        nsfw=True or False,
    )
```

#### getPost()
```python3
   client.post.getPost(
      postid=...
   )
```

#### deletePost()
```python3
   client.post.deletePost(
      postid=...
   )
```

#### lockPost()
```python3
   client.post.lockPost(
      postid=..., 
      locked=True or False
   )
```

#### getLatestPost()   ``Global``
```python3
   client.post.getLatestPost(
      postid_only=True or False
   )
```

<br>

### Reply's: 
#### sendReply()
```python3
   client.reply.sendReply(
        postid=..., 
        message="The beauti reply on this beauti message..", 
        from_="from python", 
        nsfw=True or False
   )
```

#### deleteReply()
```python3
   client.reply.deleteReply(
        replyid=...
   )
```
   
<br>
   
## Blog:
#### getLatest()
```python3
   client.blog.getLatest()
 ```

<br>

## Lis
U can just use it

