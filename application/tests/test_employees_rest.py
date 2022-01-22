"""This file contains tests for employees REST API"""

from datetime import date
from application import app, db
from application.models.models import Employee
import unittest


class TestEmployeesRest(unittest.TestCase):
    """This class contains functions for testing employees REST api"""
    def test_employees_get(self):
        """This test is for getting correct response from /api/employees GET request"""
        tester = app.test_client(self)
        response = tester.get("/api/employees")
        self.assertEqual(response.status_code, 200)

    def test_every_employee_get(self):
        """This test is for getting correct response from every /api/employee/<id> GET request"""
        tester = app.test_client(self)
        emps = Employee.query.all()
        for emp in emps:
            response = tester.get(f"/api/employee/{emp.id}")
            self.assertEqual(response.status_code, 200)

    def test_post_employees(self):
        """This test is for getting correct response from /api/employees POST request"""
        tester = app.test_client(self)
        response = tester.post("/api/employees", json={"name": "Test Test", "birth_date": "1111-12-22",
                                                   "department": "Test department", "salary": 12345},
                               follow_redirects=True)
        db.session.delete(Employee.query.filter_by(name="Test Test").first())
        db.session.commit()
        self.assertEqual(response.status_code, 201)

    def test_not_found_employee(self):
        """This test is for checking whether there would be correct response to not found employee"""
        tester = app.test_client(self)
        emps = Employee.query.all()
        max_id = 0
        for emp in emps:
            if emp.id > max_id:
                max_id = emp.id
        response = tester.get(f"/api/employee/{max_id+1}")
        self.assertEqual(response.status_code, 404)

    def test_not_found_delete_employee(self):
        """This test is for checking whether there would be correct response to not found employee"""
        tester = app.test_client(self)
        emps = Employee.query.all()
        max_id = 0
        for emp in emps:
            if emp.id > max_id:
                max_id = emp.id
        response = tester.delete(f"/api/employee/{max_id+1}")
        self.assertEqual(response.status_code, 404)

    def test_put_employee(self):
        """This test is for getting correct response from /api/employee/id PUT request"""
        tester = app.test_client(self)
        # create mock departments for test
        tester.post("/api/employees", json={"name": "Test Test", "birth_date": "1111-12-22",
                                            "department": "Test department", "salary": 12345})
        mock_emp = Employee.query.filter_by(name="Test Test").first()
        # test PUT method on mock department and then delete this department from database
        response = tester.put(f"/api/employee/{mock_emp.id}", json={"name": "Test Test", "birth_date": "1111-12-22",
                                                   "department": "Test department", "salary": 12345})
        db.session.delete(mock_emp)
        db.session.commit()
        self.assertEqual(response.status_code, 201)

    def test_delete_employee(self):
        """This test is for getting correct response from /api/employee/id DELETE request"""
        tester = app.test_client(self)
        # Creating mock employee to test if deleting working properly
        mock_emp = Employee(name="Test Test", birth_date=date(1111, 12, 22),
                            department="Test department", salary=12345)
        db.session.add(mock_emp)
        db.session.commit()
        response = tester.delete(f"/api/employee/{mock_emp.id}")
        self.assertEqual(response.status_code, 201)


if __name__ == "__main__":
    unittest.main()