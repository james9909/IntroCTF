#!/usr/bin/python

print "Content-Type: text/html\n"

import cgi, hashlib, os, cgitb
from time import strftime, localtime, time
cgitb.enable()

html = open('template.html', 'r').read()
print html

hashed = hashlib.sha1()
status = 0

inputs = cgi.FieldStorage()

if "team" not in inputs or "pass" not in inputs:
    status = 1

if status != 1:
    team = inputs["team"].value
    password = inputs["pass"].value

    login_list = open("login_list.txt", "r+w")
    read_login = login_list.read()

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

    # Passwords don't match
    if password != user_dict[team]:
        status = 1

if status == 0:
    add_info = "\n%s,yes" %(team)
    login_list.write(read_login + add_info)
    team = hashlib.sha1(team + "salt").hexdigest()
    # Use cookies
    print """<script>
    document.cookie = 'team=%s; expires=Thu, 2 Aug 9001 20:47:11 UTC; path=/';
    </script>
    """ % (team)
    print "Logged in!"

elif status == 1:
    print "Invalid credentials, please <a href='../login.html'>try again</a>"

print "</body>"
print "</html>"
