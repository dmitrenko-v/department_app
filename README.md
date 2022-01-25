[![Coverage Status](https://coveralls.io/repos/github/dmitrenko-v/department_app/badge.svg?branch=main)](https://coveralls.io/github/dmitrenko-v/department_app?branch=main)
# Department app
This is simple department web application for performing CRUD operations with database with employees and department
## Installation guide
1. Firstly, you need to install python. You can do it here: https://www.python.org/downloads/
2. Then, you need to install pip. Pip installation guide: https://pip.pypa.io/en/stable/installation/
3. It is strongly recommended to run this application in virtual environment. To create it, do the following steps: 
  - ```pip install virtualenv``` - installing package to create virtual environments
  - ```virtualenv {name of the virtual environment}``` - creating virtual environment
  
  Then, to perform further actions in created environment, type ```source {name of virtual environment}/bin/activate``` in the command line
 
4. The next step is set up the project environment. You can do it from command line in two ways
  - ```pip install -r requirements.txt```
  - ```python setup.py install```
## Usage guide
To run the application you must run "run.py" file 

You can perform CRUD operations through API(POST and PUT methods must include data in json format. Response is JSON) by following urls: 
1. */api/departments*. Possible methods: POST, GET
2. */api/department/{id of department}*. Possible methods: POST, GET, PUT, DELETE
3. */api/employees*. Possible methods: POST, GET
4. */api/employee/{id of employee}*. Possible methods: POST, GET, PUT, DELETE

Also you can do same operations through */departments*, */employees*, */department/{id of department}*, */employee/{id of employee}* in browser.
