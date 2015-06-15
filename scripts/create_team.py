#!/usr/bin/python

import cgi, hashlib, time

print "Content-Type: text/html"
print ""

inputs = cgi.FieldStorage()

def logTime():
    return int(time.time() * 1000)

def validatePassword(tpass):
    if len(tpass) < 8:
        return "Password should be at least 8 characters"

def teamTaken(tid):
    fin = open("../accounts/teams.txt", "r")
    teams = fin.readlines()
    for team in teams:
        team = team.split("||&&||")
        if tid == team[0]:
            return True
    return False

def userTaken(uid):
    fin = open("../accounts/users.txt", "r")
    info = fin.readlines()
    for user in info:
        user = user.split("||&&||")
        if uid == user[0]:
            return True
    return False

def createNewTeam(tname, tpass, uname, upass):
    tpass_hashed = hashlib.sha1(tpass + "salt").hexdigest()
    upass_hashed = hashlib.sha1(upass + "salt").hexdigest()

    solved = open("../accounts/solved.txt", "a")
    solved.write("%s\n" %(tname))
    solved.close()

    teams = open("../accounts/teams.txt", "a")
    teams.write("\n%s||&&||%s||&&||%s\n" %(tname, tpass_hashed, uname))
    teams.close()

    scores = open("../accounts/scores.txt", "a")
    scores.write("\n%s||&&||0||&&||%s\n" %(tname, logTime()))
    scores.close()

    users = open("../accounts/users.txt", "a")
    users.write("%s||&&||%s\n" %(uname, upass_hashed))
    users.close()

def submitNewTeam(inputs):
    if "tname" not in inputs or "tpass" not in inputs or "tpass_conf" not in inputs or "uname" not in inputs or "upass" not in inputs or "upass_conf" not in inputs:
        return "Something is missing"
    tname = inputs.getvalue("tname").strip()
    tpass = inputs.getvalue("tpass")
    tpass_conf = inputs.getvalue("tpass_conf")
    uname = inputs.getvalue("uname").strip()
    upass = inputs.getvalue("upass")
    upass_conf = inputs.getvalue("upass_conf")

    if tname == None or tname == "":
        return "Please enter a team name"
    if "||&&||" in tname:
        return "Invalid team name"
    if "||&&||" in uname:
        return "Invalid user name"
    if tpass != tpass_conf:
        return "Team passwords do not match"
    if upass != upass_conf:
        return "User passwords do not match"
    if tpass == "" or tpass == None:
        return "Please enter a team password"
    if upass == "" or upass == None:
        return "Please enter a user password"
    if len(tpass) < 8 or len(upass) < 8:
        return "Password should be at least 8 or more characters"
    if teamTaken(tname):
        return "Team name is already taken"
    if userTaken(uname):
        return "Username is already taken"
    createNewTeam(tname, tpass, uname, upass)
    return "Success!"

print submitNewTeam(inputs)
