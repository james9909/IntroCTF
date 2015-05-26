def correct(points, message):
    return {"status": 1, "points": points, "message": message}

def incorrect(message):
    return {"status": 0, "points": 0, "message": message}

def grade(pid, flag):
    pid = str(pid)
    if pid == "9001":
        if flag == "introductions_are_cool":
            return correct(5, "Welcome to IntroCTF!")
        else:
            return incorrect("Come on, try again!")
    if pid == "0":
        if flag == "caesar_is_easy":
            return correct(40, "Correct!")
        else:
            return incorrect("Incorrect :(")
    if pid == "1":
        if flag == "flag":
            return correct(100, "ay lmao")
        else:
            return incorrect("Incorrect :(")
    if pid == "2":
        if flag == "flag":
            return correct(100, "correct")
        else:
            return incorrect("Incorrect :(")
    if pid == "3":
        if flag == "flag":
            return correct(100, "good job")
        else:
            return incorrect("Incorrect :(")
