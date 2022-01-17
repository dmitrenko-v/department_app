"""This file contains functions for CRUD opertaions with database"""
from application import db
from application.models.models import Department


def add_department(name):
    deps = Department.query.all()
    for dep in deps:
        if dep.name == name:
            return
    new_dep = Department(name=name)
    db.session.add(new_dep)
    db.session.commit()


def delete_department(id):
    dep = Department.query.get(id)
    if not dep:
        return -1
    else:
        db.session.delete(dep)
        db.session.commit()


def update_department(id, name):
    dep = Department.query.get(id)
    if not dep:
        return -1
    else:
        dep.name = name
        db.session.commit()