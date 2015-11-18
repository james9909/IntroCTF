import sqlite3
import teamdb

db_name = "introctf.db"

conn = sqlite3.connect(db_name)
c = conn.cursor()
c.execute("CREATE TABLE problems (pid text PRIMARY KEY, name text, description text, hint text, category text, points integer, flag text, solves integer);")
c.execute("CREATE TABLE teams (name text, password text, score integer, admin integer, solves text);")
teamdb.add_admin_team("admin", "stuycs")

conn.commit()
conn.close()
