#!/usr/bin/env python


def gen_scoreboard(team_data):
    if len(team_data) == 0:
        print "No team has scored any points yet!"
    else:
        print "<tr><th>Team</th><th>Points</th></tr>"
        length = len(team_data)
        for x in range(length):
            if len(team_data) == 0:
                return
            highest_score = max(team_data.values())
            for team in team_data:
                if team_data[team] == highest_score:
                    print "<tr><td>%s</td><td>%s</td></tr>\n" %(team, highest_score)
                    del team_data[team]
                    break

def main():
    fin = open("users.txt", "r")
    data = fin.readlines()
    teams = {}
    # Data is stored team,pass,score,time,problems,solved,after
    for info in data:
        teams[info[0]] = info[2]
    gen_scoreboard(teams)

html = open("templates/logged_out.html").read()
print html
main()
