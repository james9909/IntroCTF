from flask import Flask, Blueprint, request, session
from flask import current_app as app
import sqlite3
import utils
import teamdb
import problemdb

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

@api.route("/api/add_problem", methods=["POST"])
def add_problem():
    name = request.form["problem_name"]
    desc = request.form["problem_desc"]
    hint = request.form["problem_hint"]
    category = request.form["problem_category"]
    value = request.form["problem_value"]
    conn = sqlite3.connect(db_name)
    if conn == None:
        return "-1"
    c = conn.cursor()
    if problemdb.problem_exists(name):
        return "0"
    else:
        problemdb.add_problem(name, desc, hint, category, value)
        return "1"
    if conn:
        conn.close()
