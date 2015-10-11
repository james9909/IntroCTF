import string
from werkzeug.security import generate_password_hash, check_password_hash

def is_valid_request(form, required_keys):
    for key in required_keys:
        if not form.has_key(key) or form[key] != "":
            continue
        else:
            return False
    return True

def is_valid_password(password):
    valid_chars = string.ascii_letters + string.digits + string.punctuation
    for char in password:
        if char not in valid_chars:
            return (False, "Invalid characters in password.")
    if 4 <= len(password) <= 50:
        return (True, "Successful")
    else:
        return (False, "Invalid password length")

def hash_password(s):
    return generate_password_hash(s)

def check_password(hashed_password, try_password):
    return check_password_hash(hashed_password, try_password)
