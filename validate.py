#!/usr/bin/python

import cgi

print "Content-Type: text/html\n"
print ""

def validate(key):
    if key == flag:
        return True, "Correct!"
    else:
        return False, "Incorrect :("

flag = "flag"
form = cgi.FieldStorage()
key = form.getvalue("flag", "(no flag)")

key = cgi.escape(key)

print validate(key)
