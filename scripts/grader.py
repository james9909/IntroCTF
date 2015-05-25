def correct(points, message):
    return {"status": 1, "points": points, "message": message}

def incorrect(message):
    return {"status": 0, "points": 0, "message": message}

def grade(pid, flag):
    if pid == 1:
        if flag == "crypto_is_ez":
            return correct(100, "Congratulations on your first crypto problem!")
        else:
            return incorrect("Incorrect :(")
