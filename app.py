import dbhelper
import teamdb
import utils
from functools import wraps
from flask import Flask, render_template, request, flash, session, redirect, url_for, g

app = Flask(__name__)
app.debug = True

app.secret_key="123"

logged_in = False

@app.route('/')
def index():
    global logged_in
    return render_template("index.html", logged_in=logged_in)

@app.route("/about")
def about():
    return render_template("about.html", logged_in=logged_in)

@app.route("/scoreboard")
def scoreboard():
    return render_template("scoreboard.html", logged_in=logged_in)

@app.route("/problems")
def problems():
    return render_template("problems.html", logged_in=logged_in)

@app.route("/login", methods=["GET", "POST"])
def login():
    global logged_in
    if request.method == "POST":
        login_keys = ['team_name', 'password']
        if  utils.is_valid_request(request.form, login_keys):
            team_name = request.form['team_name']
            password = request.form['password']
            response = dbhelper.authenticate("AUTH_LOGIN", team_name, password, session)
            if response[0]:
                logged_in = True
                session["team_name"] = team_name
                session["password"] = password
                session["logged_in"] = True
                if teamdb.is_admin(team_name, password):
                    session["is_admin"] = True

            flash(response[1])

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        create_keys = ['team_name', 'password', 'password2']
        if utils.is_valid_request(request.form, create_keys):
            name = request.form['team_name']
            password = request.form['password']
            response = dbhelper.authenticate("REGISTER_NEW_TEAM", name, password, _session=None)
            flash(response[1])
    return render_template("register.html")

@app.route("/logout", methods=["GET"])
def logout():
    global logged_in
    session.clear()
    logged_in = False
    flash("Logout successful")
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()
