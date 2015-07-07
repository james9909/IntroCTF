#!/usr/bin/python

import cgi, cgitb, hashlib,datetime, time
from grader import grade

cgitb.enable()

print "Content-Type: text/html"
print ""

inputs = cgi.FieldStorage()

def logTime():
#    now = datetime.datetime.today()
#    absClock = (now.hour * 3600 + now.minute * 60 + now.second) * 1000000 + now.microsecond
#    return [now.day,absClock,now.hour,now.minute,now.second]
     return int(time.time() * 1000)

def alreadySolved(uid, pid):
    users = open("../accounts/solved.txt", "r")
    solved = users.readlines()
    for problems in solved:
        problems = problems.strip()
        # Get only solved problems
        problems = problems.split("||&&||")
        if problems[0] == uid:
            problems = problems[1:]
            if pid in problems:
                return True
    return False

def writeSolved(uid, pid):
    users = open("../accounts/solved.txt", "r")
    solved = users.readlines()
    while "\n" in solved:
        solved.remove("\n")

    new_data = ""
    for data in solved:
        data = data.strip()
        data = data.split("||&&||")
        if data[0] == uid:
            data.append(pid)
        data = "||&&||".join(data)
        new_data += data + "\n"
    users = open("../accounts/solved.txt", "w")
    users.write(new_data)
    
    scores = open("../accounts/scores.txt", "r").readlines()
    new = ""
    for score in scores:
        score = score.strip().split("||&&||")
        if score[0] == uid:
            score.append(str(logTime()))
        new += "||&&||".join(score) + "\n"
    scores = open("../accounts/scores.txt", "w")
    scores.write(new)

def addScore(uid, score):
    scores = open("../accounts/scores.txt", "r")
    data = scores.readlines()
    while "\n" in data:
        data.remove("\n")

    new_data = ""
    for user in data:
        user = user.strip().split("||&&||")
        if user[0] == uid:
            curr_score = int(user[-2])
            new_score = curr_score + score
            user.append(str(new_score))

        user = "||&&||".join(user)
        new_data += user + "\n"

    users = open("../accounts/scores.txt", "w")
    users.write(new_data)

def handle_submit(inputs):
    return "The competition has ended!"
    uid = inputs.getvalue("tid")
    pid = inputs.getvalue("pid")
    flag = inputs.getvalue("flag")
    token = inputs.getvalue("token")
    confirm = hashlib.sha1(uid + "salt").hexdigest()

    if uid == None or uid == "undefined":
        return "Log in to submit flags!"
    if confirm != token:
        return "You are not who you say you are!"
    if alreadySolved(uid, pid):
        return "You have already solved this problem!"
    if pid == None or pid == "undefined":
        return "Problem id not found"
    if flag == None or flag == "":
        return "Flag cannot be empty"

    response = grade(pid, flag)

    if response["status"] == 1:
        addScore(uid, response["points"])
        writeSolved(uid, pid)
        return response["message"]

    return response["message"]

print handle_submit(inputs)
