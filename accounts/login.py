#!/usr/bin/python

print "Content-Type: text/html\n"

import cgi, hashlib, os, cgitb
from time import strftime, localtime, time
cgitb.enable()


hashed = hashlib.sha1()
status = 0

inputs = cgi.FieldStorage()

def login(team):
    login = open("login_list.txt", "r")
    login_data = login.read()
    login_list = login_data.split("\n")

    for logged_in in login_list:
        if team in logged_in:
            return False
        login = open("login_list.txt", "w")
        login.write(login_data + team)
    return True

if "team" not in inputs or "pass" not in inputs:
    status = 1

if status != 1:
    team = inputs["team"].value
    password = inputs["pass"].value

    # Team info
    user_info = open("users.txt", "r+w")
    read_info = user_info.read()
    user_list1 = read_info.split("\n")
    user_list2 = []
    user_dict = {}

    # Separate team names and password
    for info in user_list1:
        user_list2.append(info.split(","))

    # Remove empty lists that will throw errors later on
    while [""] in user_list2:
        user_list2.remove([""])

    # Link team names and password
    for info in user_list2:
        user_dict[info[0]] = info[1]

    # Hash the password for sekurity
    password = hashlib.sha1(password).hexdigest()

    # Team isn't even registered or passwords dont match
    if team not in user_dict or password != user_dict[team]:
        status = 1

if status == 0:
    if login(team):

        html = open("../templates/logged_in.html", "r").read()
        print html
        token = hashlib.sha1(team).hexdigest()
        # Use cookies
        print """<script>
        document.cookie = 'token=%s; expires=Thu, 2 Aug 9001 20:47:11 UTC; path=/';
        document.cookie = 'uid=%s; expores=Thu, 2 Aug 9001 20:47:11 UTC; path=/';
        </script>
        """ % (token, team)
    else:
        html = open("../templates/logged_out.html", "r").read()
        print html
        print "Already logged in!"

elif status == 1:
    html = open("../templates/logged_out.html", "r").read()
    print html
    print "Invalid credentials, please <a href='../login.html'>try again</a>"

print "</body>"
print "</html>"
