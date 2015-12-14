import sqlite3

import problemdb
import utils

db_name = "introctf.db"

def add_team(name, password, date=None):
    conn = sqlite3.connect(db_name)
    if conn is None:
        return "-1"
    c = conn.cursor()
    try:
        if date is None:
            date = str(utils.get_time_since_epoch())
        c.execute("INSERT into teams VALUES (?, ?, 0, 0, '', '', ?)", (name, utils.hash_password(password), "0,"+date))
        conn.commit()
        return "Success!"
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    finally:
        if conn:
            conn.close()

def remove_team(name):
    conn = sqlite3.connect(db_name)
    if conn is None:
        return "-1"
    c = conn.cursor()
    try:
        c.execute("DELETE FROM teams WHERE name = ?", (name,))
        conn.commit()
        return "Success!"
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    finally:
        if conn:
            conn.close()

def team_exists(name):
    conn = sqlite3.connect(db_name)
    if conn is None:
        return "-1"
    c = conn.cursor()
    try:
        c.execute("SELECT 1 from teams where name = ? LIMIT 1", (name,))
        return True if c.fetchone() else False
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    finally:
        if conn:
            conn.close()

def get_team_password(name):
    conn = sqlite3.connect(db_name)
    if conn is None:
        return "-1"
    c = conn.cursor()
    try:
        c.execute("SELECT password from teams where name = ? LIMIT 1", (name,))
        results = c.fetchone()
        return results[0] if results else ""
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    finally:
        if conn:
            conn.close()

def get_team_score(name):
    conn = sqlite3.connect(db_name)
    if conn is None:
        return "-1"
    c = conn.cursor()
    try:
        c.execute("SELECT score from teams where name = ? LIMIT 1", (name,))
        return c.fetchone()
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    finally:
        if conn:
            conn.close()

def add_admin_team(name, password, date=None):
    conn = sqlite3.connect(db_name)
    if conn is None:
        return "-1"
    c = conn.cursor()
    try:
        if date is None:
            date = str(utils.get_time_since_epoch())
        c.execute("INSERT into teams VALUES (?, ?, 0, 1, '', '', ?)", (name, utils.hash_password(password), "0,"+date))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    finally:
        if conn:
            conn.close()

def is_admin(team_name):
    conn = sqlite3.connect(db_name)
    if conn is None:
        return "-1"
    c = conn.cursor()
    try:
        c.execute("SELECT admin FROM teams WHERE name = ?", (team_name,))
        result = c.fetchone()
        return 1 in result
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    finally:
        if conn:
            conn.close()

def get_solves(team):
    conn = sqlite3.connect(db_name)
    if conn is None:
        return "-1"
    c = conn.cursor()
    try:
        c.execute("SELECT solves FROM teams WHERE name = ?", (team,))
        return list(c.fetchone())[0].split(",")
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    if conn:
        conn.close()

def already_solved(pid, team):
    solves = get_solves(team)
    if pid in solves:
        return True
    return False

def get_scoreboard_data(limit=None):
    conn = sqlite3.connect(db_name)
    if conn is None:
        return "-1"
    c = conn.cursor()
    try:
        if limit is None:
            c.execute("SELECT * FROM teams WHERE name != 'admin' ORDER BY score DESC, last_solve ASC")
        else:
            c.execute("SELECT * FROM teams WHERE name != 'admin' ORDER BY score DESC, last_solve ASC LIMIT ?", (limit,))
        return c.fetchall()
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    if conn:
        conn.close()

def get_teams():
    conn = sqlite3.connect(db_name)
    if conn is None:
        return "-1"
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM teams")
        return c.fetchall()
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    if conn:
        conn.close()

def get_progression(team):
    conn = sqlite3.connect(db_name)
    if conn is None:
        return "-1"
    c = conn.cursor()
    try:
        c.execute("SELECT progression FROM teams WHERE name = ?", (team,))
        return c.fetchone()[0].split(",")
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    if conn:
        conn.close()

def get_score(team):
    conn = sqlite3.connect(db_name)
    if conn is None:
        return "-1"
    c = conn.cursor()
    try:
        c.execute("SELECT score FROM teams WHERE name = ?", (team,))
        return c.fetchone()[0]
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    if conn:
        conn.close()

def update_score(team, new_score):
    conn = sqlite3.connect(db_name)
    if conn is None:
        return "-1"
    c = conn.cursor()
    try:
        c.execute("UPDATE teams SET score = ? WHERE name = ?", (new_score, team))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    if conn:
        conn.close()

def update_solves(team, new_solves):
    conn = sqlite3.connect(db_name)
    if conn is None:
        return "-1"
    c = conn.cursor()
    try:
        c.execute("UPDATE teams SET solves = ? WHERE name = ?", (new_solves, team))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    if conn:
        conn.close()

def recalculate_scores():
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

def recalculate_solves():
    raw_data = get_teams()
    data = [[team[0], team[4].split(",")[1:]] for team in raw_data]
    for team,solves in data:
        new_solves = []
        for pid in solves:
            if problemdb.pid_exists(pid):
                new_solves.append(pid)
        new_solves = ",".join(new_solves)
        update_solves(team, new_solves)
