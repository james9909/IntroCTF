import random
import teamdb
import problemdb

words = open("/usr/share/dict/words", "r").read().split("\n")
categories = [
        'Algorithms',
        'Cryptography',
        'Web',
        'Forensics',
        'Reversing',
        ]

def random_words(number):
    return str(" ".join(random.sample(words, number)))

def generate_sentence():
    return random_words(60)

def generate_team_name():
    return random_words(3)

def generate_problem_name():
    return random_words(5)

def generate_hint():
    return random_words(4)

def generate_points():
    return random.randint(10, 50) * 5

def generate_category():
    return random.choice(categories)

def generate_challenges(number):
    for x in range(number):
        problemdb.add_problem(generate_problem_name(), generate_sentence(), generate_hint(), generate_category(), generate_points(), "flag")

def generate_teams(number):
    for x in range(number):
        teamdb.add_team(generate_team_name(), "password")

def main():
    num = int(raw_input("How many challenges would you like to create? "))
    if num > 50:
        print "That's a lot of challenges..."
        return
    generate_challenges(num)
    num = int(raw_input("How many teams would you like to create? "))
    if num > 100:
        print "That's a lot of teams..."
        return
    generate_teams(num)

if __name__ == '__main__':
    main()
