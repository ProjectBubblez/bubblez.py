import time, _thread
from ..Color import Color
from ..Log import logTime

class Interval:
    def __init__(self, socket) -> None:
        self.sockets_client = socket
    
    def sleeping_ping(self, mili):
        time.sleep(mili/1000)
        self.sockets_client._send_ping()

    def setPing(self, mili_sec):
        _thread.start_new_thread(self.sleeping_ping, (mili_sec,))
