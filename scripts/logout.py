#!/usr/bin/python

import sys, os, hashlib

print "Content-Type: text/html\n"
print ""

def getUID(cookies):
    cookies = cookies.split(";")
    uid = cookies[2]
    uid = uid[3:]
    return uid

def removeFromLogged(uid):
    fin = open("../accounts/login_list.txt", "r")
    logged_in = fin.readlines()
    while "\n" in logged_in:
        logged_in.remove("\n")
    for team in logged_in:
        print hashlib.sha1(team.strip() + "salt").hexdigest()
        if hashlib.sha1(team.strip() + "salt").hexdigest() == uid:
            logged_in.remove(team)
    open("../accounts/login_list.txt", "w").write("".join(logged_in) + "\n")
    return "Success!"

try:
    cookies = os.environ["HTTP_COOKIE"]
except:
    print "Not logged in!"
    sys.exit(0)

uid = getUID(cookies).strip()
print removeFromLogged(uid)
