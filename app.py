import logging
import sqlite3

import logger
import problemdb
import teamdb

from api import api
from flask import Flask, jsonify, make_response, render_template, session, redirect, url_for
from flask_limiter import Limiter
from decorators import admins_only, redirect_if_not_logged_in

app = Flask(__name__)
limiter = Limiter(app)

@app.errorhandler(429)
def error_handler(optional_argument=""):
    logger.log("spam", logger.CRITICAL, "%s is using the api too quickly!", session["tid"])
    return make_response(jsonify(message="Slow down!"), 200)

app.debug = True
app.secret_key = open(".secret_key", "r").read()
app.jinja_env.trim_blocks = True
limiter.limit("10/minute", error_message=error_handler, exempt_when=lambda: is_admin())(api)
app.register_blueprint(api)

conn = sqlite3.connect("introctf.db", check_same_thread=False)
conn.text_factory = str

@app.route('/')
def index():
    return render_template("index.html", logged_in=is_logged_in(), admin=is_admin())

@app.route("/scoreboard")
def scoreboard():
    scoreboard = teamdb.get_scoreboard_data()
    return render_template("scoreboard.html", logged_in=is_logged_in(), admin=is_admin(), scoreboard=scoreboard)

@app.route("/problems")
@redirect_if_not_logged_in
def problems():
    problems = problemdb.get_problems()
    if len(problems) == 0:
        return render_template("problems.html", logged_in=is_logged_in(), admin=is_admin())
    team = session["tid"]
    solved = teamdb.get_solves(team)
    return render_template("problems.html", logged_in=is_logged_in(), admin=is_admin(), problems=problems, solved=solved)

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html", logged_in=is_logged_in(), admin=is_admin())

@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")

@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/admin", methods=["GET"])
@admins_only
def admin():
    problems = problemdb.get_problems()
    return render_template("admin_dashboard.html", problems=problems, logged_in=is_logged_in(), admin=is_admin())

def is_logged_in():
    return "logged_in" in session and session["logged_in"]

def is_admin():
    return "admin" in session and session["admin"]

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    logger.initalize_logs()
    app.run(host="0.0.0.0", port=5000)
