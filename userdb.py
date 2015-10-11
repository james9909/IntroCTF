import psycopg2, psycopg2.extras
import dbhelper
import utils

def add_user(name, password, team, conn=None):
    persist_conn = True

    if not conn:
        conn = dbhelper.connect()
        persist_conn = False
    if conn == None:
        return "Database Error"

    c = conn.cursor()
    try:
	c.execute("INSERT INTO users VALUES('%s', '%s', '%s')" % (name, utils.hash_password(password), team))
	conn.commit()
    except psycopg2.DatabaseError, e:
        print "Error %s: " % e
    finally:
        if conn and not persist_conn:
            conn.close()

def remove_user(name, conn=None):
    persist_conn = True

    if not conn:
        conn = dbhelper.connect()
        persist_conn = False
    if conn == None:
        return "Database Error"

    c = conn.cursor()
    try:
        c.execute("DELETE FROM users WHERE name = %s" % (name))
        conn.commit()
    except psycopg2.DatabaseError, e:
        print "Error %s: " % e
    finally:
        if conn and not persist_conn:
            conn.close()

def user_exists(name):
    conn = dbhelper.connect()
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT 1 FROM users where name = '%s' LIMIT 1" % (name))
        return c.fetchone()
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()

def get_user_password(name):
    conn = dbhelper.connect()
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT password from users where name = '%s' LIMIT 1" % (name))
        results = c.fetchone()
        return results[0] if results else None
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()

def get_user_team(name):
    conn = dbhelper.connect()
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT team from users where name = '%s' LIMIT 1" % (name))
        results = c.fetchone()
        return results[0] if results else None
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()
