import sys

flag = "{flag}"

def validate(key):
    if key == flag:
        return True, "Correct!"
    else:
        return False, "Incorrect :("

print validate(sys.argv[1])
