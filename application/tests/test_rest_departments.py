"""This file contains tests for departments REST API"""
from application import app, db
from application.models.models import Department
import unittest


class TestDepartmentsRest(unittest.TestCase):
    """This class contains functions for testing departments REST api"""
    def test_departments_get(self):
        """This test is for getting correct response from /api/departments GET request"""
        tester = app.test_client(self)
        response = tester.get("/api/departments")
        self.assertEqual(response.status_code, 200)

    def test_departments_post(self):
        """This test is for getting correct response from /api/departments POST request"""
        tester = app.test_client(self)
        response = tester.post("api/departments", json={"name": "Test department"})
        db.session.delete(Department.query.filter_by(name="Test department").first())
        db.session.commit()
        self.assertEqual(response.status_code, 201)

    def test_every_department_get(self):
        """This test is for getting correct response from every /api/department/<id> GET request"""
        tester = app.test_client(self)
        deps = Department.query.all()
        for dep in deps:
            response = tester.get(f"/api/department/{dep.id}")
            self.assertEqual(response.status_code, 200)

    def test_not_found_department(self):
        """This test is for checking whether there would be correct response to not found department"""
        tester = app.test_client(self)
        deps = Department.query.all()
        max_id = 0
        for dep in deps:
            if dep.id > max_id:
                max_id = dep.id
        response = tester.get(f"/api/department/{max_id + 1}")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
