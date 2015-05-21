#!/usr/bin/python

import cgi

def grade(key):
    if key == flag:
        return True, "Correct!"
    else:
        return False, "Incorrect :("

flag = "flag"
form = cgi.FieldStorage()
key = form.getvalue("flag", "(no flag)")

key = cgi.escape(key)
