import sqlite3

db_name = "introctf.db"

conn = sqlite3.connect(db_name)
c = conn.cursor()
c.execute("CREATE TABLE users (username text, password text, team_name text, admin integer);")
c.execute("CREATE TABLE problems (name text, description text, hint text, points integer, solves integer);")
c.execute("CREATE TABLE teams (name text, password text, score integer);")

conn.commit()
conn.close()
