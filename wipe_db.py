import sqlite3

db_name = "introctf.db"

conn = sqlite3.connect(db_name)
if conn == None:
    return "Database Error"
c = conn.cursor()
try:
    c.execute("DROP TABLE teams;")
    c.execute("DROP TABLE problems;")
    conn.commit()
except:
    return
finally:
    if conn:
        conn.close()
