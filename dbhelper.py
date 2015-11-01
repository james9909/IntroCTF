import utils
import teamdb
import sqlite3

db_name = "introctf.db"

def wipe_tables():
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

def authenticate(type, team_name, password, _session):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return (False, "Database Error")
    c = conn.cursor()
    if type == "REGISTER_NEW_TEAM":
        response = utils.is_valid_password(password)
        if not response[0]:
            return False, response[1]
        if not teamdb.team_exists(team_name):
            teamdb.add_team(team_name, password)
            return True, "Successfully created new team"
        else:
            return False, "A team with that name already exists!"
    elif type == "AUTH_LOGIN":
        stored_team_password = teamdb.get_team_password(team_name)
        if utils.check_password(stored_team_password, password):
            _session['tid'] = team_name
            return True, "Login successful"
        else:
            return False, "Invalid credentials"
    else:
        return "Bad request"

if __name__ == '__main__':
    wipe_tables()
