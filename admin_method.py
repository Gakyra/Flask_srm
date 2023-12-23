from functools import wraps
from flask_login import current_user
from flask import redirect


def admin_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated:
            if current_user.username == "admin":
                return function()
            return redirect("profile")
        return redirect("login")
    return wrapper


