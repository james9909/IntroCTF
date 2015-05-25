#!/usr/bin/env python

import os
print "Content-Type: text/html\n"
print ""

def gen_scoreboard(team_data):
    if len(team_data) == 0:
        print "There are no teams!"
    else:
        print "<br>"
        print "<div class='container'>"
        print "<table class='responsive-table bordered hoverable centered'>"
        print "<thead>"
        print "<tr><th>Rank</th><th>Team</th><th>Score</th></tr>"
        print "</thead>"
        length = len(team_data)
        for x in range(length):
            if len(team_data) == 0:
                return
            highest_score = max(team_data.values())
            for team in team_data:
                if team_data[team] == highest_score:
                    print "<tr><td>%d</td><td>%s</td><td>%s</td></tr>\n" %(x+1, team, highest_score)
                    del team_data[team]
                    break

def main():
    fin = open("accounts/scores.txt", "r")
    data = fin.readlines()
    teams = {}
    # Data is stored team,score
    for info in data:
        info = info.strip().split(",")
        teams[info[0]] = info[1]
    gen_scoreboard(teams)

if 'HTTP_COOKIE' not in os.environ:
    html = open("templates/scoreboard_logged_out.html").read()
else:
    html = open("templates/scoreboard_logged_in.html").read()

print html
main()
