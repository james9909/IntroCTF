import random

sid = ""
for length in range(50):
    sid += str(random.randint(0, 9))

print sid
