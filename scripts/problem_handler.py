#!/usr/bin/python

import cgi, cgitb
from grader import grade

cgitb.enable()

print "Content-Type: text/html"
print ""

inputs = cgi.FieldStorage()

def alreadySolved(uid, pid):
    users = open("accounts/users.txt", "r")
    solved = users.readlines()
    for problems in solved:
        # Get only solved problems
        problems = problems.split(",")
        problems = problems[2:]
        if pid in problems:
            return True
    return False

def writeSolved(uid, pid):
    users = open("accounts/users.txt", "r")
    solved = users.readlines()
    while "\n" in solved:
        solved.remove("\n")

    for data in solved:
        data = data.split(",")
        if data[0] == uid:
            data.append(pid)
        print data
        data = ",".join(data)
        users = open("accounts/users.txt", "w")
        users.write(data)

def handle_submit(inputs):
    result = {}
    # uid = inputs.getvalue("uid")
    # pid = inputs.getvalue("pid")
    # flag = inputs.getvalue("flag")
    uid = "oof"
    pid = "1"
    flag = "crypto_is_ez"

    correct = False
    if pid == "":
        return {"status": 0, "points": 0, "message": "Problem id not found"}
    if flag == "":
        return {"status": 0, "points": 0, "message": "Answer cannot be empty"}

    response = grade(1, "crypto_is_ez")

    if response["status"] == 1:
        if alreadySolved(uid, pid):
            return {"status": 0, "points": 0, "message": "You already solved this problem!"}
        writeSolved(uid, pid)
        return response

    return response

print handle_submit(inputs)
