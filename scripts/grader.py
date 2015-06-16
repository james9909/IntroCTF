def correct(points, message):
    return {"status": 1, "points": points, "message": message + " [ +" + str(points) + " ]"}

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
        if flag == "how_many_bases?" or flag == "how_many_bases":
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
            return correct(55, "Correct!")
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
            return correct(75, "Good job!")
        else:
            return incorrect("Incorrect :(")
    if pid == "inspect":
        if flag == "you_pass_inspection":
            return correct(20, "Correct!")
        else:
            return incorrect("Incorrect :(")
    if pid == "cookie":
        if flag == "coookkkkiiiieeeee":
            return correct(35, "Delicious!")
        else:
            return incorrect("Incorrect :(")
    if pid == "hidden":
        if flag == "hidden_input_too_easy":
            return correct(40, "Correct!!")
        else:
            return incorrect("Incorrect :(")
    if pid == "get":
        if flag == "i_dont_get_it":
            return correct(45, "Do you get it?")
        else:
            return incorrect("Incorrect :(")
    if pid == "spoof":
        if flag == "wasnt_that_easy":
            return correct(70, "Correct!")
        else:
            return incorrect("Incorrect :(")
    if pid == "sets":
        if flag == "9046":
            return correct(50,"ARML 2009 #10")
        else:
            return incorrect("Incorrect :(")
    if pid == "donttrip":
        if flag == "6580.5":
            return correct(60, "What a friend")
        else:
            return incorrect("Incorrect :(")
    if pid == "indif":
        if flag == "617":
            return correct(65, "Meh.")
        else:
            return incorrect("Incorrect :(")
    if pid == "fast":
        if flag == "wish_i_can_math_this_fast":
            return correct(70, "Dam you fast")
        else:
            return incorrect("Incorrect :(")
    if pid == "triangle":
        if flag == "167898753":
            return correct(85, "Nice")
        else:
            return incorrect("Incorrect :(")
    if pid == "overflow":
        if flag == "0v3rf10w":
            return correct(50, "Correct!")
        else:
            return incorrect("Incorrect :(")
    if pid == "eval":
        if flag == "eval_is_fun":
            return correct(50, "Correct!")
        else:
            return incorrect("Incorrect :(")
    if pid == "copy":
        if flag == "shoulda_been_my_final_project":
            return correct(55, "Correct!")
        else:
            return incorrect("Incorrect :(")
    if pid == "easy-rev":
        if flag == "that_wasnt_between_1_and_100":
            return correct(65, "Correct!")
        else:
            return incorrect("Incorrect :(")
    if pid == "rand-eval":
        if flag == "random_eval":
            return correct(65, "Correct!")
        else:
            return incorrect("Incorrect :(")
    if pid == "election":
        if flag == "not_rigged":
            return correct(75, "Correct!")
        else:
            return incorrect("Incorrect :(")
