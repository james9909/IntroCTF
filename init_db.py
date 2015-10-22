import sqlite3
import teamdb

db_name = "introctf.db"

conn = sqlite3.connect(db_name)
c = conn.cursor()
c.execute("CREATE TABLE problems (name text, description text, hint text, points integer, solves integer);")
c.execute("CREATE TABLE teams (name text, password text, score integer, admin integer);")
teamdb.add_admin_team("admin", "stuycs")

conn.commit()
conn.close()
