import psycopg2, psycopg2.extras
import utils
import dbhelper

def add_team(name, password, conn=None):
    persist_conn = True

    if not conn:
        conn = dbhelper.connect()
        persist_conn = False
    if conn == None:
        return "Database Error"

    c = conn.cursor()
    try:
        c.execute('''INSERT INTO teams VALUES(%s, %s, 0, '{}', '{}')''', (name, utils.hash_password(password)))
        conn.commit()
    except psycopg2.DatabaseError, e:
        print "Error %s: " % e
    finally:
        if conn and not persist_conn:
            conn.close()

def remove_team(name, conn=None):
    persist_conn = True

    if not conn:
        conn = dbhelper.connect()
        persist_conn = False
    if conn == None:
        return "Database Error"

    c = conn.cursor()
    try:
        c.execute("DELETE FROM teams WHERE name = %s" % (name))
        conn.commit()
    except psycopg2.DatabaseError, e:
        print "Error %s: " % e
    finally:
        if conn and not persist_conn:
            conn.close()

def team_exists(name):
    conn = dbhelper.connect()
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT 1 from teams where name = '%s' LIMIT 1" % (name))
        return c.fetchone()
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()

def get_team_password(name):
    conn = dbhelper.connect()
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("SELECT password from teams where name = '%s' LIMIT 1" % (name))
        results = c.fetchone()
        return results[0] if results else None
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()

def get_team_members(team_name):
    conn = dbhelper.connect()
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute('''SELECT members from teams where name = '%s' LIMIT 1''' % (team_name))
        result = c.fetchone()
        return result[0] if result else None
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()

def add_user_to_team(team_name, user):
    conn = dbhelper.connect()
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        members = get_team_members(team_name)
        old_members = list(members)
        members.append(user)
        c.execute("UPDATE teams SET members = %s WHERE members = %s", (members, old_members))
        conn.commit()
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()
