from flask import url_for, redirect, session
from functools import wraps

def api_wrapper(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        web_result = {}
        response = 200
        try:
            web_result = f(*args, **kwds)
        except Exception as error:
            web_result = { "success": 0, "message": "Something went wrong! Please notify us about this immediately: %s" % error }
            import traceback
            print traceback.print_exc()
        return json.dumps(web_result), response, { "Content-Type": "application/json; charset=utf-8" }
    return wrapper

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
