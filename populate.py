import datetime
import problemdb
import random
import teamdb
import utils

words = open("/usr/share/dict/words", "r").read().split("\n")
categories = [
        'Algorithms',
        'Cryptography',
        'Web',
        'Forensics',
        'Reversing',
        ]

def random_words(number):
    return str(" ".join([word.decode("unicode_escape").encode("ascii", "ignore").capitalize() for word in random.sample(words, number)])).replace("'", "")

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

def random_date(start, end):
    return start + datetime.timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def main():
    num_problems = int(raw_input("How many problems would you like to create? "))
    for x in xrange(num_problems):
        problemdb.add_problem(generate_problem_name(), generate_sentence(), generate_hint(), generate_category(), generate_points(), "flag")

    num_teams = int(raw_input("How many teams would you like to create? "))
    for x in xrange(num_teams):
        base_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=-(60*num_problems))
        solved = []
        team_name = generate_team_name()
        teamdb.add_team(team_name, "password", str(utils.unix_time_millis(base_time)))
        problems = problemdb.get_problems()

        for x in xrange(random.randint(1, num_problems)):
            pid = random.choice(problems)[0]
            if pid not in solved:
                new_base = random_date(base_time, base_time + datetime.timedelta(minutes=60))
                problemdb.submit_flag(team_name, pid, "flag", str(utils.unix_time_millis(new_base)))
                base_time = new_base
                solved.append(pid)

if __name__ == '__main__':
    main()
