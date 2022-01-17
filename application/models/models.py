"""This module contains database models"""
from application import db


class Department(db.Model):
    """Department table contains id(primary key) and name of department"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Department {self.name}"


class Employee(db.Model):
    """Employee table contains id(primary key), name, birth date, department and salary of employee"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    department = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Employee {self.name} from {self.department} Department born on {self.birth_date} earns {self.salary}"