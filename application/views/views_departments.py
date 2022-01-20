"""This file contains departments routes to web application"""

from flask import redirect, render_template, abort
from application import app
from application.forms.forms import AddDepartmentForm, EditDepartmentForm
from application.models.models import Department
from application.service.service_departments import add_department, delete_department, update_department


@app.route("/")
def home():
    return redirect("/departments")


@app.route("/departments", methods=["GET"])
def departments():
    form = AddDepartmentForm()
    deps = Department.query.all()
    return render_template("departments.html", departments=deps, form=form)


@app.route("/departments", methods=["POST"])
def departments_post():
    form = AddDepartmentForm()
    if form.validate_on_submit():
        add_department(form.name.data)
    return redirect("/departments")


@app.route("/department/<id_>", methods=["GET"])
def department(id_):
    form = EditDepartmentForm()
    dep = Department.query.get(id_)
    if not dep:
        abort(404)
    return render_template("department.html", department=dep, form=form)


@app.route("/department/<id_>/delete")
def department_delete(id_):
    dep = Department.query.get(id_)
    if not dep:
        abort(404)
    delete_department(id_)
    return redirect("/departments")


@app.route("/department/<id_>", methods=["POST"])
def department_edit(id_):
    form = EditDepartmentForm()
    if form.validate_on_submit():
        update_department(id_, form.name.data)
    return redirect(f"/department/{id_}")

