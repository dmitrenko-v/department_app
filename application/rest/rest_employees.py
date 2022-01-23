"""This file contains employees routes to web service
Every route response with JSON"""

from datetime import date
from flask import request, jsonify
from application import app
from application.models.models import Employee
from application.service.service_employees import add_employee, delete_employee, update_employee


@app.route("/api/employees", methods=["GET"])
def get_employees():
    """This is API to GET all employees"""
    emps = Employee.query.all()
    return jsonify([{"name": emp.name, "birth_date": emp.birth_date, "department": emp.department,
                     "salary": emp.salary} for emp in emps])


@app.route("/api/employee/<id_>", methods=["GET"])
def get_employee(id_):
    """This is API to get employee with given id"""
    emp = Employee.query.get(id_)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify({"name": emp.name, "birth_date": emp.birth_date,
                    "department": emp.department, "salary": emp.salary})


@app.route("/api/employee/<id_>", methods=["DELETE"])
def delete_employee_api(id_):
    """This is API to delete existing employee"""
    if delete_employee(id_) == -1:
        return jsonify({"error": "Employee not found"}), 404
    return "", 201


@app.route("/api/employees", methods=["POST"])
def add_employee_api():
    """This is API to add new employee"""
    name = request.json.get("name", "")
    birth_date = request.json.get("birth_date", "")
    department = request.json.get("department", "")
    salary = request.json.get("salary", "")
    if not name or not birth_date or not department or not salary:
        return jsonify({"error": "Incorrect request"})
    formatted_date = date(int(birth_date[:4]), int(birth_date[5:7]), int(birth_date[8:]))
    add_employee(name, formatted_date, department, salary)
    return jsonify({"name": name, "birth_date": formatted_date, "department": department,
                    "salary": salary}), 201


@app.route("/api/employee/<id_>", methods=["PUT"])
def update_employee_api(id_):
    name = request.json.get("name", "")
    birth_date = request.json.get("birth_date", "")
    department = request.json.get("department", "")
    salary = request.json.get("salary", "")
    if not name or not birth_date or not department or not salary:
        return jsonify({"error": "Incorrect request"})
    formatted_date = date(int(birth_date[:4]), int(birth_date[5:7]), int(birth_date[8:]))
    if update_employee(id_, name, formatted_date, department, salary) == -1:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify({"name": name, "birth_date": formatted_date, "department": department, "salary": salary}), 201
