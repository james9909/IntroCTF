import string
import random
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app as app, url_for, redirect, session
from functools import wraps

def hash_password(s):
    return generate_password_hash(s)

def check_password(hashed_password, try_password):
    return check_password_hash(hashed_password, try_password)

def generate_string(length):
    return "".join([random.choice(string.letters + string.digits) for x in range(length)])

def admins_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session or not session['admin']:
            session.clear()
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return decorated_function

def redirect_if_not_logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "tid" not in session or "logged_in" not in session or not session["logged_in"]:
            return redirect(url_for("index"))
        return f(*args, **kwargs)
    return decorated_function
