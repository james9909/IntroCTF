#!/usr/bin/python

print "Content-Type: text/html\n"

import cgi, hashlib, os, cgitb
from time import strftime, localtime, time
cgitb.enable()

hashed = hashlib.sha1()

def login_status(inputs):
    status = 0
    if "team" not in inputs or "pass" not in inputs or "confirm_pass" not in inputs:
        status = 4

    if status != 4:
        if not inputs["team"].value.isalnum() or not inputs["pass"].value.isalnum():
            status = 3

    if status < 3:
        newTeam = inputs["team"].value
        newPassword = inputs["pass"].value
        confirmNewPass = inputs["confirm_pass"].value

        users = open("users.txt", "r+w")
        read_info = users.read()
        user_list1 = read_info.split("\n")
        user_list2 = []
        user_dict = {}

        # Separate team names and password
        for info in user_list1:
            user_list2.append(info.split(","))

        # Remove empty strings that will throw errors later on
        while [""] in user_list2:
            user_list2.remove([""])

        # Link team names and password
        for info in user_list2:
            user_dict[info[0]] = info[1]

        if newPassword != confirmNewPass:
            status = 2

        if newTeam in user_dict:
            status = 1
    return status

def main():
    inputs = cgi.FieldStorage()
    if login_status(inputs) == 0:
        # Hash password for higher security
        newPassword = inputs["pass"].value
        hashed.update(newPassword)
        newPassword = hashed.hexdigest()
        newTeam = inputs["team"].value

        new_user = "%s,%s" %(newTeam, newPassword)
        users = open("users.txt", "w")
        scores = open("scores.txt", "w")

        scores.write(newTeam + ",0")
        users.write(new_user)
        print "Thank you for registering! </br><a href='../index.html'>Return Home</a>"

    elif status == 1:
        print "Team name is taken, <a href='../register.html'>try again</a>"

    elif status == 2:
        print "Passwords do not match, <a href='../register.html'>try again</a>"

    elif status == 3:
        print "Please user alphanumeric characters, <a href='../register.html'>try again</a>"

    elif status == 4:
        print "Something is missing ...<a href='../register.html'>try again</a>"

html = open('../templates/logged_out.html', 'r').read()
print html
main()

print "</body>"
print "</html>"
