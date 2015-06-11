#!/usr/bin/python

import sys, os

print "Content-Type: text/html\n"
print ""

def getTID(cookies): 
    cookies = cookies.split(";")
    tid = cookies[1]
    tid = tid[5:]
    return tid

def removeFromLogged(tid):
    fin = open("../accounts/login_list.txt", "r")
    logged_in = fin.readlines()
    while "\n" in logged_in:
        logged_in.remove("\n")
    for team in logged_in:
        if team.strip() == tid:
            logged_in.remove(team)
    open("../accounts/login_list.txt", "w").write("".join(logged_in) + "\n") 
    return "Success!"

try:
    cookies = os.environ["HTTP_COOKIE"]
except:
    print "Not logged in!"
    sys.exit(0)

tid = getTID(cookies).strip()
print removeFromLogged(tid)
