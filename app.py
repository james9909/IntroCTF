import dbhelper
import problemdb
import teamdb
import utils
from api import api
from functools import wraps
from flask import Flask, render_template, request, flash, session, redirect, url_for, g

app = Flask(__name__)
app.debug = True

app.secret_key="123"

@app.route('/')
def index():
    return render_template("index.html", logged_in=is_logged_in(), admin=is_admin())

@app.route("/scoreboard")
def scoreboard():
    return render_template("scoreboard.html", logged_in=is_logged_in(), admin=is_admin())

@app.route("/problems")
def problems():
    problems = problemdb.get_problems()
    return render_template("problems.html", logged_in=is_logged_in(), admin=is_admin(), problems=problems)

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")

@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    flash("Logout successful")
    return redirect(url_for("index"))

@app.route("/admin", methods=["GET"])
def admin():
    problems = problemdb.get_problems()
    return render_template("admin_dashboard.html", problems=problems)

def is_logged_in():
    return "logged_in" in session and session["logged_in"]

def is_admin():
    return "admin" in session and session["admin"]

if __name__ == '__main__':
    app.register_blueprint(api)
    app.run()
