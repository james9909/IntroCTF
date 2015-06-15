#!/usr/bin/python

import os, operator, cgitb
print "Content-Type: text/html\n"
print ""

cgitb.enable()

def get_team(cookies):
    cookies = cookies.split("; ")
    tid = cookies[1][4:]
    return tid

def sort_dict(d):
    return sorted(d.items(), key=operator.itemgetter(1))

def rank_teams(team_data):
    team_data_copy = team_data.copy()
    ranks = {}
    rank = 1
    length = len(team_data_copy)
    for x in range(length):
        if len(team_data_copy) == 0:
            return
        highest_score = max(team_data_copy.values())
        for team in team_data_copy:
            if team_data_copy[team] == highest_score:
                ranks[team] = rank
                rank += 1
                del team_data_copy[team]
                break
    return ranks

def get_rank(ranked, team):
    for info in ranked:
        teamm, rank = info
        if teamm == team:
            return rank
    return False

def gen_scoreboard(team_data, ranked, team):
    print '<h2 class="center teal-text">Scoreboard</h2>'
    if len(team_data) == 0:
        print '<h5 class = "center">There are no teams!<h5>'
        return
    if team != "":
        print "<center>Team %s, with a rank of %d, has %d points" %(team, get_rank(ranked, team), team_data[team])
    print "<br>"
    print "<div class='container'>"
    print "<table class='responsive-table bordered hoverable centered'>"
    print "<thead>"
    print "<tr><th>Rank</th><th>Team</th><th>Score</th></tr>"
    print "</thead>"
    for team, rank in ranked:
        print "<tr class='clickable-row' data-href='profile.py?team=%s'><td>%s</td><td>%s</td><td>%d</td></tr>" %(team, rank, team, team_data[team])

def main():
    fin = open("accounts/scores.txt", "r")
    data = fin.readlines()
    teams = {}
    # Data is stored team,score
    for info in data:
        info = info.strip().split("||&&||")
        if info[0] == "":
            continue
        teams[info[0]] = int(info[-2])
    ranked = sort_dict(rank_teams(teams))
    gen_scoreboard(teams, ranked, team)

try:
    cookies = os.environ["HTTP_COOKIE"]
    team = get_team(cookies)
except:
    team = ""
html = open("templates/scoreboard.html").read()
print html
main()
