import json
import sqlite3
import utils
import teamdb
import problemdb
from flask import Flask, Blueprint, request, session, jsonify, make_response
from flask import current_app as app
from utils import admins_only, redirect_if_not_logged_in

api = Blueprint("api", __name__)
db_name = "introctf.db"

@api.route("/api/register", methods=["POST"])
def register():
    team = request.form["team"]
    password = request.form["password"]
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

@api.route("/api/top/<count>", methods=["GET", "POST"])
def top(count):
    data = {}
    teams = teamdb.get_scoreboard_data(5)
    scoreboard = []
    for team in teams:
        jason = {}
        jason["name"] = team[0]
        jason["score"] = team[2]
        jason["last_solve"] = team[5]
        jason["progression"] = team[6] + ",%s,%s" % (team[2], utils.get_time_since_epoch()) # Add current time score to make graph look nicer
        scoreboard.append(jason)
    data["scoreboard"] = scoreboard
    return jsonify(data=data)

@api.route("/api/export_data", methods=["GET", "POST"])
@admins_only
def export_data():
    data = {}
    form = request.form
    if "problems" in form:
        problem_list = []
        problems = problemdb.get_problems()
        for problem in problems:
            jason = {}
            jason["pid"] = problem[0]
            jason["name"] = problem[1]
            jason["description"] = problem[2]
            jason["hint"] = problem[3]
            jason["category"] = problem[4]
            jason["points"] = problem[5]
            jason["flag"] = problem[6]
            problem_list.append(jason)
        data["problems"] = problem_list
    if "scoreboard" in form:
        scoreboard = []
        teams = teamdb.get_scoreboard_data()
        for team in teams:
            jason = {}
            jason["name"] = team[0]
            jason["score"] = team[2]
            jason["solves"] = [problemdb.get_name_from_pid(pid) for pid in team[4].split(",")[1:]]
            jason["last_solve"] = team[5]
            jason["progression"] = team[6] + ",%s,%s" % (team[2], utils.get_time_since_epoch()) # Add current time score to make graph look nicer
            scoreboard.append(jason)
        data["scoreboard"] = scoreboard
    if "teams" in form:
        team_list = []
        teams = teamdb.get_teams()
        for team in teams:
            jason = {}
            jason["name"] = team[0]
            jason["password"] = team[1]
            jason["score"] = team[2]
            jason["admin"] = team[3]
            jason["solves"] = [problemdb.get_name_from_pid(pid) for pid in team[4].split(",")[1:]]
            jason["last_solve"] = team[5]
            jason["progression"] = team[6]
            team_list.append(jason)
        data["teams"] = team_list
    data = json.dumps(data, indent=4)
    if "download" in form:
        response = make_response(data)
        response.headers["Content-Disposition"] = "attachment; filename=data.json"
        return response
    return jsonify(data=json.loads(data))
