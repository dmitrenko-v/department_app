"""This file contains functions for departments
CRUD operations with database"""
from application import db
from application.models.models import Department


def add_department(name):
    """This is service function to add department
    to database"""
    deps = Department.query.all()
    for dep in deps:
        if dep.name == name:
            return
    new_dep = Department(name=name)
    db.session.add(new_dep)
    db.session.commit()


def delete_department(id_):
    """This is service function to delete department
       from database"""
    dep = Department.query.get(id_)
    if not dep:
        return -1
    db.session.delete(dep)
    db.session.commit()


def update_department(id_, name):
    """This is service function to update department"""
    dep = Department.query.get(id_)
    if not dep:
        return -1
    dep.name = name
    db.session.commit()
