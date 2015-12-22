import sqlite3

import app
import teamdb
import utils

def get_problems():
    conn = app.conn
    if conn == None:
        return
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM problems ORDER BY points ASC")
        return c.fetchall()
    except sqlite3.DatabaseError, e:
        print e
        return

def add_problem(name, description, hint, category, points, flag):
    if name_exists(name):
        return "Problem name already taken"
    conn = app.conn
    pid = utils.generate_string(16)
    while pid_exists(pid):
        pid = utils.generate_string(16)
    if conn == None:
        return "Could not connect to database"
    c = conn.cursor()
    try:
        c.execute("INSERT into problems VALUES (?, ?, ?, ?, ?, ?, ?, 0)", (pid, name, description, hint, category, points, flag,))
        conn.commit()
        return "Successfully added problem"
    except sqlite3.DatabaseError, e:
        return "Database error. Please contact an administrator as soon as possible: %s" % e

def remove_problem(pid):
    if not pid_exists(pid):
        return "Problem does not exist"
    conn = app.conn
    if conn == None:
        return "Could not connect to database"
    c = conn.cursor()
    try:
        c.execute("DELETE from problems WHERE pid = ?", (pid,))
        conn.commit()
        teamdb.recalculate_scores()
        teamdb.recalculate_solves()
        return "Problem removed"
    except sqlite3.DatabaseError, e:
        return "Database error. Please contact an administrator as soon as possible: %s" % e

def pid_exists(pid):
    conn = app.conn
    if conn == None:
        return
    c = conn.cursor()
    try:
        c.execute("SELECT 1 FROM problems WHERE pid = ? LIMIT 1", (pid,))
        return True if c.fetchone() else False
    except sqlite3.DatabaseError, e:
        print e
        return

def name_exists(name):
    conn = app.conn
    if conn == None:
        return
    c = conn.cursor()
    try:
        c.execute("SELECT 1 FROM problems WHERE name = ? LIMIT 1", (name,))
        return True if c.fetchone() else False
    except sqlite3.DatabaseError, e:
        print e
        return

def get_problems_from_category(category):
    conn = app.conn
    if conn == None:
        return
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM problems WHERE category = ? ORDER BY points ASC, last_solve DESC", (category,))
        return c.fetchall()
    except sqlite3.DatabaseError, e:
        print e
        return

def get_problem_data(pid):
    conn = app.conn
    if conn == None:
        return
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM problems WHERE pid = ?", (pid,))
        return c.fetchone()
    except sqlite3.DatabaseError, e:
        print e
        return

def submit_flag(team, pid, flag, date=None):
    if teamdb.already_solved(pid, team):
        return "You already solved this problem!"
    conn = app.conn
    if conn == None:
        return "Could not connect to database"
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM problems WHERE pid = ? AND flag = ?", (pid, flag,))
        if c.fetchone():
            c.execute("UPDATE problems SET solves = solves + 1 WHERE pid = ?", (pid,))
            solves = teamdb.get_solves(team)
            solves.append(pid)
            progression = teamdb.get_progression(team)
            data = get_problem_data(pid)
            if date is None:
                date = str(utils.get_time_since_epoch())
            progression.append(str(int(teamdb.get_score(team))+int(data[5]))+","+date)
            c.execute("UPDATE teams SET solves = ?, score = score + ?, last_solve = ?, progression = ? WHERE name = ?", (",".join(solves), data[5], date, ",".join(progression), team,))
            conn.commit()
            utils.log("submissions", 20, "%s has submitted %s to %s [CORRECT]" % (team, flag, get_name_from_pid(pid)))
            return "Correct!"
        else:
            utils.log("submissions", 20, "%s has submitted %s to %s [INCORRECT]" % (team, flag, get_name_from_pid(pid)))
            return "Incorrect"
    except sqlite3.DatabaseError, e:
        print e
        return "Database error. Please contact an administrator as soon as possible: %s" % e

def update_problem(pid, name, desc, hint, category, points, flag):
    conn = app.conn
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("UPDATE problems SET name = ?, description = ?, hint = ?, category = ?, points = ?, flag = ? WHERE pid = ?", (name, desc, hint, category, points, flag, pid,))
        conn.commit()
        teamdb.recalculate_scores()
        return "Problem updated!"
    except sqlite3.DatabaseError, e:
        print e
        return "Database error. Please contact an administrator as soon as possible: %s" % e

def get_name_from_pid(pid):
    conn = app.conn
    if conn == None:
        return
    c = conn.cursor()
    try:
        c.execute("SELECT name FROM problems WHERE pid = ?", (pid,))
        return c.fetchone()[0]
    except sqlite3.DatabaseError, e:
        print e
        return
