import utils
import sqlite3

db_name = "introctf.db"

def add_team(name, password):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "-1"
    c = conn.cursor()
    try:
        c.execute("INSERT into teams VALUES (?, ?, 0, 0, '', '')", (name, utils.hash_password(password),))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    finally:
        if conn:
            conn.close()

def remove_team(name):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "-1"
    c = conn.cursor()
    try:
        c.execute("DELETE FROM teams WHERE name = ?", (name,))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    finally:
        if conn:
            conn.close()

def team_exists(name):
    conn = sqlite3.connect(db_name)
    if conn == None:
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
    if conn == None:
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
    if conn == None:
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

def add_admin_team(name, password, conn=None):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "-1"
    c = conn.cursor()
    try:
        c.execute("INSERT into teams VALUES (?, ?, 0, 1, '', '')", (name, utils.hash_password(password),))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    finally:
        if conn:
            conn.close()

def is_admin(team_name):
    conn = sqlite3.connect(db_name)
    if conn == None:
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
    if conn == None:
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

def get_scoreboard_data():
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "-1"
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM teams WHERE name != 'admin' ORDER BY score DESC, last_solve ASC")
        return c.fetchall()
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    if conn:
        conn.close()

def get_teams():
    conn = sqlite3.connect(db_name)
    if conn == None:
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
