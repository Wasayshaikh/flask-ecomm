from functools import wraps
from flask import session, request,jsonify, redirect,url_for
def check_auth(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        if 'auth_user' in session:
             return func(*args, **kwargs)
        return redirect(url_for("web.login"))
    return decorated
