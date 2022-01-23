"""This file contains employees routes to web application"""

from datetime import date
from flask import render_template, redirect, abort
from application import app
from application.models.models import Employee
from application.forms.forms import AddEmployeeForm, EditEmployeeForm
from application.service.service_employees import add_employee, update_employee, delete_employee


@app.route("/employees", methods=["GET"])
def employees():
    """Route to page with employees list"""
    form = AddEmployeeForm()
    emps = Employee.query.all()
    return render_template("employees.html", employees=emps, form=form)


@app.route("/employees", methods=["POST"])
def employees_post():
    """Route to adding new employee"""
    form = AddEmployeeForm()
    if form.validate_on_submit():
        formatted_date = date(int(form.birth_date.data[:4]), int(form.birth_date.data[5:7]),
                              int(form.birth_date.data[8:]))
        add_employee(form.name.data, formatted_date, form.department.data, form.salary.data)
    return redirect("/employees")


@app.route("/employee/<id_>")
def employee(id_):
    """Route to page of employee with given id"""
    emp = Employee.query.get(id_)
    form = EditEmployeeForm()
    if not emp:
        abort(404)
    return render_template("employee.html", employee=emp, form=form)


@app.route("/employee/<id_>/delete")
def employee_delete(id_):
    """Route to deleting employee"""
    emp = Employee.query.get(id_)
    if not emp:
        abort(404)
    delete_employee(id_)
    return redirect("/employees")


@app.route("/employee/<id_>", methods=["POST"])
def employee_edit(id_):
    """Route to updating employee's info"""
    form = EditEmployeeForm()
    if form.validate_on_submit():
        formatted_date = date(int(form.birth_date.data[:4]), int(form.birth_date.data[5:7]),
                              int(form.birth_date.data[8:]))
        update_employee(id_, form.name.data, formatted_date, form.department.data, form.salary.data)
    return redirect(f"/employee/{id_}")
