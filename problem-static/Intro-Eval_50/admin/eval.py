
#!/usr/bin/python

del __builtins__.__dict__['__import__']
del __builtins__.__dict__['reload']

flag = "eval_is_fun"

def main():
    print "Hi, welcome to the flag database. We are under construction right now, so you cannot view the flags, or do anything."
    while True:
        command = input("What would you like to do? ")
        try:
            print "Executing command: %s" %(command)
            exec(command)
        except:
            print "Invalid command"

main()