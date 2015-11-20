import string
import random
from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(s):
    return generate_password_hash(s)

def check_password(hashed_password, try_password):
    return check_password_hash(hashed_password, try_password)

def generate_string(length):
    return "".join([random.choice(string.letters + string.digits) for x in range(length)])
