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
        c.execute("INSERT into teams VALUES(%s, %s, 0)", (name, utils.hash_password(password)))
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
        c.execute("DELETE FROM teams WHERE name = %s" % (name))
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
        c.execute("SELECT 1 from teams where name = %s LIMIT 1" % (name))
        return c.fetchone()
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
        c.execute("SELECT password from teams where name = %s LIMIT 1" % (name))
        results = c.fetchone()
        return results[0] if results else None
    except sqlite3.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()
