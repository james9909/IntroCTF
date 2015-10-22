import sqlite3
import utils

db_name = "introctf.db"

def add_user(name, password, team, conn=None):
    persist_conn = True

    if not conn:
        conn = sqlite3.connect(db_name)
        persist_conn = False
    if conn == None:
        return "Database Error"

    c = conn.cursor()
    try:
        c.execute("INSERT INTO users VALUES(?, ?, ?, 0)", (name, utils.hash_password(password), team,))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print "Error %s: " % e
    finally:
        if conn and not persist_conn:
            conn.close()

def remove_user(name, conn=None):
    persist_conn = True

    if not conn:
        conn = sqlite3.connect(db_name)
        persist_conn = False
    if conn == None:
        return "Database Error"

    c = conn.cursor()
    try:
        c.execute("DELETE FROM users WHERE username = ?", (name,))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print "Error %s: " % e
    finally:
        if conn and not persist_conn:
            conn.close()

def user_exists(name):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT 1 FROM users where username = ? LIMIT 1", (name,))
        return c.fetchone()
    except sqlite3.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()

def get_user_password(name):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT password from users where username = ? LIMIT 1", (name,))
        results = c.fetchone()
        return results[0] if results else None
    except sqlite3.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()

def get_user_team(name):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT team_name from users where username = ? LIMIT 1", (name,))
        results = c.fetchone()
        return results[0] if results else None
    except sqlite3.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()

def add_admin(username, password, team, conn=None):
    persist_conn = True

    if not conn:
        conn = sqlite3.connect(db_name)
        persist_conn = False
    if conn == None:
        return "Database Error"

    c = conn.cursor()
    try:
        c.execute("INSERT INTO users VALUES(?, ?, ?, 1)", (username, utils.hash_password(password), team,))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print "Error %s: " % e
    finally:
        if conn and not persist_conn:
            conn.close()

def is_admin(username, password):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT username FROM users WHERE username = ? AND password = ? AND admin = 1" , (username, utils.hash_password(password),))
        return True if c.fetchone() else False
    except sqlite3.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()
