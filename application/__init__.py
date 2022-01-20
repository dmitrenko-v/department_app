from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dep.db"
app.config["SECRET_KEY"] = '47f4404b0e04eda30c88d0112e6cc3985f2a8412f9c88e25d0a6c900d1a11885'

db = SQLAlchemy(app)

from application.views import views_employees, views_departments
from application.rest import rest_departments, rest_employees