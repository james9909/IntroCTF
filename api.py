import sqlite3
import utils
import teamdb
import problemdb
from flask import Flask, Blueprint, request, session
from flask import current_app as app
from utils import admins_only, redirect_if_not_logged_in

api = Blueprint("api", __name__)
db_name = "introctf.db"

@api.route("/api/register", methods=["POST"])
def register():
    team = request.form["team"]
    password = request.form["password"]
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
@admins_only
def add_problem():
    name = request.form["problem_name"]
    desc = request.form["problem_desc"]
    hint = request.form["problem_hint"]
    category = request.form["problem_category"]
    value = request.form["problem_value"]
    flag = request.form["problem_flag"]
    response = problemdb.add_problem(name, desc, hint, category, value, flag)
    return response

@api.route("/api/submit_flag", methods=["POST"])
@admins_only
def submit_flag():
    flag = request.form["flag"]
    pid = request.form["pid"]
    team = session["tid"]
    response = problemdb.submit_flag(team, pid, flag)
    return response

@api.route("/api/remove_problem", methods=["POST"])
@admins_only
def remove_problem():
    pid = request.form["pid"]
    response = problemdb.remove_problem(pid)
    return response

@api.route("/api/update_problem", methods=["POST"])
@admins_only
def update_problem():
    pid = request.form["pid"]
    name = request.form["name"]
    desc = request.form["description"]
    hint = request.form["hint"]
    category = request.form["category"]
    points = request.form["points"]
    flag = request.form["flag"]
    response = problemdb.update_problem(pid, name, desc, hint, category, points, flag)
    return response
