"""This file contains departments routes to web service
Every route response with JSON"""

from flask import request, jsonify

from application import app
from application.models.models import Department
from application.service.service_departments import add_department, delete_department, \
    update_department


@app.route("/api/departments", methods=["GET"])
def get_departments():
    """This is API to GET all departments"""
    deps = Department.query.all()
    return jsonify([{"name": dep.name} for dep in deps])


@app.route("/api/department/<id_>", methods=["GET"])
def get_department(id_):
    """This is API to GET department with given id"""
    dep = Department.query.get(id_)
    if not dep:
        return jsonify({"error": "Department not found"}), 404
    return jsonify({"name": dep.name})


@app.route("/api/departments", methods=["POST"])
def add_department_api():
    """This is API to add new department"""
    name = request.json.get("name", "")
    if not name:
        return jsonify({"error": "Incorrect request"})
    add_department(name)
    return jsonify({"name": name}), 201


@app.route("/api/department/<id_>", methods=["DELETE"])
def delete_department_api(id_):
    """This is API to delete existing department"""
    if delete_department(id_) == -1:
        return jsonify({"error": "Department not found"}), 404
    return "", 201


@app.route("/api/department/<id_>", methods=["PUT"])
def update_department_api(id_):
    """This is API to update existing department"""
    name = request.json.get("name", "")
    if not name:
        return jsonify({"error": "Incorrect request"})
    if update_department(id_, name) == -1:
        return jsonify({"error": "Department not found"}), 404
    return jsonify({"name": name}), 201
