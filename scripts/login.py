#!/usr/bin/python

import cgi, cgitb, hashlib

cgitb.enable()

print "Content-Type: text/html"
print ""

inputs = cgi.FieldStorage()

def getTeam(uname):
    fin = open("../accounts/teams.txt")
    teams = fin.readlines()
    for team in teams:
        team = team.strip().split("||&&||")
        members = team[2:]
        for member in members:
            if uname == member:
                return team[0]

def login(inputs):
    uname = inputs["uname"].value
    tid = getTeam(uname)
    token = hashlib.sha1(tid).hexdigest()
    u = hashlib.sha1(uname).hexdigest
    return "%s||&&||%s||&&||%s" %(token, tid, u)

print login(inputs)
