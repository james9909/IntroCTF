#!/usr/bin/python

import cgi, cgitb, hashlib

cgitb.enable()

print "Content-Type: text/html"
print ""

inputs = cgi.FieldStorage()
    
def login(tid):
    tid = inputs["tid"].value
    token = hashlib.sha1(tid).hexdigest()
#    print """<script>
#    document.cookie = 'token=%s; expires=Thu, 2 Aug 9001 20:47:11 UTC; path=/';
#    document.cookie = 'uid=%s; expores=Thu, 2 Aug 9001 20:47:11 UTC; path=/';
#    </script>
#    """ % (token, tid)
    return "%s,%s" %(token, tid)

print login(inputs)
