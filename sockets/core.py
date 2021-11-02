from .classes import bcolors, Times, Interval
import json, websocket, ssl

class Sockets:
    def __init__(self, client, verbose=False) -> None:
        self.client = client
        self.lisener = None 
        self.events = {}
        self.authenticated = False 
        self.ping_interval = Interval(self)
        self.verbose = verbose

    def on(self, event, **kwargs):
        def deco(func):
            self.events[event.name(event)] = func 
            return func
        return deco
    
    def _send_ping(self):
        if self.verbose:
            print(f"{bcolors.OKBLUE}[Bubblez.py] {Times.log()} Sending ping!{bcolors.ENDC}")
        self.lisener.send(
            json.dumps({
                "message": "HEARTBEAT"
            })
        )

    def on_error(self, *args):
        if isinstance(args[0], websocket.WebSocketConnectionClosedException):
            print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Lost connection with websocket, reconnecting!{bcolors.ENDC}")
            self.connect()
            return 
        print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Error Message:", args, bcolors.ENDC)

    def on_message(self, incomming):
        incomming = json.loads(incomming)

        if incomming['message'] == "AUTHENTICATION_REQUIRED":
            if self.verbose:
                print(f"{bcolors.OKGREEN}[Bubblez.py] {Times.log()} Trying to Authenticate!{bcolors.ENDC}")
            self.lisener.send(json.dumps(({
                    "message": "SEND_TOKEN",
                    "token": self.client.token
            })))
            return
        
        if incomming['message'] == "AUTHENTICATED":
            print(f"{bcolors.OKGREEN}[Bubblez.py] {Times.log()} Authentication successful!{bcolors.ENDC}")
            self.authenticated = True 
            self.pingTimeout = incomming['heartbeatinterval']-200
            self.ping_interval.set(self.pingTimeout)
            return
        
        if incomming['message'] == "HEARTBEAT_ACK":
            if self.verbose:
                print(f"{bcolors.OKBLUE}[Bubblez.py] {Times.log()} Received pong!{bcolors.ENDC}")
            self.ping_interval.set(self.pingTimeout)
            return

        if incomming['message'] == "HEARTBEAT_MISSED":
            if self.verbose:
                print(f"{bcolors.WARNING}[Bubblez.py] Missed heartbeat, resending now!{bcolors.ENDC}")
            self._send_ping()
            self.pingTimeout = incomming['heartbeatinterval']
            self.ping_interval.set(self.pingTimeout)
            return

        if incomming['message'] == "NEW_POST":
            if "NEW_POST" in self.events:
                self.events["NEW_POST"](post=incomming['postdata'])
                return

        if incomming['message'] == "NEW_REPLY":
            if "NEW_REPLY" in self.events:
                self.events['NEW_REPLY'](post=incomming['postdata'], reply=incomming['replydata'])
                return 
            
        if incomming['message'] == "NEW_DEVLOG":
            if "NEW_REPLY" in self.events:
                self.events['NEW_DEVLOG'](devlog=incomming['postdata'])
                return 


        if self.verbose:
            print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()}", incomming, f" Was not fetched!{bcolors.ENDC}")

    def on_open(self,*args):
        print(f"{bcolors.OKGREEN}[Bubblez.py] {Times.log()} Connected with websockets!{bcolors.ENDC}")

    def on_close(self, *args):
        print(f"{bcolors.WARNING}[Bubblez.py] {Times.log()} Websockets closed!\nReason: ", args, f"{bcolors.ENDC}")

    def connect(self, verify: bool):
        if self.verbose:
            print(f"{bcolors.OKGREEN}[Bubblez.py] {Times.log()} Trying to connect with websockets!{bcolors.ENDC}")
        self.lisener = websocket.WebSocketApp(
            url="wss://ws.bubblez.app/live",
            on_close=self.on_close,
            on_error=self.on_error,
            on_message=self.on_message,
            on_open=self.on_open)
        if verify:
            self.lisener.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
        else:
            self.lisener.run_forever()