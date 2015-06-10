#!/usr/bin/python

import cgi, cgitb, hashlib

cgitb.enable()

print "Content-Type: text/html"
print ""

inputs = cgi.FieldStorage()
    
def login(tid):
    tid = inputs["tid"].value
    token = hashlib.sha1(tid).hexdigest()
    return "%s,%s" %(token, tid)

print login(inputs)
