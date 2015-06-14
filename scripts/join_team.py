#!/usr/bin/python

import cgi, cgitb, hashlib

cgitb.enable()

print "Content-Type: text/html"
print ""

inputs = cgi.FieldStorage()

def validateTeam(tname, tpass):
    tpass = hashlib.sha1(tpass).hexdigest()
    fin = open("../accounts/teams.txt", "r")
    teams = fin.readlines()
    for team in teams:
        team = team.split("||&&||")
        if tname == team[0]:
            if tpass == team[1]:
                return True
    return False

def addUser(uname, upass):
    upass_hashed = hashlib.sha1(upass).hexdigest()

    users = open("../accounts/users.txt", "a")
    users.write("%s||&&||%s\n" %(uname, upass_hashed))
    users.close()

def fullTeam(tname):
    fin = open("../accounts/teams.txt", "r")
    teams = fin.readlines()
    for team in teams:
        team = team.strip().split("||&&||")
        team = team[1:]
        if len(team) == 4:
            return True
    return False

def alreadyOnTeam(tname, uname):
    fin = open("../accounts/teams.txt", "r")
    teams = fin.readlines()
    for team in teams:
        team = team.strip().split("||&&||")
        for user in team:
            if user == uname:
                return True
    return False

def joinTeam(tname, uname):
    fin = open("../accounts/teams.txt", "r")
    teams = fin.readlines()
    output = ""
    for team in teams:
        team = team.strip().split("||&&||")
        if team[0] == tname:
            team.append(uname + "\n")
        output += "||&&||".join(team)
    teams = open("../accounts/teams.txt", "w")
    teams.write(output)

def submitNewTeam(inputs):
    if "uname" not in inputs or "upass" not in inputs or "upass_conf" not in inputs or "join_id" not in inputs or "join_pass" not in inputs:
        return "Something is missing"
    uname = inputs.getvalue("uname").strip()
    upass = inputs.getvalue("upass").strip()
    upass_conf = inputs.getvalue("upass_conf").strip()
    team = inputs.getvalue("join_id")
    team_pass = inputs.getvalue("join_pass")

    if uname == None or uname == "":
        return "Please enter a team name"
    if "||&&||" in uname:
        return "Invalid username"
    if upass != upass_conf:
        return "Passwords do not match"
    if upass.strip() == "" or upass == None:
        return "Please enter a password"
    if len(upass) < 8:
        return "Password should be at least 8 or more characters"
    if not validateTeam(team, team_pass):
        return "Invalid team credentials"
    if fullTeam(team):
        return "That team is full"
    if alreadyOnTeam(team, uname):
        return "You are already on that team"

    joinTeam(team, uname)
    addUser(uname, upass)
    return "Success!"

print submitNewTeam(inputs)
