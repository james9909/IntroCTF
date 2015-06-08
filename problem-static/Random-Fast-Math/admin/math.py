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
    # Generate a random number of digits length
    return int("".join([random.choice(nums) for x in range(digits)]))

sys.stdout = UnbufferedStream(sys.stdout)
print "Welcome to random math! Here, we will be testing your abilities to math fast with random problems.\nYou get 0.1 seconds to solve each of these easy math problems"
a = random_gen(5)
b = random_gen(5)
prob = "%d + %d" %(a, b)
print prob

ans = wait_for_input(.1)
if ans != str(eval(prob)):
    print "Incorrect!"
    sys.exit(0)
print "Correct!"

a = random_gen(8)
b = random_gen(8)
c = random_gen(8)
prob = "%d & %d * %d" %(a, b, c)
print prob

ans = wait_for_input(.1)
if ans != str(eval(prob)):
    print "Incorrect!"
    sys.exit(0)
print "Correct!"

a = random_gen(15)
b = random_gen(15)
c = random_gen(15)
prob = "(%d ** 2 + 4 * %d) * (%d + %d)" %(a, b, c, random.choice([a, b, c]))
print prob 
ans = wait_for_input(.1)
if ans != str(eval(prob)):
    print "Incorrect!"
    sys.exit(0)
print "Correct!"

a = random_gen(random_gen(1))
b = random_gen(random_gen(1))
c = random_gen(random_gen(1))

prob = "((%d * %d + %d + %d) + (%d & %d ^ %d) ) * .5" %(random.choice([a, b, c]), random.choice([a, b, c]), random.choice([a, b, c]), random.choice([a, b, c]), random.choice([a, b, c]), random.choice([a, b, c]), random.choice([a, b, c]))
print prob
ans = wait_for_input(.1)

if ans != str(eval(prob)):
    print "Incorrect!"
    sys.exit(0)

print "Congratulations! You are fast! The flag is wish_i_can_math_this_fast"
