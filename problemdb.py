import sqlite3
import utils
import teamdb

db_name = "introctf.db"

def get_problems():
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM problems ORDER BY points ASC")
        return c.fetchall()
    except sqlite3.DatabaseError, e:
        print e
    if conn:
        conn.close()

def add_problem(name, description, hint, category, points, flag):
    conn = sqlite3.connect(db_name)
    pid = utils.generate_string(16)
    while pid_exists(pid):
        pid = utils.generate_string(16)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("INSERT into problems VALUES (?, ?, ?, ?, ?, ?, ?, 0)", (pid, name, description, hint, category, points, flag,))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print e
    if conn:
        conn.close()

def remove_problem(pid):
    if not pid_exists(pid):
        return "0"
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "-1"
    c = conn.cursor()
    try:
        c.execute("DELETE from problems WHERE pid = ?", (pid,))
        conn.commit()
        return "1"
    except sqlite3.DatabaseError, e:
        print e
        return "-1"
    if conn:
        conn.close()

def pid_exists(pid):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT 1 FROM problems WHERE pid = ? LIMIT 1", (pid,))
        return True if c.fetchone() else False
    except sqlite3.DatabaseError, e:
        print e
    if conn:
        conn.close()

def get_problems_from_category(category):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM problems WHERE category = ? ORDER BY points ASC, last_solve DESC", (category,))
        return c.fetchall()
    except sqlite3.DatabaseError, e:
        print e
    if conn:
        conn.close()

def get_problem_data(pid):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM problems WHERE pid = ?", (pid,))
        return c.fetchone()
    except sqlite3.DatabaseError, e:
        print e
    if conn:
        conn.close()

def submit_flag(team, pid, flag):
    if teamdb.already_solved(pid, team):
        return "-1"
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM problems WHERE pid = ? AND flag = ?", (pid, flag,))
        if c.fetchone():
            c.execute("UPDATE problems SET solves = solves + 1 WHERE pid = ?", (pid,))
            solves = teamdb.get_solves(team)
            solves.append(pid)
            data = get_problem_data(pid)
            c.execute("UPDATE teams SET solves = ?, score = score + ?, last_solve = datetime('now') WHERE name = ?", (",".join(solves), data[5], team,))
            conn.commit()
            return "1"
        else:
            return "0"
    except sqlite3.DatabaseError, e:
        print e
    if conn:
        conn.close()
