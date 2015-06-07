#!/usr/bin/python

import sys, random
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

def wait_for_input(timeout):
    '''Wait for user input for timeout seconds'''
    rlist, _, _ = select([sys.stdin], [], [], timeout)
    if rlist:
	ans = raw_input() 
        return ans
    else:
        print "Too slow!"
        sys.exit(0)

nums = "1234567890"
def random_gen(digits):
    return int("".join([random.choice(nums) for x in range(digits)]))

sys.stdout = UnbufferedStream(sys.stdout)
print "Welcome to random math! Here, we will be testing your abilities to math fast with random problems.\nYou get 2 seconds to solve each of these easy math problems"
a = random_gen(5)
b = random_gen(5)
print "%d + %d" %(a, b)

ans = wait_for_input(2)
if ans != str(a + b):
    print "Incorrect!"
    sys.exit(0)
print "Correct!"

a = random_gen(8)
b = random_gen(8)
c = random_gen(8)
print "%d / %d * %d" %(a, b, c)

ans = wait_for_input(2)
if ans != str(a / b * c):
    print "Incorrect!"
    sys.exit(0)
print "Correct!\n\
You are good, but let's step it up. You now have 0.5 seconds to solve each of the following:"

a = random_gen(10)
b = random_gen(10)
c = random_gen(10)
print "%d % %d + %d" %(a, b, c)

ans = wait_for_input(.5)
if ans != str(a % b + c):
    print "Incorrect!"
    sys.exit(0)
print "Correct!"

a = random_gen(15)
b = random_gen(15)
c = random_gen(15)
print "(%d ** 2 + 4 * %d) ** %d" %(a, b, c)

ans = wait_for_input(.5)
if ans != str((a ** 2 + 4 * b) ** d):
    print "Incorrect!"
    sys.exit(0)
print "Correct!"

print "Wow, you are fast, but can you beat this final stage? You get .1 seconds!"
a = random_gen(random_gen(3))
b = random_gen(random_gen(3))
c = random_gen(random_gen(3))

prob = "((%d * %d - %d ** %d) + (%d / %d & %d) ^ (%d + 2 * %d)) ** .5" %(random.choice([a, b, c]), random.choice([a, b, c]), random.choice([a, b, c]), random.choice([a, b, c]), random.choice([a, b, c]), random.choice([a, b, c]), random.choice([a, b, c]), random.choice([a, b, c]), random.choice([a, b, c]))
print prob
ans = wait_for_input(.1)

if ans != str(eval(prob)):
    print "Incorrect!"
    sys.exit(0)

print "Congratulations! You are fast! The flag is wish_i_can_math_this_fast"
