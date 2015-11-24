import problemdb
import teamdb
import utils
from utils import admins_only, redirect_if_not_logged_in
from api import api
from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.debug = True

app.secret_key="123"

@app.route('/')
def index():
    return render_template("index.html", logged_in=is_logged_in(), admin=is_admin())

@app.route("/scoreboard")
def scoreboard():
    teams = teamdb.get_teams()
    return render_template("scoreboard.html", logged_in=is_logged_in(), admin=is_admin(), teams=teams)

@app.route("/problems")
@redirect_if_not_logged_in
def problems():
    problems = problemdb.get_problems()
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
    flash("Logout successful")
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

if __name__ == '__main__':
    app.jinja_env.trim_blocks = True
    app.register_blueprint(api)
    app.run()
