import traceback
from ..classes.Color import Color
from ..classes.Log import logTime
from ..classes.socket.events.events import Events

from ..classes.socket.receive.Devlog import Devlog as ReceivedDevlog
from ..classes.socket.receive.User import User as ReceivedUser
from ..classes.socket.receive.Post import Post as ReceivedPost
from ..classes.socket.receive.Reply import Reply as ReceivedReply
from ..classes.socket.receive.Likes import Likes as ReceivedLike
from ..classes.socket.receive.Follower import Follower as ReceivedFollower
from ..classes.socket.receive.Edit import Edit as ReceivedEdit

import websocket, json, time, _thread, ssl, functools

class Interval:
    def __init__(self, socket) -> None:
        self.sockets_client = socket
    
    def sleeping_ping(self, mili):
        time.sleep(mili/1000)
        self.sockets_client.ping()

    def setPing(self, mili_sec):
        _thread.start_new_thread(self.sleeping_ping, (mili_sec,))

class Socket:
    def __init__(self, client, url=None) -> None:
        self.client = client
        self.ws = None 

        self.mili_bt_ping = 40000
        self.ping_send = False 
        self.ping_thread = Interval(self) 

        if self.client.canary: self.websocket_uri = "wss://ws.bubblez.app/canary"
        else: self.websocket_uri = "wss://ws.bubblez.app/live"
        
        if url:
            self.websocket_uri = url 
        self.events = {}
        
    def on(self, event, **kwargs):
        """
        Decorator for websocket events!
        """
        def deco(func):
            self.events[event.name(event)] = func 
            return func
        return deco
    
    def ping(self):
        if self.client.verbose:
            print(f"{Color.OKBLUE}[Bubblez.py-websockets-{self.client.prefix_log}] {logTime()} Sending Ping!", Color.ENDC)
                
        self.ws.send(
            json.dumps(
                {
                    "message": "HEARTBEAT"
                }
            )
        )
        self.ping_send = True 

    def connect(self, verify:bool=False):
        def on_message(ws: websocket.WebSocketApp, incomming):
            incomming = json.loads(incomming)
            event = incomming['message']

            if event == "AUTHENTICATION_REQUIRED":
                if self.client.verbose:
                    print(f"{Color.OKBLUE}[Bubblez.py-websockets-{self.client.prefix_log}] {logTime()} Trying to authenticated!", Color.ENDC)
                self.ws.send(json.dumps(({
                        "message": "SEND_TOKEN",
                        "token": self.client.token,
                        "version": 1
                })))
                return 
                
            elif event == "AUTHENTICATED":
                self.mili_bt_ping = incomming['heartbeatinterval']
                self.ping()
                self.ping_thread.setPing(self.mili_bt_ping)
                return 

            elif event == "HEARTBEAT_ACK":
                if self.client.verbose:
                    print(f"{Color.OKBLUE}[Bubblez.py-websockets-{self.client.prefix_log}] {logTime()} Received Pong!", Color.ENDC)
                self.ping_thread.setPing(self.mili_bt_ping)
                return 
            
            elif event == "HEARTBEAT_MISSED":
                if self.client.verbose:
                    print(f"{Color.OKBLUE}[Bubblez.py-websockets-{self.client.prefix_log}] {logTime()} Missed heartbeat!", Color.ENDC)
                self.ping()
                self.mili_bt_ping = incomming['heartbeatinterval']
                self.ping_thread.setPing(self.mili_bt_ping)
                return 

            elif event == "NEW_POST":
                if event in self.events:
                    self.events[event](
                            post=ReceivedPost(self.client, incomming['postdata'])
                        )
                    return 

            elif event == "NEW_REPLY":
                if event in self.events:
                    self.events[event](
                            post=ReceivedPost(self.client, incomming['postdata']), 
                            reply=ReceivedReply(self.client, incomming['replydata'])
                            )
                    return

            elif event == "NEW_DEVLOG":
                if event in self.events:
                    self.events[event](
                            devlog=ReceivedDevlog(self.client, incomming['postdata'])
                        )
                    return

            elif event == "NEW_LIKE":
                if event in self.events:
                    self.events[event](
                            type=incomming['type'], 
                            user=ReceivedUser(self.client, incomming['userdata']), 
                            post=ReceivedPost(self.client, incomming['postdata'])
                        )
                    return

            elif event == "NEW_FOLLOWER":
                if event in self.events:
                    self.events[event](
                            user=ReceivedUser(self.client, incomming['userdata'])
                        )
                    return

            elif event == "UNFOLLOWED":
                if event in self.events:
                    self.events[event](
                            user=ReceivedUser(self.client, incomming['userdata'])
                        )
                    return

            elif event == "NEW_EDIT":
                if event in self.events:
                    post, reply = None, None 
                    if incomming['type'] == "post": post = ReceivedPost(self.client, incomming['postdata'])
                    if incomming['type'] == "reply": reply = ReceivedReply(self.client, incomming['replydata'])
                    self.events[event](
                        user=ReceivedUser(self.client, incomming['userdata']), type=incomming['type'], post=post, reply=reply
                    )
                    return

            elif event == "UNLIKE":
                if event in self.events:
                    post, reply = None, None 
                    if incomming['type'] == "post": post = ReceivedPost(self.client, incomming['postdata'])
                    if incomming['type'] == "reply": reply = ReceivedReply(self.client, incomming['replydata'])

                    self.events[event](
                        user=ReceivedUser(self.client, incomming['userdata']), type=incomming['type'], post=post, reply=reply
                    )
                    return 
            
            if self.client.verbose:
                print(f"{Color.WARNING}[Bubblez.py-websockets-{self.client.prefix_log}] {logTime()}", incomming, f" was not fetched!{Color.ENDC}")
        
        def on_error(ws, what_failed):
            print(f"{Color.FAIL}[Bubblez.py-websockets-{self.client.prefix_log}] {logTime()} Error with websockets \n The error:", what_failed, f"{Color.ENDC}")
            traceback.print_exc()

        def on_open(ws):
            print(f"{Color.OKGREEN}[Bubblez.py-websockets-{self.client.prefix_log}] {logTime()} Connected with the websockets!{Color.ENDC}")

        def on_close(ws, close_status_code, close_msg):
            print(f"{Color.WARNING}[Bubblez.py-websockets-{self.client.prefix_log}] {logTime()} Websockets closed!\nClose code:", close_status_code,"  Close msg:", close_msg, f"{Color.ENDC}")
        
        
        self.ws = websocket.WebSocketApp(
            url=self.websocket_uri,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
            on_message=on_message
        )
        
        if self.client.verbose:
            print(f"{Color.OKGREEN}[Bubblez.py-websockets-{self.client.prefix_log}] {logTime()} Trying to connect with websockets!{Color.ENDC}")

        if verify:
            self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
        else: self.ws.run_forever()
