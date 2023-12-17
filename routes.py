from . import app, login_manager
from flask import request, redirect, render_template, url_for, flash
from .models.database import session
from .models.group import Group
from .models.student import Student
from .models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user

@app.route("/")
@app.route("/main")
@app.route("/group_management")
def group_manager():
    all_groups = session.query(Group).all()
    all_groups = [x.group_name for x in all_groups]
    return render_template("group_management.html", group_names=all_groups)

@app.route("/group_management", methods=["POST"])
@login_required
def group_management_user():
    group_name = request.form["group_name"]
    group = Group(
        group_name=group_name
    )
    try:
        session.add(group)
        session.commit()
    except Exception as exc:
        return f"Виникла проблема: {exc}"
    finally:
        session.close()
    return redirect("/group_management")



@app.route("/student_management/<group_name>")
def group_list_as_user(group_name):
    group_id = session.query(Group).where(Group.group_name == group_name).first().id()
    group = session.query(Student).where(Student.groups == group_id).all()
    return render_template("student_management.html", group=group)


@app.route("/student_management/<group_name>", methods=["POST"])
@login_required
def group_list_as_user_login(group_name):
    group_id = session.query(Group).where(Group.group_name == group_name).first().id()
    surname = request.form["surname"]
    name = request.form["name"]
    age = request.form["age"]
    home_address = request.form["home_address"]

    student = Student(
        surname=surname,
        name=name,
        age=age,
        home_address=home_address,
        groups=group_id
    )
    try:
        session.add(student)
        session.commit()
    except Exception as exc:
        return f"Виникла проблема при збереженні: {exc}"
    finally:
        session.close()
    return redirect(f"student_management/{group_name}")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form.get("name")
        password = request.form.get("password")

        user = session.query(User).where(User.username == username).first()
        if user:
            flash("Користувач з таким імене вже є у базі даних")
            return redirect(url_for("signup"))
        else:
            new_user = User(
                username=username,
                password=generate_password_hash(password=password)
            )
            session.add(new_user)
            session.commit()
            session.close()
            return redirect("login")
    else:
        return render_template("signup.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("name")
        password = request.form.get("password")
        remember = True if request.form.get("remember") else False

        user = session.query(User).where(User.username == username).first()

        if not user and not check_password_hash(user.password, password):
            flash("Будь ласка, перевір свої деталі авторизпції та спробуй ще раз ")
            return redirect(url_for("login"))

        login_user(user, remember=remember)
        return redirect("main")
    else:
        return render_template("login.html")


@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(int(user_id))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("main")