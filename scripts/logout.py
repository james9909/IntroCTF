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
    fin = open("../accounts/login_list.txt", "rw")
    logged_in = fin.readlines()
    for team in logged_in:
        if team.strip() == tid:
            logged_in.remove(team)
    fin.write("".join(logged_in)) 
    return "Success!"

try:
    cookies = os.environ["HTTP_COOKIE"]
except:
    print "Not logged in!"
    sys.exit(0)

tid = getTID(cookies)
print removeFromLogged(tid)
