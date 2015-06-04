import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def random_str():
    rand = ""
    for x in range(26):
        rand += random.choice(letters)
    return rand

def main():
    f = open("cookies.php", "w")
    cookies = ""
    for x in range(50):
        cookies += "setcookie(%s, %s, time() + (86400 * 90001), '/');\n" %(random_str(), random_str())
    f.write(cookies)

main()
