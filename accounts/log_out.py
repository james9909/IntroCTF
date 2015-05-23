#!/usr/bin/python

print "Content-Type: text/html\n"


import os, hashlib

# Remove team from logged in teams
def logout(team):
    login = open("login_list.txt", "r")
    login_data = login.read()
    login_list = login_data.split("\n")

    while "" in login_list:
        login_list.remove("")

    new_login = ""
    for login in login_list:
        if hashlib.sha1(login + "salt").hexdigest() != team:
            new_login += "\n" + login

    login = open("login_list.txt", "w")
    login.write(new_login)

if "HTTP_COOKIE" not in os.environ:
    html = open("template.html", "r").read()
    print html

    print "You aren't logged in!<br>"
    print "Log in <a href=../login.html>here</a>"
else:
    html = open("redirect.html", "r").read()
    print html
    team = os.environ['HTTP_COOKIE']
    team = team[5:]

    logout(team)
    # Use cookies
    print """<script>
    document.cookie = 'team=; expires=Thu, 01, Jan 1970 00:00:01 GMT; path=/;';
    </script>"""

    print "Logged out"

print "</body>"
print "</html>"
