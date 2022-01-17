"""This file contains routes to web application"""

from datetime import date
from application import app
from flask import render_template, redirect, request, abort
from application.models.models import Department, Employee
from application.forms.forms import AddDepartmentForm, AddEmployeeForm
from application.service.service_departments import add_department, update_department, delete_department
from application.service.service_employees import add_employee, update_employee, delete_employee


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


@app.route("/employees", methods=["GET"])
def employees():
    form = AddEmployeeForm()
    emps = Employee.query.all()
    return render_template("employees.html", employees=emps, form=form)


@app.route("/employees", methods=["POST"])
def employees_post():
    form = AddEmployeeForm()
    if form.validate_on_submit():
        formatted_date = date(int(form.birth_date.data[:4]), int(form.birth_date.data[5:7]),
                              int(form.birth_date.data[8:]))
        add_employee(form.name.data, formatted_date, form.department.data, form.salary.data)
    return redirect("/employees")


@app.route("/employee/<id_>")
def employee(id_):
    emp = Employee.query.get(id_)
    if not emp:
        abort(404)
    return render_template("employee.html", employee=emp)


@app.route("/department/<id_>")
def department(id_):
    dep = Department.query.get(id_)
    if not dep:
        abort(404)
    return render_template("department.html", department=dep)