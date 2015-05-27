#!/usr/bin/python

import cgi, cgitb, hashlib
from grader import grade

cgitb.enable()

print "Content-Type: text/html"
print ""

inputs = cgi.FieldStorage()

def alreadySolved(uid, pid):
    users = open("../accounts/users.txt", "r")
    solved = users.readlines()
    for problems in solved:
        problems = problems.strip()
        # Get only solved problems
        problems = problems.split(",")
        if problems[0] == uid:
            problems = problems[2:]
            if pid in problems:
                return True
    return False

def writeSolved(uid, pid):
    users = open("../accounts/users.txt", "r")
    solved = users.readlines()
    while "\n" in solved:
        solved.remove("\n")

    new_data = ""
    for data in solved:
        data = data.strip()
        data = data.split(",")
        if data[0] == uid:
            data.append(pid)
        data = ",".join(data)
        new_data += data + "\n"
    users = open("../accounts/users.txt", "w")
    users.write(new_data)

def addScore(uid, score):
    scores = open("../accounts/scores.txt", "r")
    data = scores.readlines()
    while "\n" in data:
        data.remove("\n")

    new_data = ""
    for user in data:
        user = user.split(",")
        if user[0] == uid:
            user[1] = int(user[1])
            user[1] += score
            user[1] = str(user[1])

        user = ",".join(user)
        new_data += user + "\n"

    users = open("../accounts/scores.txt", "w")
    users.write(new_data)

def handle_submit(inputs):
    return inputs
    uid = inputs.getvalue("uid")
    pid = inputs.getvalue("pid")
    flag = inputs.getvalue("flag")
    token = inputs.getvalue("token")

    if uid == None or uid == "undefined":
        return "Log in to submit flags!"
    if alreadySolved(uid, pid):
        return "You have already solved this problem!"
    if pid == None or pid == "undefined":
        return "Problem id not found"
    if flag == None or flag == "":
        return "Flag cannot be empty"
    confirm = hashlib.sha1(uid).hexdigest()
    if confirm != token:
        return "You are not who you say you are!"

    response = grade(pid, flag)

    if response["status"] == 1:
        writeSolved(uid, pid)
        addScore(uid, response["points"])
        return response["message"]

    return response["message"]

print handle_submit(inputs)
