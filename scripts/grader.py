def correct(points, message):
    return {"status": 1, "points": points, "message": message}

def incorrect(message):
    return {"status": 0, "points": 0, "message": message}

def grade(pid, flag):
    pid = str(pid)
    if pid == "intro":
        if flag == "introductions_are_cool":
            return correct(5, "Welcome to IntroCTF!")
        else:
            return incorrect("Come on, try again!")
    if pid == "caesar":
        if flag == "caesar_is_easy":
            return correct(20, "Wasn't that easy?")
        else:
            return incorrect("Incorrect :(")
    if pid == "base":
        if flag == "how_many_bases?":
            return correct(30, "Nice!")
        else:
            return incorrect("Incorrect :(")
    if pid == "absent":
        if flag == "subs_are_great":
            return correct(40, "Subs are great!")
        else:
            return incorrect("Incorrect :(")
    if pid == "brutus":
        if flag == "unions3337":
            return correct(45, "Correct!")
        else:
            return incorrect("Incorrect :(")
    if pid == "bb":
        if flag == "br0k3n":
            return correct(80, "Correct!")
        else:
            return incorrect("Incorrect :(")
    if pid == "stego":
        if flag == "stegggoooooo":
            return correct(50, "LEGOOOOO!")
        else:
            return incorrect("Incorrect :(")
    if pid == "dot":
        if flag == "d0tf1l35":
            return correct(50, "Correct!")
        else:
            return incorrect("Incorrect :(")
    if pid == "corrupt":
        if flag == "corrupt_headers":
            return correct(60, "Correct!")
        else:
            return incorrect("Incorrect :(")
    if pid == "inverted":
        if flag == "color_swap":
            return correct(60, "Correct!")
        else:
            return incorrect("Incorrect :(")
    if pid == "rawr":
        if flag == "rawr_rar":
            return correct(60, "RAWWRRR!")
        else:
            return incorrect("Incorrect :(")
    if pid == "messy":
        if flag == "ripobfuscate":
            return correct(60, "RAWWRRR!")
        else:
            return incorrect("Incorrect :(")
