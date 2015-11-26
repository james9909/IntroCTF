import json
import os
import sqlite3
import problemdb
import teamdb

db_name = "introctf.db"

def generate_secret_key():
    key = os.urandom(128)
    open(".secret_key", "w").write(key)

def init_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("CREATE TABLE problems (pid text PRIMARY KEY, name text, description text, hint text, category text, points integer, flag text, solves integer);")
    c.execute("CREATE TABLE teams (name text, password text, score integer, admin integer, solves text, last_solve text);")
    response = str(raw_input("An admin team does not currently exist. Would you like to make one? [y/n] "))
    if response.lower() == "y":
        name = str(raw_input("Please input a name: "))
        password = str(raw_input("Please input a password: "))
    teamdb.add_admin_team(name, password)

    conn.commit()
    conn.close()

if not os.path.isfile(".secret_key"):
    print "Generating secret key..."
    generate_secret_key()
    print "Done!"

if not os.path.isfile(db_name):
    print "Initializing the database..."
    init_db()
    print "Done!"
