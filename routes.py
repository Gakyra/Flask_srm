from . import app
from flask import request, redirect, render_template
from .models.database import session
from .models.group import Group
from .models.student import Student


@app.route("/")
@app.route("/group_management", methods=["POST", "GET"])
def group_manager():
    all_groups = session.query(Group).all()
    all_groups = [x.group_name for x in all_groups]

    if request.method == "POST":
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
    return render_template("group_management.html", group_names=all_groups)


@app.route("/student_management/<group_name>", methods=["POST", "GET"])
def group_list(group_name):
    group_id = session.query(Group).where(Group.group_name == group_name).first().id()

    group = session.query(Student).where(Student.groups == group_id).all()
    if request.method == "POST":
        surname = request.form["surname"]
        name = request.form["name"]
        age = request.form["age"]
        home_address = request.form["home_address"]

        student = Student(
            surname=surname,
            name=name,
            age=age,
            home_address=home_address
        )
        try:
            session.add(student)
            session.commit()
        except Exception as exc:
            return f"Виникла проблема при збереженні: {exc}"
        finally:
            session.close()
        return redirect(f"student_management/{group_name}")
    return render_template("student_management.html", group=group)

