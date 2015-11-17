from flask import Flask, Blueprint, request, session
from flask import current_app as app
import sqlite3
import utils
import teamdb

api = Blueprint("api", __name__)
db_name = "introctf.db"

@api.route("/api/register", methods=["POST"])
def register():
    team = request.form["team"]
    password = request.form["password"]
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "-1"
    c = conn.cursor()
    response = utils.is_valid_password(password)
    if not response[0]:
        return "2"
    if teamdb.team_exists(team):
        return "0"
    else:
        teamdb.add_team(team, password)
        return "1"

@api.route("/api/login", methods=["POST"])
def login():
    print request.form
    team = request.form["team"]
    password = request.form["password"]
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "-1"
    c = conn.cursor()
    stored_team_password = teamdb.get_team_password(team)
    if utils.check_password(stored_team_password, password):
        session["tid"] = team
        session["logged_in"] = True
        if teamdb.is_admin(team):
            session["admin"] = True
        return "1"
    else:
        return "0"
