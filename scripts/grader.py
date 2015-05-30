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
            return correct(20, "Wasn't that easy?")
        else:
            return incorrect("Incorrect :(")
    if pid == "1":
        if flag == "how_many_bases?":
            return correct(30, "Nice!")
        else:
            return incorrect("Incorrect :(")
    if pid == "2":
        if flag == "hotspootsalt":
            return correct(55, "Pls dont hax hotspoot")
        else:
            return incorrect("Incorrect :(")
    if pid == "3":
        if flag == "flag":
            return correct(100, "good job")
        else:
            return incorrect("Incorrect :(")
