import requests
from requests import api

baseurl = "https://bubblez.app/api/v1/"
header = { "Content-Type": "application/x-www-form-urlencoded" }

# options = True or False, True == reply False != Reply
# Check if baseurl is right!

username = None
apikey = None

def load(apikey_import, username_import):
    global apikey, username
    apikey = apikey_import
    username = username_import
    print("Loaded: api-token: {}  username: {}".format(apikey, username))

def sendPost(content, locked):
    global apikey, username, baseurl, header
    if locked != None:
        if content != None:
            para = {"post": content, "locked": locked, "token": apikey}
            postRequest = requests.post(
                baseurl + "sendpost", data=para, headers=header)
            if "error" in postRequest:
                print(postRequest.text)
            return postRequest.json()
        else:
            print("sendPost: No message to send!")
    else:
        print("sendPost: options locked: True or False")


def reply(postid, message):
    global apikey, username, baseurl, header
    if apikey != None:
        if postid != None:
            para = {"token": apikey, "postid": postid, "reply": message}
            replyRequest = requests.post(baseurl + "sendreply", data=para, headers=header)
            if "error" in replyRequest:
                print(replyRequest.text)
            return replyRequest.json()
        else:
            print("reply: Pls give a postid!")
    else:
        print("Reply: Pls load api-token/key first! Bubblez.load(token, username)")

def latestPost():
    global apikey, username, baseurl, header
    if apikey != None:
        para = { "token": apikey }
        latestpostRequest = requests.post(
            baseurl + "latestpost", data=para, headers=header)
        if "error" in latestpostRequest:
            print(latestpostRequest.text)
        return latestpostRequest.json()
    else:
        print("LatestPost: Pls Load api-token/key first! Bubblez.load(token, username)")

def getUser():
    global apikey, username, baseurl, header
    if username != None:
        para = {"username": username, "token": apikey}
        userRequest = requests.post(
            baseurl + "getuser", data=para, headers=header)
        if "error" in userRequest:
            print(userRequest.text)
        return userRequest.json()
    else:
        print("GetUser: Pls load username first! Bubblez.load(token, username)")

def getTokenUser():
    global apikey, username, baseurl, header
    if apikey != None:
        para = {"token": apikey}
        tokenRequest = requests.post(
            baseurl + "checkuser", data=para, headers=header)
        if "error" in tokenRequest:
            print(tokenRequest.text)
        return tokenRequest.json()
    else:
        print("getTokenUser: Pls Load api-token/key first! Bubblez.load(token, username)")

def getPost(postid):
    global apikey, username, baseurl, header
    if postid != None:
        para = { "token": apikey, "postid": postid}
        postRequest = requests.post(baseurl, data=para, headers=header)
        if "error" in postRequest:
            print(postRequest.text)
        return postRequest.json()
    else:
        print("GetPost: pls give a postid! ")

def login():
    global apikey, username, baseurl, header
    if apikey != None:
        para = { "token": apikey }
        loginRequest = requests.post(
            baseurl + "checktoken", data=para, headers=header)
        if "error" in loginRequest:
            print(loginRequest.text)
        return loginRequest.json()
    else:
        print("login: Pls Load api-token/key first! Bubblez.load(token, username)")