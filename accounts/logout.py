#!/usr/bin/python

print "Content-Type: text/html\n"


import os, hashlib

def getCookie(name):
    cookies = os.environ["HTTP_COOKIE"]
    cookies = cookies.split(";")
    for cookie in cookies:
        cookie = cookie.split("=")
        if cookie[0].strip() == name:
            return cookie[1]
    return None

# Remove team from logged in teams
def logout(team):
    login = open("login_list.txt", "r")
    login_data = login.read()
    login_list = login_data.split("\n")

    while "" in login_list:
        login_list.remove("")

    new_login = ""
    for login in login_list:
        if hashlib.sha1(login).hexdigest() != team:
            new_login += "\n" + login

    login = open("login_list.txt", "w")
    login.write(new_login)

if "HTTP_COOKIE" not in os.environ:
    html = open("../templates/logout_logged_out.html", "r").read()
    print html

    print "You aren't logged in!<br>"
    print "Log in <a href=../login>here</a>"
else:
    html = open("../templates/logout_logged_in.html", "r").read()
    print html
    team = getCookie("token")
    logout(team)
    # Use cookies
    print """<script>
    document.cookie = 'token=; expires=Thu, 01, Jan 1970 00:00:01 GMT; path=/;';
    document.cookie = 'uid=; expires=Thu, 01, Jan 1970 00:00:01 GMT; path=/;';
    </script>"""

    print "Logged out"

print "</body>"
print "</html>"
