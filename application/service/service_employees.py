"""This file contains functions for employees
CRUD operations with database"""
from application import db
from application.models.models import Employee


def add_employee(name, birth_date, department, salary):
    """This is service function to add employee to DB"""
    emps = Employee.query.all()
    for emp in emps:
        if emp.name == name:
            return
    new_emp = Employee(name=name, birth_date=birth_date, department=department, salary=salary)
    db.session.add(new_emp)
    db.session.commit()


def delete_employee(id_):
    """This is service function to delete employee from DB"""
    emp = Employee.query.get(id_)
    if not emp:
        return -1
    db.session.delete(emp)
    db.session.commit()


def update_employee(id_, name, birth_date, department, salary):
    """This is service function to update employee info from DB"""
    emp = Employee.query.get(id_)
    if not emp:
        return -1
    emp.name = name
    emp.birth_date = birth_date
    emp.department = department
    emp.salary = salary
    db.session.commit()
