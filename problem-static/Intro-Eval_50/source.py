#!/usr/bin/python2.7

import sys

# No sus things :)
del __builtins__.__dict__['__import__']
del __builtins__.__dict__['reload']
del __builtins__.__dict__['open']
del __builtins__.__dict__['file']
del __builtins__.__dict__['execfile']
del __builtins__.__dict__['eval']

flag = "XXXXXXXXXXXXXXXXXX"

# Ignore this, just used to print to stdout
class UnbufferedStream(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = UnbufferedStream(sys.stdout)
def main():
    print "Welcome to the flag database! We are currently under construction. Please do not hack the flags."
    while True:
        try:
            command = str(input("What would you like to do? "))
            print command
        except Exception, e:
            print "Invalid command!"
            continue

main()
