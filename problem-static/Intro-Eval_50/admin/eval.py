#!/usr/bin/python2.7

import sys, random

# No sus things :)
del __builtins__.__dict__['__import__']
del __builtins__.__dict__['reload']
del __builtins__.__dict__['open']
del __builtins__.__dict__['file']
del __builtins__.__dict__['execfile']
del __builtins__.__dict__['eval']

flag = "eval_is_fun"

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

def gen_serial():
    return "".join([str(random.randrange(10)) for x in range(random.randrange(10, 20))])
    
def main():
    a = gen_serial()
    x = raw_input("Prove that you are not a robot by typing in the second following serial: %s %s >> " %(gen_serial(), a))
    if x == a:
    
        print "Welcome to the flag database! We are currently under construction. Please do not hack the flags."
        try:
            command = str(input("What would you like to do? "))
            print command
        except Exception, e:
            print "Invalid command!"
            return
    else: 
        print "Wrong!"
        return

main()
