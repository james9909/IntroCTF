#!/usr/bin/python

print "Content-Type: text/html\n"
print """
<!DOCTYPE html>
<html>
    <head>
        <!--Import materialize.css-->
        <link type="text/css" rel="stylesheet" href="css/materialize.min.css"  media="screen,projection"/>

        <!--Let browser know website is optimized for mobile-->
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>

        <title>IntroCTF - Login</title>
    </head>

    <body>
        <!--Import jQuery before materialize.js-->
        <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
        <script type="text/javascript" src="js/materialize.min.js"></script>

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

if "team" not in inputs or "pass" not in inputs or "confirm_pass" not in inputs:
    status = 4

if status != 4:
    if not inputs["team"].value.isalnum() or not inputs["pass"].valie.isalnum():
        status = 3

if status < 3:
    newTeam = inputs["team"].value
    newPassword = inputs["pass"].value
    confirmNewPass = inputs["confirm_pass"]

    user_info = open("user_info.txt", "r+w").read()
    user_list1 = user_info.split("\n")
    user_list2 = []
    user_dict = {}

    # Separate team name and password
    for info in user_list1:
        user_list2.append(info.split(","))

    # Link team name and password
    for info in user_list2:
        user_dict[info[0]] = info[1]

    if newPassword != confirmNewPass:
        status = 2

    if newTeam in user_dict:
        status = 1

if status == 0:
    # Hash password for higher security
    hashed.update(NewPassword)
    newPassword = hashed.hexdigest()
    new_user = "\n%s,%s" %(newTeam, newPassword)
    user_info.write(new_user)
    print "Thank you for registering! </br><a href='../index.html'>Return Home</a>"
elif status == 1:
    print "Team name is taken, <a href='signUp.html'>try Again</a>"
elif status == 2:
    print "Passwords do not match, <a href='signUp.html'>try Again</a>"
elif status == 3:
    print "Please user alphanumeric characters, <a href='signUp.html'>try Again</a>"
elif status == 4:
    print "Something is missing ...<a href='signUp.html'>try Again</a>"

print "</body>"
print "</html>"
