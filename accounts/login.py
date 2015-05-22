#!/usr/bin/python

print "Content-Type: text/html\n"
print """
<!DOCTYPE html>
<html>
    <head>
        <!--Import materialize.css-->
        <link type="../text/css" rel="stylesheet" href="../css/materialize.min.css"  media="screen,projection"/>

        <!--Let browser know website is optimized for mobile-->
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>

        <title>IntroCTF - Login</title>
    </head>

    <body>
        <!--Import jQuery before materialize.js-->
        <script type="../text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
        <script type="../text/javascript" src="../js/materialize.min.js"></script>

        <nav role="navigation" style="background-color: #009688">
            <div class="nav-wrapper container">
                <a href="#" class="brand-logo">IntroCTF</a>
                <ul class="right hide-on-med-and-down">

                    <li><a href="../">Home</a></li>
                    <li><a href="../scoreboard">Scoreboard</a></li>
                    <li><a href="../problems">Problems</a></li>
                    <li><a href="../about">About</a></li>
                    <li><a href="./login.html">Login</a></li>
                    <li><a href="./register.html">Register</a></li>

                    <!-- <li><a class="mdi-action-info-outline modal-trigger" href="#helpmodal"></a></li> -->
                </ul>
                <ul id="nav-mobile" class="side-nav">

                    <li><a class="waves-effect waves-indigo" href="../">Home</a></li>
                    <li><a class="waves-effect waves-indigo" href="../scoreboard">Scoreboard</a></li>
                    <li><a class="waves-effect waves-indigo" href="../problems">Problems</a></li>
                    <li><a class="waves-effect waves-indigo" href="../about">About</a></li>
                    <li><a class="waves-effect waves-indigo" href="./login.html">Login</a></li>
                    <li><a class="waves-effect waves-indigo" href="./register.html">Register</a></li>

                    <!-- <li><a class="waves-effect waves-indigo modal-trigger" href="#helpmodal"><i class="mdi-action-info-outline"></i></a></li> -->
                </ul>
                <a class="button-collapse" href="#" data-activates="nav-mobile"><i class="mdi-navigation-menu"></i></a>
            </div>
        </nav>
    </body>
</html>
"""

import cgi, hashlib, os, cgitb
from time import strftime, localtime, time
cgitb.enable()

hashed = hashlib.sha1()
status = 0

inputs = cgi.FieldStorage()

if "team" not in inputs or "pass" not in inputs:
    status = 1

if status != 1:
    team = inputs["team"].value
    password = inputs["pass"].value

    # Team info
    user_info = open("user_info.txt", "r+w")
    read_info = user_info.read()
    user_list1 = read_info.split("\n")
    user_list2 = []
    user_dict = {}

    # Recent log ins
    login_list = open("login_list.txt", "r+w")
    log = login_list.read()
    log = log[::-1] # Read in reverse so we can find most recent login
    logList = log.split("\n")
    logList2 = []

    while "" in logList:
        logList.remove("")

    # Reverse elements to account for above
    for element in logList:
        logList2.append(element[::-1])

    logged_in = ""

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

if status == 0:
    add_info = "\n%s,yes" %(team)
    login_list.write(add_info)
    # Use cookies
    print """<script>
    document.cookie = 'team=%s; expires=Thu, 2 Aug 9001 20:47:11 UTC; path=/';
    </script>
    """ % (team)
    print "<meta http-equiv='refresh'>"

elif status == 1:
    print "Invalid credentials, please <a href='login.html'>try again</a>"

print "</body>"
print "</html>"
