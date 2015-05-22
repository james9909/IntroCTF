#!/usr/bin/python

print "Content-Type: text/html\n"

import cgi, hashlib, os, cgitb
from time import strftime, localtime, time
cgitb.enable()

hashed = hashlib.sha1()

def login_status(inputs):
    status = 0

    if "team" not in inputs or "pass" not in inputs:
        status = 1

    if status != 1:
        team = inputs["team"].value
        password = inputs["pass"].value

        login_list = open("login_list.txt", "r+w")
        read_login = login_list.read()

        # Team info
        user_info = open("user_info.txt", "r+w")
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
        hashed.update(password)
        password = hashed.hexdigest()

        # Passwords don't match
        if password != user_dict[team]:
            status = 1

        return status

def main():
    inputs = cgi.FieldStorage()

    if login_status(inputs) == 0:

        add_info = "\n%s,yes" %(team)
        login_list.write(read_login + add_info)

        # Use cookies
        print """<script>
        document.cookie = 'team=%s; expires=Thu, 2 Aug 9001 20:47:11 UTC; path=/';
        </script>
        """ % (team)
        print "Logged in!"

    elif status == 1:
        print "Invalid credentials, please <a href='../login.html'>try again</a>"

html = open('template.html', 'r').read()
print html
main()

print "</body>"
print "</html>"
