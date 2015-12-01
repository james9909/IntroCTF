import sqlite3

db_name = "introctf.db"

def wipe_database():
    conn = sqlite3.connect(db_name)
    if conn is None:
        print "Error connecting to the database"
    else:
        c = conn.cursor()
        try:
            c.execute("DROP TABLE teams;")
            c.execute("DROP TABLE problems;")
            conn.commit()
        except sqlite3.DatabaseError, e:
            print e
        finally:
            if conn:
                conn.close()

if __name__ == "__main__":
    wipe_database()
