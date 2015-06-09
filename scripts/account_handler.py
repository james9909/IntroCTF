#!/usr/bin/python

import cgi, cgitb, hashlib

cgitb.enable()

print "Content-Type: text/html"
print ""

inputs = cgi.FieldStorage()

def teamTaken(tid):
    teams = open("../accounts/teams.txt", "r")
    for team in teams:
        if tid == team[0]:
            return True
    return False

def createNewTeam(tid, tpass):
    hashed = hashlib.sha1(tpass).hexdigest()
    teams = open("../accounts/teams.txt", "a")
    teams.write("%s,%s" %(tid, hashed))
    teams.close()
    scores = open("../accounts/scores.txt", "a")
    scores.write("%s,0" %(tid))
    scores.close()

def submitNewTeam(inputs):
    tid = inputs.getvalue("tid")
    tpass = inputs.getvalue("tpass")
    tpass_conf = inputs.getvalue("tpass_conf")
    return inputs

    if tid == None or tid == "undefined":
        return "Please enter a team name"
    if tpass != tpass_conf:
        return "Passwords do not match"
    if teamTaken(tid):
        return "Team name is already taken"
    createNewTeam(tid, tpass)

print submitNewTeam(inputs)
