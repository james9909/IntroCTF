#!/usr/bin/python2.7

import sys, random

# No sus things :)
del __builtins__.__dict__['__import__']
del __builtins__.__dict__['reload']
del __builtins__.__dict__['open']
del __builtins__.__dict__['file']
del __builtins__.__dict__['execfile']
del __builtins__.__dict__['eval']

flag = "random_fun"

# Ignore this, just used to print to stdout
class UnbufferedStream(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

choices = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
def random_serial():
    serial = ""
    for x in range(24):
        serial += random.choice(choices)
    return serial

def check_serial(serial, guess):
    status = ""
    for x in range(len(serial)):
        if serial[x] == guess[x]:
            status = status + "1"
        else:
            status = status + "0"
    return status

sys.stdout = UnbufferedStream(sys.stdout)
def main():
    print "-----Random Serial Generator------"
    print "Guess the 24 character serial that I've come up with, and you win!"
    print "I will tell you which characters are right"
    serial = random_serial()
    print "SERIAL GENERATED!!!"
    while True:
        guess = str(input("What is your guess?\n> "))
        if len(guess) != 24:
            print "Not even the right length!"
            continue

        print "Here are the results:"
        print guess
        print check_serial(serial, guess)

        if guess == serial:
            print "You win!"
            sys.exit(0)

main()
