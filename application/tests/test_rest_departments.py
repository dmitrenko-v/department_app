"""This file contains tests for departments REST API"""

import unittest
from application import app, db
from application.models.models import Department


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
        """This test is for checking whether there would be correct
        response to not found department"""
        tester = app.test_client(self)
        deps = Department.query.all()
        max_id = 0
        for dep in deps:
            if dep.id > max_id:
                max_id = dep.id
        response = tester.get(f"/api/department/{max_id + 1}")
        self.assertEqual(response.status_code, 404)

    def test_not_found_delete_department(self):
        """This test is for checking whether there would be correct
         response to not found department"""
        tester = app.test_client(self)
        deps = Department.query.all()
        max_id = 0
        for dep in deps:
            if dep.id > max_id:
                max_id = dep.id
        response = tester.delete(f"/api/department/{max_id + 1}")
        self.assertEqual(response.status_code, 404)

    def test_put_department(self):
        """This test is for getting correct response from /api/depatment/id PUT request"""
        tester = app.test_client(self)
        # create mock departments for test
        tester.post("/api/departments", json={"name": "Test department"})
        mock_dep = Department.query.filter_by(name="Test department").first()
        # test PUT method on mock department and then delete this department from database
        response = tester.put(f"/api/department/{mock_dep.id}", json={"name": "Test Test"})
        db.session.delete(mock_dep)
        db.session.commit()
        self.assertEqual(response.status_code, 201)

    def test_delete_department(self):
        """This test is for checking whether there would be correct
        response when deleting department"""
        tester = app.test_client(self)
        # Creating mock department to test if deleting working properly
        mock_dep = Department(name="Mock dep")
        db.session.add(mock_dep)
        db.session.commit()
        response = tester.delete(f"/api/department/{mock_dep.id}")
        self.assertEqual(response.status_code, 201)


if __name__ == "__main__":
    unittest.main()
