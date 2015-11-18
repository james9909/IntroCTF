import sqlite3
import utils

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

def add_problem(name, description, hint, category, points):
    conn = sqlite3.connect(db_name)
    pid = utils.generate_string(16)
    while pid_exists(pid):
        pid = utils.generate_string(16)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("INSERT into problems VALUES (?, ?, ?, ?, ?, ?, 0)", (pid, name, description, hint, category, points,))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print e
    if conn:
        conn.close()

def remove_problem(name):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("DELETE from problems WHERE name = ?", (name,))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print e
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
        c.execute("SELECT * FROM problems WHERE category = ? ORDER BY points ASC", (category,))
        return c.fetchall()
    except sqlite3.DatabaseError, e:
        print e
    if conn:
        conn.close()
