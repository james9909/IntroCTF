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
    if "uname" not in inputs or "upass" not in inputs:
        return "Invalid credentials"
    uname = inputs["uname"].value
    upass = inputs["upass"].value
    if alreadyLoggedIn(uname):
        return "Already logged in"

    fin = open("../accounts/users.txt")
    users = fin.readlines()
    hashed = hashlib.sha1(upass).hexdigest()
    for data in users:
        data = data.split("||&&||")
        if uname == data[0]:
            if hashed == data[1].strip():
                writeLogin(uname)
                return "Success!"
    return "Invalid credentials"

print verify(inputs)
