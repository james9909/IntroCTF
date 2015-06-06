import sys
from select import select

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
print "You have 5 second to answer:"
ans = wait_for_input(5)

if ans != "288021":
    print "Incorrect!"
    sys.exit(0)

print "Problem 2: What is the square root of 876543212365?"
print "You have 4 seconds to answer:"
ans = wait_for_input(4)

if ans != "936238.865015":
    print "Incorrect!"
    sys.exit(0)

print "You are good, but let's step up it up"
raw_input("Press any key to continue to stage 2....")

print "Problem 3: pls joel gimme math problem"
print "You have x seconds to answer:"
ans = wait_for_input(x)

if ans != gimmecorrectansjoel:
    print "Incorrect!"
    sys.exit(0)

