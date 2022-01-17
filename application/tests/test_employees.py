"""This file contains tests for employees views"""

from application import app
from application.models.models import Employee
import unittest


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
                                                   "department": "Test department", "salary": 12345},
                               follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_not_found_employee(self):
        """This test is for checking whether there would be correct response to not found employee"""
        tester = app.test_client(self)
        emps = Employee.query.all()
        response = tester.get(f"/department/{len(emps)+1}", content_type="html/text")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()