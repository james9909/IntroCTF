#!/usr/bin/python

import cgi, cgitb, hashlib

cgitb.enable()

print "Content-Type: text/html"
print ""
inputs = cgi.FieldStorage()

def writeLogin(tid):
    fout = open("../accounts/login_list.txt", "a")
    fout.write("\n" + tid + "\n")
    fout.close()

def alreadyLoggedIn(tid):
    logged_in = open("../accounts/login_list.txt", "r").readlines()
    for team in logged_in:
        if team.strip() == tid:
            return True
    return False

def verify(inputs):
    if "tid" not in inputs or "tpass" not in inputs:
        return "Invalid credentials"
    tid = inputs["tid"].value
    tpass = inputs["tpass"].value
    if alreadyLoggedIn(tid):
        return "Already logged in"
    fin = open("../accounts/teams.txt")
    team_data = fin.readlines()
    hashed = hashlib.sha1(tpass).hexdigest()
    for team in team_data:
        team = team.split(",")
        if tid == team[0]:
            if hashed == team[1].strip():
                writeLogin(tid)
                return "Success!"
    return "Invalid credentials"

print verify(inputs)
