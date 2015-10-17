import utils
import userdb
import teamdb
import sqlite3

db_name = "introctf.db"

def wipe_tables():
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "Database Error"
    c = conn.cursor()
    try:
        c.execute("DROP TABLE users;")
        c.execute("DROP TABLE teams;")
        c.execute("DROP TABLE problems;")
        conn.commit()
    except:
        return
    finally:
        if conn:
            conn.close()

def authenticate(type, name, password, team_name, team_pass, _session):
    conn = sqlite3.connect(db_name)
    if conn == None:
        return (False, "Database Error")
    c = conn.cursor()
    if type == "REGISTER_NEW_TEAM":
        response = utils.is_valid_password(password)
        if not response[0]:
            return False, response[1]
        response = utils.is_valid_password(team_pass)
        if not response[0]:
            return False, response[1]
        if not userdb.user_exists(name):
            if not teamdb.team_exists(team_name):
                userdb.add_user(name, password, team_name)
                teamdb.add_team(team_name, team_pass, 0)
                return True, "Successfully created new team"
            else:
                return False, "A team with that name already exists!"
        else:
            return False, "A user with that name already exists!"
    elif type == "REGISTER_JOIN_TEAM":
        response = utils.is_valid_password(password)
        if not response[0]:
            return False, response[1]
        stored_team_password = teamdb.get_team_password(team_name)
        if userdb.user_exists(name):
            return False, "A user with that name already exists!"
        if utils.check_password(stored_team_password, team_pass):
            userdb.add_user(name, password, team_name)
            return True, "Successfully joined team"
        else:
            return False, "Invalid team credentials"
    elif type == "AUTH_LOGIN":
        stored_user_password = userdb.get_user_password(name)
        if utils.check_password(stored_user_password, password):
            tid = userdb.get_user_password(name)
            _session['tid'] = tid
            return True, "Login successful"
        else:
            return False, "Invalid credentials"
    else:
        return "Bad request"

if __name__ == '__main__':
    wipe_tables()
