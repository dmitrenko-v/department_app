"""This file contains web application forms"""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired


class AddDepartmentForm(FlaskForm):
    """This is form class for adding new department"""
    name = StringField("Name", validators=[DataRequired()])
    add = SubmitField("Add")


class AddEmployeeForm(FlaskForm):
    """This is form class for adding new employee"""
    name = StringField("Name", validators=[DataRequired()])
    birth_date = StringField("Birth date", validators=[DataRequired()])
    department = StringField("Department", validators=[DataRequired()])
    salary = FloatField("Salary", validators=[DataRequired()])
    add = SubmitField("Add")