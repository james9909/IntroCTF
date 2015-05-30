#!/usr/bin/python2.7

import sys

del __builtins__.__dict__['__import__']
del __builtins__.__dict__['reload']

flag = "eval_is_fun"

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
    while True:
        print "Welcome to the flag database! We are currently under construction. Please do not hack the flags."
        try:
            command = str(raw_input("What would you like to do? "))
            result = str(eval(command))
            print "This is the result: %s" %(result)
        except Exception, e:
            print "Invalid command!!!! EXITING!!!!!"
            return

main()