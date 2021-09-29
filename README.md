# Bubblez.py - Api Module for 
A Python Module for the [bubblez](https://bubblez.app) api

## Setup
To use this python module, you need to install ```$ python3 -m pip install Requests ```


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
<b>checkUser:</b>
```python3
   client.user.checkUser()
```

<b>pingUser:</b>
```python3
   client.user.pingUser()
```

<br>

## Posts:
<b>sendPost:</b> 
```python3
   client.post.sendPost(
        message="The best Website is:...",
        from_="This Beauti Python Program",
        locked=True or False,
        nsfw=True or False,
    )
```

<b>getPost:</b>
```python3
   client.post.getPost(
      postid=...
   )
```

<b>deletePost:</b>
```python3
   client.post.deletePost(
      postid=...
   )
```

<b>lockPost:</b>
```python3
   client.post.lockPost(
      postid=..., 
      locked=True or False
   )
```

<b>getLatestPost:   ``Global``</b>
```python3
   client.post.getLatestPost(
      postid_only=True or False
   )
```

<br>

### Reply's: 
<b>sendReply:</b>
```python3
   client.reply.sendReply(
        postid=..., 
        message="The beauti reply on this beauti message..", 
        from_="from python", 
        nsfw=True or False
   )
```

<b>deleteReply:</b>
```python3
   client.reply.deleteReply(
        replyid=...
   )
```
   
<br>
   
## Blog:
<b>getLatest:</b>
```python3
   client.blog.getLatest()
 ```

<br>

## Lis
U can just use it

