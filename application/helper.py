from functools import wraps
from flask import session, request,jsonify, redirect,url_for
import loadEnv
import os
def check_auth(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        if 'auth_user' in session:
             return func(*args, **kwargs)
        return redirect(url_for("web.login"))
    return decorated
def env(key):
    return os.getenv(key)
