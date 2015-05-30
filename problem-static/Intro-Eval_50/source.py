#!/usr/bin/python2.7

del __builtins__.__dict__['__import__']
del __builtins__.__dict__['reload']

flag = "XXXXXXXXXXXXX"

def main():
    print "Hi, welcome to the flag database. We are under construction right now, so you cannot view the flags, or do anything."
    while True:
        command = raw_input("What would you like to do? ")
        try:
            result = eval(command)
            print "Here is the result of your command: %s" %(result)
        except:
            print "Invalid command, try again"

main()
