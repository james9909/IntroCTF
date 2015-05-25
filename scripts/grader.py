def correct(points, message):
    return {"status": 1, "points": points, "message": message}

def incorrect(message):
    return {"status": 0, "points": 0, "message": message}

def grade(pid, flag):
    if pid == "1":
        if flag == "flag":
            return correct(100, "Congratulations on your first crypto problem!")
        else:
            return incorrect("Incorrect :(")
    if pid == "2":
        if flag == "flag":
            return correct(100, "ay lmao")
        else:
            return incorrect("Incorrect :(")
    if pid == "3":
        if flag == "flag":
            return correct(100, "correct")
        else:
            return incorrect("Incorrect :(")
    if pid == "4":
        if flag == "flag":
            return correct(100, "good job")
        else:
            return incorrect("Incorrect :(")
