import sqlite3

import app
import problemdb
import utils

def add_team(name, password, date=None):
    conn = app.conn
    if conn is None:
        return "Could not connect to the database"
    c = conn.cursor()
    try:
        if date is None:
            date = str(utils.get_time_since_epoch())
        c.execute("INSERT into teams VALUES (?, ?, 0, 0, '', '', ?)", (name, utils.hash_password(password), "0,"+date))
        conn.commit()
        return "Success!"
    except sqlite3.DatabaseError, e:
        print e
        return "Could not connect to the database"

def remove_team(name):
    conn = app.conn
    if conn is None:
        return "Could not connect to the database"
    c = conn.cursor()
    try:
        c.execute("DELETE FROM teams WHERE name = ?", (name,))
        conn.commit()
        return "Success!"
    except sqlite3.DatabaseError, e:
        print e
        return "Could not connect to the database"

def team_exists(name):
    conn = app.conn
    if conn is None:
        return "Could not connect to the database"
    c = conn.cursor()
    try:
        c.execute("SELECT 1 from teams where name = ? LIMIT 1", (name,))
        return True if c.fetchone() else False
    except sqlite3.DatabaseError, e:
        print e
        return "Could not connect to the database"

def get_team_password(name):
    conn = app.conn
    if conn is None:
        return "Could not connect to the database"
    c = conn.cursor()
    try:
        c.execute("SELECT password from teams where name = ? LIMIT 1", (name,))
        results = c.fetchone()
        return results[0] if results else ""
    except sqlite3.DatabaseError, e:
        print e
        return "Could not connect to the database"

def get_team_score(name):
    conn = app.conn
    if conn is None:
        return "Could not connect to the database"
    c = conn.cursor()
    try:
        c.execute("SELECT score from teams where name = ? LIMIT 1", (name,))
        return c.fetchone()
    except sqlite3.DatabaseError, e:
        print e
        return "Could not connect to the database"

def add_admin_team(name, password, date=None):
    conn = app.conn
    if conn is None:
        return "Could not connect to the database"
    c = conn.cursor()
    try:
        if date is None:
            date = str(utils.get_time_since_epoch())
        c.execute("INSERT into teams VALUES (?, ?, 0, 1, '', '', ?)", (name, utils.hash_password(password), "0,"+date))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print e
        return "Could not connect to the database"

def is_admin(team_name):
    conn = app.conn
    if conn is None:
        return "Could not connect to the database"
    c = conn.cursor()
    try:
        c.execute("SELECT admin FROM teams WHERE name = ?", (team_name,))
        result = c.fetchone()
        return 1 in result
    except sqlite3.DatabaseError, e:
        print e
        return "Could not connect to the database"

def get_solves(team):
    conn = app.conn
    if conn is None:
        return "Could not connect to the database"
    c = conn.cursor()
    try:
        c.execute("SELECT solves FROM teams WHERE name = ?", (team,))
        return list(c.fetchone())[0].split(",")
    except sqlite3.DatabaseError, e:
        print e
        return "Could not connect to the database"

def already_solved(pid, team):
    solves = get_solves(team)
    if pid in solves:
        return True
    return False

def get_scoreboard_data(limit=None):
    conn = app.conn
    if conn is None:
        return "Could not connect to the database"
    c = conn.cursor()
    try:
        if limit is None:
            c.execute("SELECT * FROM teams WHERE name != 'admin' ORDER BY score DESC, last_solve ASC")
        else:
            c.execute("SELECT * FROM teams WHERE name != 'admin' ORDER BY score DESC, last_solve ASC LIMIT ?", (limit,))
        return c.fetchall()
    except sqlite3.DatabaseError, e:
        print e
        return "Could not connect to the database"

def get_teams():
    conn = app.conn
    if conn is None:
        return "Could not connect to the database"
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM teams")
        return c.fetchall()
    except sqlite3.DatabaseError, e:
        print e
        return "Could not connect to the database"

def get_progression(team):
    conn = app.conn
    if conn is None:
        return "Could not connect to the database"
    c = conn.cursor()
    try:
        c.execute("SELECT progression FROM teams WHERE name = ?", (team,))
        return c.fetchone()[0].split(",")
    except sqlite3.DatabaseError, e:
        print e
        return "Could not connect to the database"

def get_score(team):
    conn = app.conn
    if conn is None:
        return "Could not connect to the database"
    c = conn.cursor()
    try:
        c.execute("SELECT score FROM teams WHERE name = ?", (team,))
        return c.fetchone()[0]
    except sqlite3.DatabaseError, e:
        print e
        return "Could not connect to the database"

def update_score(team, new_score):
    conn = app.conn
    if conn is None:
        return "Could not connect to the database"
    c = conn.cursor()
    try:
        c.execute("UPDATE teams SET score = ? WHERE name = ?", (new_score, team))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print e
        return "Could not connect to the database"

def update_solves(team, new_solves):
    conn = app.conn
    if conn is None:
        return "Could not connect to the database"
    c = conn.cursor()
    try:
        c.execute("UPDATE teams SET solves = ? WHERE name = ?", (new_solves, team))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print e
        return "Could not connect to the database"

def recalculate_scores(pid=None, new_value=None):
    if pid is None or new_value is None:
        raw_data = get_teams()
        data = [[team[0], team[4].split(",")[1:]] for team in raw_data]
        for team,solves in data:
            new_score = 0
            for pid in solves:
                try:
                    new_score += int(problemdb.get_problem_data(pid)[5])
                except TypeError:
                    # Problem does not exist
                    pass
            update_score(team, new_score)
    elif pid and new_value:
        original_value = problemdb.get_problem_data(pid)[5]
        teams = problemdb.get_teams_who_solved(pid)
        for team in teams:
            team = team[0]
            score = get_score(team)
            new_score = score - original_value + int(new_value)
            update_score(team, new_score)

def recalculate_solves(pid=None):
    if pid is None:
        raw_data = get_teams()
        data = [[team[0], team[4].split(",")[1:]] for team in raw_data]
        for team,solves in data:
            new_solves = []
            for pid in solves:
                if problemdb.pid_exists(pid):
                    new_solves.append(pid)
            new_solves = ",".join(new_solves)
            update_solves(team, new_solves)
    else:
        teams = problemdb.get_teams_who_solved(pid)
        for team in teams:
            new_solves = []
            solved = get_solves(team)
            for problem in solved:
                if problemdb.pid_exists(problem):
                    new_solves.append(problem)
            new_solves = ",".join(new_solves)
            update_solves(team, new_solves)
