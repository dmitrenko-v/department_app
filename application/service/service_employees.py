from application import db
from application.models.models import Employee


def add_employee(name, birth_date, department, salary):
    emps = Employee.query.all()
    for emp in emps:
        if emp.name == name:
            return
    new_emp = Employee(name=name, birth_date=birth_date, department=department, salary=salary)
    db.session.add(new_emp)
    db.session.commit()


def delete_employee(id):
    emp = Employee.query.get(id)
    if not emp:
        return -1
    else:
        db.session.delete(emp)
        db.session.commit()


def update_employee(id, name, birth_date, department, salary):
    emp = Employee.query.get(id)
    if not emp:
        return -1
    else:
        emp.name = name
        emp.birth_date = birth_date
        emp.department = department
        emp.salary = salary
        db.session.commit()