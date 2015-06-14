#!/usr/bin/python

print "Content-Type: text/html\n"
print ""

import cgi

problems = {"intro": "Introduction", "caesar": "Caesar", "base": "The Best Base", "absent": "Absent", "brutus": "Brutus", "bb": "b1naryb0ts", "stego": "Intro Stego", "dot": "Dot", "corrupt": "Corruption", "inverted": "Inverted", "rawr": "RAAWWWRRRR", "messy": "Messy Code", "inspect": "Inspector", "cookie": "Cookie Jar", "hidden": "HIdden", "get": "GET", "spoof": "Easy Spoof", "donttrip": "Don't Trip", "indif": "Indifferent", "fast": "Random Fast Math", "triangle": "Triangles", "overflow": "Intro Overflow", "eval": "Intro Eval", "copy": "Copy Cat", "easy-rev": "Easy Reverse", "rand-eval": "Random Eval", "election": "Elections", "sets": "Sets"}

def getProblemPointValue(pid):
    fin = open("problemPoints.txt", "r")
    problems = fin.readlines()
    for problem in problems:
        problem = problem.strip().split(",")
        if problem[0] == pid:
            return problem[1]

def getTeamSolved(tid):
    fin = open("accounts/solved.txt", "r")
    teams = fin.readlines()
    for team in teams:
        team = team.strip().split("||&&||")
        if team[0] == tid:
            return team[1:]

def isSolved(tid, pid):
    solved = getTeamSolved(tid)
    return pid in solved

def existsTeam(tid):
    fin = open("accounts/teams.txt", "r'")
    teams = fin.readlines()
    for team in teams:
        team = team.split("||&&||")
        if team[0] == tid:
            return True
    return False

def genTable(tid):
    if not existsTeam(tid):
        print "Team does not exist!"
        return
    print "<h3 class='center teal-text'>%s</h3>" %(tid)
    print "<br>"
    print "<div class='container'>"
    print "<table class='responsive-table bordered hoverable centered'>"
    print "<thead>"
    print "<tr><th>Problem</th><th>Point Value</th><th>Status</th></tr>"
    print "</thead>"
    solved = getTeamSolved(tid)
    for problem in solved:
        status = isSolved(tid, problem)
        value = getProblemPointValue(problem)
        if status:
            print "<tr class='green lighten-4'><td>%s</td><td>%s</td><td>Solved</td></tr>" %(problem, value)
        else:
            print "<tr class='red lighten-4'><td>%s</td><td>%s</td><td>Unsolved</td></tr>" %(problem, value)

def main():
    inputs = cgi.FieldStorage()
    tid = inputs.getvalue("team")
    gen_scoreboard(tid)

main()
