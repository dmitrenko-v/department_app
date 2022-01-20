"""This file contains tests for department views """

from application import app
from application.models.models import Department
import unittest


class TestDepartmentViews(unittest.TestCase):
    """This is class for departments views testing"""
    def test_departments_get(self):
        """This test is for GET /departments page"""
        tester = app.test_client(self)
        response = tester.get("/departments", content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_every_department_get(self):
        """This test is for GET every /department/<id> page correctly"""
        tester = app.test_client(self)
        deps = Department.query.all()
        for dep in deps:
            response = tester.get(f"/department/{dep.id}", content_type="html/text")
            self.assertEqual(response.status_code, 200)

    def test_post_departments(self):
        """This test is for creating new department from form"""
        tester = app.test_client(self)
        response = tester.post("/departments", data={"name": "Test department"}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_not_found_department(self):
        """This test is for checking whether there would be correct response to not found department"""
        tester = app.test_client(self)
        deps = Department.query.all()
        max_id = 0
        for dep in deps:
            if dep.id > max_id:
                max_id = dep.id
        response = tester.get(f"/department/{max_id+1}", content_type="html/text")
        self.assertEqual(response.status_code, 404)

    def test_edit_department(self):
        tester = app.test_client(self)
        deps = Department.query.all()
        for dep in deps:
            response = tester.post(f"/department/{dep.id}", data={"name": "Test department"}, follow_redirects=True)
            self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()