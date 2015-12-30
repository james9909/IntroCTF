import datetime
import logging
import logging.handlers
import os
import random
import string

from werkzeug.security import generate_password_hash, check_password_hash

def initalize_logs():
    registration_logger = logging.getLogger("registrations")
    login_logger = logging.getLogger("logins")
    submission_logger = logging.getLogger("submissions")

    registration_logger.setLevel(logging.INFO)
    login_logger.setLevel(logging.INFO)
    submission_logger.setLevel(logging.INFO)

    base = os.path.dirname(__file__)
    log_path = os.path.join(base, "logs")

    if not os.path.exists(log_path):
        os.mkdir(log_path)

    logs = [os.path.join(log_path, "registrations.log"), os.path.join(log_path, "logins.log"), os.path.join(log_path, "submissions.log")]

    registration_log = logging.handlers.RotatingFileHandler(logs[0], maxBytes=10000)
    login_log = logging.handlers.RotatingFileHandler(logs[1], maxBytes=10000)
    submission_log = logging.handlers.RotatingFileHandler(logs[2], maxBytes=10000)

    registration_logger.addHandler(registration_log)
    login_logger.addHandler(login_log)
    submission_logger.addHandler(submission_log)

def log(log, level, message):
    log = logging.getLogger(log)
    message = "[%s] %s" % (datetime.datetime.now().strftime("%m/%d/%Y %X"), message)
    log.log(level, message)

def hash_password(s):
    return generate_password_hash(s)

def check_password(hashed_password, try_password):
    return check_password_hash(hashed_password, try_password)

def generate_string(length):
    return "".join([random.choice(string.letters + string.digits) for x in range(length)])

def unix_time_millis(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000.0

def get_time_since_epoch():
    return unix_time_millis(datetime.datetime.now())
