import json
import utils

import logger
import problemdb
import teamdb

from decorators import api_wrapper
from flask import Blueprint, request, session, jsonify, make_response
from decorators import admins_only

api = Blueprint("api", __name__)

@api.route("/api/register", methods=["POST"])
@api_wrapper
def register():
    team = request.form["team"]
    password = request.form["password"]
    password2 = request.form["password2"]

    if password != password2:
        return {"message": "Passwords do not match"}
    if len(password) < 4:
        return {"message": "Passwords should be at least 4 characters long"}
    if teamdb.team_exists(team):
        return {"message": "Team already exists"}
    else:
        response = teamdb.add_team(team, password)
        if "Success" in response:
            logger.log("registrations", logger.INFO, "%s has registered" % team)

        return {"message": response}


@api.route("/api/login", methods=["POST"])
@api_wrapper
def login():
    team = request.form["team"]
    password = request.form["password"]
    stored_team_password = teamdb.get_team_password(team)
    if utils.check_password(stored_team_password, password):
        session["tid"] = team
        session["logged_in"] = True
        if teamdb.is_admin(team):
            session["admin"] = True
            logger.log("logins", logger.WARNING, "%s logged as admin" % team)
        else:
            logger.log("logins", logger.INFO, "%s logged in" % team)
        return {"success": 1, "message": "Success!"}
    else:
        return {"success": 0, "message": "Invalid credentials"}

@api.route("/api/add_problem", methods=["POST"])
@admins_only
@api_wrapper
def add_problem():
    name = request.form["problem_name"]
    desc = request.form["problem_desc"]
    hint = request.form["problem_hint"]
    category = request.form["problem_category"]
    value = request.form["problem_value"]
    flag = request.form["problem_flag"]
    response = problemdb.add_problem(name, desc, hint, category, value, flag)
    return {"message": response}

@api.route("/api/submit_flag", methods=["POST"])
@api_wrapper
def submit_flag():
    flag = request.form["flag"]
    pid = request.form["pid"]
    team = session["tid"]
    response = problemdb.submit_flag(team, pid, flag)
    return {"message": response}

@api.route("/api/remove_problem", methods=["POST"])
@admins_only
@api_wrapper
def remove_problem():
    pid = request.form["pid"]
    response = problemdb.remove_problem(pid)
    return {"message": response}

@api.route("/api/update_problem", methods=["POST"])
@admins_only
@api_wrapper
def update_problem():
    pid = request.form["pid"]
    name = request.form["name"]
    desc = request.form["description"]
    hint = request.form["hint"]
    category = request.form["category"]
    points = request.form["points"]
    flag = request.form["flag"]
    response = problemdb.update_problem(pid, name, desc, hint, category, points, flag)
    return {"message": response}

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
