#!/usr/bin/python

import sys
from select import select

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

def wait_for_input(timeout):
    '''Wait for user input for timeout seconds'''
    rlist, _, _ = select([sys.stdin], [], [], timeout)
    if rlist:
        ans = sys.stdin.readline().strip()
        return ans
    else:
        print "Too slow!"
        sys.exit(0)

print "Welcome to fast math! Here, we will be testing your abilities to math fast"
raw_input("Press any key to continue....")

print "Problem 1: What is 120958 + 167063?"
print "You have 5 seconds to answer:"
ans = wait_for_input(5)

if ans != "288021":
    print "Incorrect!"
    sys.exit(0)
print "Correct!"

print "Problem 2: What is the square root of 876543212365? (6 Decimal Places)"
print "You have 4 seconds to answer:"
ans = wait_for_input(4)

if ans != "936238.865015":
    print "Incorrect!"
    sys.exit(0)
print "Correct!"

print "You are good, but let's step up it up"
raw_input("Press any key to continue to stage 2....")

print "Problem 3: Digit sum of the 1000th Fibonacci number."
print "You have 3 seconds to answer:"
ans = wait_for_input(3)

if ans != "1005":
    print "Incorrect!"
    sys.exit(0)
print "Correct!"

print "Problem 4: How many permutations are there of a 2x2x2 rubik's cube?"
print "You have 3 seconds to answer:"
ans = wait_for_input(5)

if str(int(float(ans))) != "88179840": #8! * 3^7
    print "Incorrect!"
    sys.exit(0)
print "Correct!"

print "Final stretch"
raw_input("Press any key to continue to stage 3....")

if ans != "1002242216651368":
    print "Incorrect!"
    sys.exit(0)
