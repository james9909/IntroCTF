#!/usr/bin/python

print "Content-Type: text/html\n"
print ""

import cgi, cgitb, collections

cgitb.enable()

pids = ["intro", "caesar", "base", "absent", "brutus", "bb", "stego", "dot", "corrupt", "inverted", "rawr", "messy", "inspect", "cookie", "hidden", "get", "spoof", "sets", "indif", "donttrip","fast", "triangle", "overflow", "eval", "copy", "easy-rev", "rand-eval", "election", "sets"]
names = ["Introduction", "Caesar", "The Best Base", "Absent", "Brutus", "b1naryb0ts", "Intro Stego", "Dot", "Corruption", "Inverted", "RAAWWWRRRR", "Messy Code", "Inspector", "Cookie Jar", "HIdden", "GET", "Easy Spoof", "Sets", "Indifferent", "Don't Trip", "Random Fast Math", "Triangles", "Intro Overflow", "Intro Eval", "Copy Cat", "Easy Reverse", "Random Eval", "Elections"]

problems = collections.OrderedDict()

for pid, name in zip(pids, names):
    problems[pid] = name
    
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

def genProfile(tid):
    print "<br><br>"
    if not existsTeam(tid):
        print "Team does not exist!"
        return
    print "<h3 class='center teal-text'>%s</h3>" %(tid)
    print "<div class='container'>"
    print "<table class='responsive-table bordered hoverable'>"
    print "<thead>"
    print "<tr><th>Problem</th><th>Point Value</th><th>Status</th></tr>"
    print "</thead>"
    for problem in problems:
        status = isSolved(tid, problem)
        value = getProblemPointValue(problem)
        if status:
            print "<tr class='green lighten-5'><td>%s</td><td>%s</td><td>Solved</td></tr>" %(problems[problem], value)
        else:
            print "<tr class='red lighten-5'><td>%s</td><td>%s</td><td>Unsolved</td></tr>" %(problems[problem], value)

def getTeamMembers(tid):
    fin = open("accounts/teams.txt", "r")
    teams = fin.readlines()
    for team in teams:
        team = team.strip().split("||&&||")
        if team[0] == tid:
            return team[2:]

def main():
    inputs = cgi.FieldStorage()
    tid = inputs.getvalue("team")
    members = getTeamMembers(tid)
    if not existsTeam(tid):
        print "Team does not exist!"
        return
    print "<h3 class='center teal-text'>Team %s</h3>" %(tid)
    print "<ol>"
    for member in members:
        print "<br>"
        print "<li style='font-weight:800;'>%s</li>" %(member)
    print "</ol>"
    print "<br>"
    print "<center>Up to %d more member(s) can join this team</center>" %(4 - len(members))
    print "</div>"
    """print '<div class="row">'
    print '<div class="card medium col s6">'
    print '<h5 class="center teal-text">Rank</h5>'
    print "test"
    print "</div>"
    print "</div>"
    print "</div>"""
    print "</div>"
    genProfile(tid)

html = open("templates/profile.html", "r").read()
print html
main()
