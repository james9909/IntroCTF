import os

print "Content-Type: text/html\n"

print os.environ["QUERY_STRING"]
