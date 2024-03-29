"""This file contains tests for employees views"""

import unittest
from datetime import date
from application import app, db
from application.models.models import Employee


class TestEmployeesViews(unittest.TestCase):
    """This is class for employees views testing"""
    def test_employees_get(self):
        """This test for GET /departments page"""
        tester = app.test_client(self)
        response = tester.get("/employees", content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_every_employee_get(self):
        """This test is for GET every employee page correctly"""
        tester = app.test_client(self)
        emps = Employee.query.all()
        for emp in emps:
            response = tester.get(f"/employee/{emp.id}", content_type="html/text")
            self.assertEqual(response.status_code, 200)

    def test_post_employees(self):
        """This test is for creating new employee from form"""
        tester = app.test_client(self)
        response = tester.post("/employees", data={"name": "Test Test", "birth_date": "1234-56-78",
                                                   "department": "Test department",
                                                   "salary": 12345},
                               follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_not_found_employee(self):
        """This test is for checking whether there would be correct
        response to not found employee"""
        tester = app.test_client(self)
        emps = Employee.query.all()
        max_id = 0
        for emp in emps:
            if emp.id > max_id:
                max_id = emp.id
        response = tester.get(f"/employee/{max_id+1}", content_type="html/text")
        self.assertEqual(response.status_code, 404)

    def test_edit_employees(self):
        """This test is for checking whether there would be correct
        response to editing existing employee"""
        tester = app.test_client(self)
        emps = Employee.query.all()
        for emp in emps:
            response = tester.post(f"/employee/{emp.id}", data={"name": "Test Test",
                                                                "birth_date": "1234-56-78",
                                                                "department": "Test department",
                                                                "salary": 12345},
                                   follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_not_found_delete(self):
        """This test is for checking whether there would be correct
        response to not found employee while deleting one"""
        tester = app.test_client(self)
        emps = Employee.query.all()
        max_id = 0
        for emp in emps:
            if emp.id > max_id:
                max_id = emp.id
        response = tester.get(f"/employee/{max_id+1}/delete")
        self.assertEqual(response.status_code, 404)

    def test_delete_employee(self):
        """This test is for checking whether there would be
        correct response to deleting employee from DB"""
        tester = app.test_client(self)
        # Creating mock employee to test if deleting working properly
        mock_emp = Employee(name="Test Test", birth_date=date(1111, 12, 22),
                            department="Test department", salary=12345)
        db.session.add(mock_emp)
        db.session.commit()
        response = tester.get(f"/employee/{mock_emp.id}/delete")
        self.assertEqual(response.status_code, 302)


if __name__ == "__main__":
    unittest.main()
