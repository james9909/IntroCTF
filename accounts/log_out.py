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
                <a href=".." class="brand-logo">IntroCTF</a>
                <ul class="right hide-on-med-and-down">

                    <li><a href="../">Home</a></li>
                    <li><a href="../scoreboard">Scoreboard</a></li>
                    <li><a href="../problems">Problems</a></li>
                    <li><a href="../about">About</a></li>
                    <li><a href="../login.html">Login</a></li>
                    <li><a href="../register.html">Register</a></li>

                    <!-- <li><a class="mdi-action-info-outline modal-trigger" href="#helpmodal"></a></li> -->
                </ul>
                <ul id="nav-mobile" class="side-nav">

                    <li><a class="waves-effect waves-indigo" href="../">Home</a></li>
                    <li><a class="waves-effect waves-indigo" href="../scoreboard">Scoreboard</a></li>
                    <li><a class="waves-effect waves-indigo" href="../problems">Problems</a></li>
                    <li><a class="waves-effect waves-indigo" href="../about">About</a></li>
                    <li><a class="waves-effect waves-indigo" href="../login.html">Login</a></li>
                    <li><a class="waves-effect waves-indigo" href="../register.html">Register</a></li>

                    <!-- <li><a class="waves-effect waves-indigo modal-trigger" href="#helpmodal"><i class="mdi-action-info-outline"></i></a></li> -->
                </ul>
                <a class="button-collapse" href="#" data-activates="nav-mobile"><i class="mdi-navigation-menu"></i></a>
            </div>
        </nav>
"""

import os
login_list = open("login_list.txt", "r+w")

if "HTTP_COOKIE" not in os.environ:
    print "You aren't logged in!<br>"
    print "Log in <a href=../login.html>here</a>"
else:
    team = os.environ['HTTP_COOKIE']
    team = team[5:]

    add_info = "\n%s,no" %(team)
    login_list.write(add_info)

    # Use cookies
    print """<script>
    document.cookie = 'team=; expires=Thu, 01, Jan 1970 00:00:01 GMT; path=/;';
    </script>"""

    print "Logged out"

print "</body>"
print "</html>"
