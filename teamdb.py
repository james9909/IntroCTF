import utils
import sqlite3

db_name = "introctf.db"

def add_team(name, password, conn=None):
    persist_conn = True

    if not conn:
        conn = sqlite3.connect(db_name)
        persist_conn = False
    if conn == None:
        return "Database Error"

    c = conn.cursor()
    try:
        c.execute("INSERT into teams VALUES (?, ?, 0, 0, '')", (name, utils.hash_password(password),))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print "Error %s: " % e
    finally:
        if conn and not persist_conn:
            conn.close()

def remove_team(name, conn=None):
    persist_conn = True

    if not conn:
        conn = sqlite3.connect(db_name)
        persist_conn = False
    if conn == None:
        return "Database Error"

    c = conn.cursor()
    try:
        c.execute("DELETE FROM teams WHERE name = ?", (name,))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print "Error %s: " % e
    finally:
        if conn and not persist_conn:
            conn.close()

def team_exists(name):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT 1 from teams where name = ? LIMIT 1", (name,))
        return True if c.fetchone() else False
    except sqlite3.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()

def get_team_password(name):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT password from teams where name = ? LIMIT 1", (name,))
        results = c.fetchone()
        return results[0] if results else ""
    except sqlite3.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()

def get_team_score(name):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT score from teams where name = ? LIMIT 1", (name,))
        return c.fetchone()
    except sqlite3.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()

def add_admin_team(name, password, conn=None):
    persist_conn = True

    if not conn:
        conn = sqlite3.connect(db_name)
        persist_conn = False
    if conn == None:
        return "Database Error"

    c = conn.cursor()
    try:
        c.execute("INSERT into teams VALUES (?, ?, 0, 1, '')", (name, utils.hash_password(password),))
        conn.commit()
    except sqlite3.DatabaseError, e:
        print "Error %s: " % e
    finally:
        if conn and not persist_conn:
            conn.close()

def is_admin(team_name):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT admin FROM teams WHERE name = ?", (team_name,))
        result = c.fetchone()
        return 1 in result
    except sqlite3.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()

def get_solves(team):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT solves FROM teams WHERE name = ?", (team,))
        return str(c.fetchone()).split(",")
    except sqlite3.DatabaseError, e:
        print e
    if conn:
        conn.close()

def already_solved(pid, team):
    solves = get_solves(team)
    if pid in solves:
        return True
    return False

if __name__ == '__main__':
    print is_admin("admin")
