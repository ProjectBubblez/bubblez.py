import datetime

from ..components.Post import Post
from ..components.Reply import Reply
from ..components.User import User

from ..models.urls.Endpoints import Endpoints
from ..models.urls.Requester import Requester

class Posts:
    def __init__(self, client) -> None:
        self.client = client
        self.requester = Requester(self.client)

    def get(self, postid: int, replies: bool = True) -> Post:
        '''
        | postid   | `<int>` | id of the post you want to get \n
        | replies* | `<bool>`| if True, the posts returns with all the replies
        '''

        resp = self.requester.request(Endpoints.Posts.get(postid=postid, replies=replies))
        print(resp.content)


        pass 
    
    def send(self, content: str, locked: bool = False, nsfw: bool = False) -> Post:
        '''
        Here you can send an new post\n 
        | content | `<str>`  | the "text" content of the post
        | locked  | `<bool>` | if True, no one can reply to the post
        | nsfw    | `<bool>` | if True, DOB has to be set in settings `18+`
        '''
        resp = self.requester.request(Endpoints.Posts.send(content=content, locked=locked, nsfw=nsfw))
        print(resp.content)
        pass 

    def sendObj(self, postObj: dict) -> Post:
        '''
        similar to .send but here you can post an dict: \n
        postObj: {
            "content": `<str>`    | the "text" content of the post
            "locked": `<bool>`,   | if True, no one can reply to the post
            "nsfw": `<bool>`,     | if True, DOB has to be set in settings `18+`
        }
        '''
        pass 
    
    
    def delete(postid: int) -> True|False:
        '''
        This deletes the post\n
        | postid | `<int>` | id of the post to delete
        '''
        pass 

    def edit(postid: int, content: str = None, locked: bool = None, nsfw: bool = None) -> Post:
        '''
        Here you can edit/update an existing post
        | postid  | `<int>`  | id of the post to edit/update
        | content | `<str>`  | the updated "text" content of the post
        | locked  | `<bool>` | if True, no one can reply to the post
        | nsfw    | `<bool>` | if True, DOB has to be set in settings `18+`
        '''

        pass 

    def lock() -> Post:
        pass 

    def like(postid: int, liked: bool = True):
        pass 

