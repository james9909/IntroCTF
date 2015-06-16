#!/usr/bin/python

import cgi, cgitb, hashlib

cgitb.enable()

print "Content-Type: text/html"
print ""
inputs = cgi.FieldStorage()

def verify(inputs):
    if "uname" not in inputs or "upass" not in inputs:
        return "Invalid credentials"
    uname = inputs["uname"].value
    upass = inputs["upass"].value

    fin = open("../accounts/users.txt")
    users = fin.readlines()
    hashed = hashlib.sha1(upass + "salt").hexdigest()
    for data in users:
        data = data.split("||&&||")
        if uname == data[0]:
            if hashed == data[1].strip():
                return "Success!"
    return "Invalid credentials"

print verify(inputs)
