import time, json, _thread, datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Events:
    class NewDevlog:
        def name(self):
            return "NEW_DEVLOG"
    class NewPost:
        def name(self):
            return "NEW_POST"
    class NewReply:
        def name(self):
            return "NEW_REPLY"

class Interval:
    def __init__(self, socket) -> None:
        self.Sockets = socket
    
    def ping(self, mili):
        time.sleep(mili/1000)
        self.Sockets._send_ping()

    def set(self, mili):
        _thread.start_new_thread(self.ping, (mili,))


class Times:
    def log():
        return datetime.datetime.now().strftime("%H:%M:%S")
